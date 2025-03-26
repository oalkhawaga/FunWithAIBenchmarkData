# File Name : visualization.py
# Student Name: Omar Alkhawaga
# email: alkhawoe@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The assignment is to add some data visualization into Python project in Visual Studio.
# Brief Description of what this module does: This module creates a visualization using matplotlib, its chart that shows the values of the attributes
# Citations: https://chatgpt.com/   https://pypi.org/project/matplotlib/
# Anything else that's relevant:N/A
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def create_chart():
    """
    Creates a sample bar chart for data visualization.
    @return: Matplotlib Figure object.
    """
    categories = ['Attack', 'Defense', 'Speed', 'HP', 'Special']
    values = [85, 87, 76, 90, 85]  # Sample Pokemon stats

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(categories, values, color=['red', 'blue', 'green', 'purple', 'orange'])
    ax.set_title("Pokemon Stats")
    ax.set_xlabel("Attributes")
    ax.set_ylabel("Values")

    return fig

def display_chart(root):
    """
    Displays the chart in a Tkinter window.
    @param root: Tkinter root window.
    """
    figure = create_chart()
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack(side=tk.RIGHT, padx=10, pady=10)