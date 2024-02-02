import random
from django.shortcuts import render
from django.http import JsonResponse
import os


def index(request):
    return render(request,"index.html")

def get( request, *args, **kwargs):
        folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'cookies')

        # Get a list of all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        if not files:
            text_content = 'No files in the folder'
        else:
            # Randomly select one file from the list
            random_file = random.choice(files)

            # Read content from the randomly selected file
            file_path = os.path.join(folder_path, random_file)
            with open(file_path, 'r') as file:
                text_content = file.read().strip()
        context = {
            'text_content': text_content,
        }

        return render(request, "netflix.html", context)


def get_random_content(self, *args, **kwargs):
    # Assuming 'netflix' is a folder in the same directory as your Django project
    folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'cookies')

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        return JsonResponse({'text_content': 'No files in the folder'})

    # Randomly select one file from the list
    random_file = random.choice(files)

    # Read content from the randomly selected file
    file_path = os.path.join(folder_path, random_file)
    with open(file_path, 'r') as file:
        random_content = file.read().strip()

    return JsonResponse({'text_content': random_content})
