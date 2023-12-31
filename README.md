# comic_strip_creator

## About the Project
This is a django app made for an assignment of a placement selection process.
In this django app I have used an API which generates comic strip using text prompts from users.

## Installation 

To install the following app on your local system follow the steps given below:

- Install Python 3.10.7
- Install virtualenv
- Create a folder by whatever name your want to give. Example: Dashtoon
- Open the Dashtoon folder in VS Code. Open the terminal.
- Create a virtual environment: 
    ```
    virtualenv myenv
    ```
- Switch to the newly created environment:
    ```
    cd myenv/Scripts
    ```
    ```
    ./activate
    ```
- Return Back to the parent directory:
    ```
    cd ../../
    ```
- Clone the repository:
    ```
    git clone https://github.com/Vaibhav-22-dm/comic_strip_creator.git
    ```
- Change directory to newly cloned repository:
    ```
    cd comic_strip_creator
    ```
- Build the environment using the given requirements:
    ```
    pip install -r requirements.txt
    ```

- Start the django server:
    ```
    python manage.py runserver
    ```

- Visit http://127.0.0.1:8000/ to generate comic strip.

