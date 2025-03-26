# main.py
import tkinter as tk
from imagePackage.image import display_image
from DataVisualizationPackage.visualization import display_chart

def main():
    """Main function to display image and data visualization."""
    root = tk.Tk()
    root.title("Image and Data Visualization")

    display_image(root, "imagePackage/image.png")  
    display_chart(root)  

    root.mainloop()

if __name__ == "__main__":
    main()