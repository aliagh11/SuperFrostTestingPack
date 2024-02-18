import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd

# Create the main window
root = tk.Tk()
root.title("SperFrost Testing Pack (STP)")
root.geometry("1000x600")
root.resizable(False, False)

#Gradient Background
bg_image = Image.open("C:/Users/admin/Desktop/STP/Images/Background.jpg")
width, height = 1000, 600
bg_image = bg_image.resize((width, height))
bg_photo = ImageTk.PhotoImage(bg_image)
# Create a label widget to display the image
bg_label = tk.Label(root, image=bg_photo)
bg_label.pack()

#Start button functions
def start_clicked():
    #Starting a new window for start (start-window)
    start_window = tk.Toplevel()
    start_window.geometry("1000x600")
    start_window.resizable(False,False)
    start_window.title("Testing ...")
    start_window_label.pack()
    close_button = tk.Button(start_window, text="Close", command=start_window.destroy)
    close_button.pack()

    #Upload excel button
    def excel_button_clicked():
        file_path = filedialog.askopenfilename(
            title="Select an Excel file",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*")) # You can adjust the filetypes to restrict to certain file extensions
        )
        if file_path:  # If a file was selected
            print(f"File selected: {file_path}")
            df = pd.read_excel(file_path)

#Creating Start button
start_button = tk.Button(root, text=" Start test \n 📈 ", command = lambda: start_clicked(), font=('Lucida Handwriting', 9, 'bold'), bg="#FF7F7F")
start_button.place(relx=0.46, rely=0.7)

#License button function
def license_clicked():
    print("Button was clicked!")

license_button = tk.Button(root, text="Check License Terms \n  📄 ", command = lambda: license_clicked(), font=('Lucida Handwriting', 9, 'bold'), bg="#ADD8E6")
license_button.place(relx=0.56, rely=0.7)

#User manual button function
def user_manual_clicked():
    print("Button was clicked!")

user_manual_button = tk.Button(root, text="Check User Manual \n  📄 ", command = lambda: user_manual_clicked(), font=('Lucida Handwriting', 9, 'bold'), bg="#ADD8E6")
user_manual_button.place(relx=0.285, rely=0.7)

# Run the application
root.mainloop()