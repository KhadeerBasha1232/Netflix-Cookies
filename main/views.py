import random
import shutil
import zipfile
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


def post(request, *args, **kwargs):
    uploaded_file = request.FILES.get('zip_file')

    if uploaded_file:
        print("uploaded")
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension == 'zip':
            # Create a temporary directory to extract files
            temp_dir = 'temp_extraction_dir'
            os.makedirs(temp_dir, exist_ok=True)

            try:
                # Extract the zip file
                with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)


                # Move all text files to the 'cookies' folder
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith('.txt'):
                            src_path = os.path.join(root, file)
                            dest_path = os.path.join('cookies', file)
                            os.rename(src_path, dest_path)

                # Clean up the temporary directory
                shutil.rmtree(temp_dir)

                return render(request, "upload.html", {'message': 'Extraction successful'})
            except Exception as e:
                shutil.rmtree(temp_dir)
                return render(request, "upload.html", {'message': f'Error: {e}'})
        else:
            return render(request, "upload.html", {'message': 'Invalid file format'})
    else:
        return render(request, "upload.html", {'message': 'No file selected'})
