from django.http import HttpResponse
from django.shortcuts import render
import requests
import concurrent.futures
from .models import *
from django.core.files.base import ContentFile

API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "image/png",
    "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
    "Content-Type": "application/json",
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content


# Create your views here.
def index(request):
    if request.method == "POST":
        prompts = [request.POST.get(f"prompt-{i}") for i in range(10)]
        comicstrip = ComicStrip.objects.create()
        panels = []
        # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        #     processes = [
        #         executor.submit(
        #             requests.post, API_URL, headers=headers, json={"inputs": prompt}
        #         )
        #         for prompt in prompts
        #     ]
            # for i, process in enumerate(concurrent.futures.as_completed(processes)):
        for prompt in prompts:
            try:
                image_bytes = query({
                     "inputs": prompt
                })
                panel = ComicPanel.objects.create(
                    comicstrip=comicstrip,
                    prompt=prompt,
                )
                panel.image.save(
                    f"image-{panel.id}-{comicstrip.id}.png",
                    ContentFile(image_bytes),
                    save=True,
                )
                panels.append(panel)
            except Exception as e:
                print(str(e))
        return render(
            request,
            "app/index.html",
            {"panels": panels, "comicstrip_id": comicstrip.id},
        )
    return render(request, "app/index.html")
