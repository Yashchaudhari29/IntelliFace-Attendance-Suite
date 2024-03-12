from college_admin.models import *
import os

def Insert(en_no, name,img):
    a = register.objects.create(en_no=en_no, name=name,img=img,cap_img=None)
    return a

def Emptying():
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory,'img')
    print(file_path)
    try:
        if os.path.exists(file_path):
            for img in os.listdir(file_path):
                os.remove(f"{file_path}/{img}")
            print(f"File {file_path} removed successfully.")
        else:
            print(f"File {file_path} does not exist.")
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")

    current_directory = os.getcwd()
    file_path = os.path.join(current_directory,'cap_images')
    print(file_path)
    try:
        if os.path.exists(file_path):
            for img in os.listdir(file_path):
                os.remove(f"{file_path}/{img}")
            print(f"File {file_path} removed successfully.")
        else:
            print(f"File {file_path} does not exist.")
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")

