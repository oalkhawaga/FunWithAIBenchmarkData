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

from PIL import Image, ImageTk

import tkinter as tk
 
def resize_image(image_path, max_size=(200, 200)):
    """
    Reads and resize an image.
    @param image_path string: The path to the image file.
    @param max_size int: The size of the image.
    """
    image = Image.open(image_path)
    image.thumbnail(max_size, Image.LANCZOS)
    return image
 
def display_image(image_path):
    """
    Displays the image using Tkinter
    @param filename string: The path to the image file.
    """
    image = resize_image(image_path)
    root = tk.Tk()
    root.title("Image Viewer")
    img_tk = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=img_tk)
    label.pack()
    root.mainloop()
