# image.py
# File Name : image.py
# Student Name: Kengo Ishizuka
# email: ishizuko@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to add some data visualization into Python project in Visual Studio.

# Brief Description of what this module does: This module reads, resizes, and displays the image of our team's name.
# Citations: https://www.geeksforgeeks.org/reading-images-in-python/
#            https://www.geeksforgeeks.org/loading-images-in-tkinter-using-pil/
#            https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
#            https://stackoverflow.com/questions/24848917/adding-and-removing-image-tkinter-root

# Anything else that's relevant:

# image.py
from PIL import Image, ImageTk
import tkinter as tk

def resize_image(image_path, max_size=(200, 200)):
    """
    Reads and resizes an image.
    @param image_path: str - Path to the image file.
    @param max_size: tuple - Maximum width and height for resizing.
    @return: Image object or None if failed.
    """
    try:
        image = Image.open(image_path)
        image.thumbnail(max_size, Image.LANCZOS)
        return image
    except Exception as e:
        print(f"Error: Unable to open image {image_path}. {e}")
        return None

def display_image(root, image_path):
    """
    Displays an image in a Tkinter window.
    @param root: Tkinter root window.
    @param image_path: str - Path to the image file.
    """
    image = resize_image(image_path)
    if image:
        img_tk = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=img_tk)
        label.image = img_tk  # Keep reference to avoid garbage collection
        label.pack(side=tk.LEFT, padx=10, pady=10)
