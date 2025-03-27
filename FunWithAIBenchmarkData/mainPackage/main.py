# main.py
import tkinter as tk
from imagePackage.image import display_image
from DataVisualizationPackage.visualization import display_chart

def main():
    """
    Main function to display image and data visualization.
    @param: N/A
    @returns: N/A
    """
    nidoking = tk.Tk()
    nidoking.title("Image and Data Visualization")

    display_image(nidoking, "imagePackage/image.png")  
    display_chart(nidoking)  

    nidoking.mainloop()

if __name__ == "__main__":
    main()