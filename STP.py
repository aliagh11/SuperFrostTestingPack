import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

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

#Loading testing window background image
testing_window_bg_image = Image.open("C:/Users/admin/Desktop/STP/Images/startbg.jpg")
testing_window_bg_photo = ImageTk.PhotoImage(testing_window_bg_image)


#Start button functions
def start_clicked():
    #Starting a new window for start (start-window)
    start_window = tk.Toplevel()
    start_window.geometry("1000x600")
    start_window.title(" Testing ...")
    start_window.resizable(False, False)
    start_window_bg_label = tk.Label(start_window, image=testing_window_bg_photo)
    start_window_bg_label.pack()
    
    # Importing excel file function
    def import_excel_file():
        file_path = filedialog.askopenfilename(
        title="Select an Excel file",
        filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
    )
        # Check if a file path was selected
        if file_path:
            try:
                df = pd.read_excel(file_path)
                #Here you can process your data :)
            except Exception as e:
                print(f"An error occurred while trying to read the file: {e}")
    
    #Creating importing excel file button
    import_excel_button = tk.Button(start_window, text="Import Excel File", command = lambda: import_excel_file())
    import_excel_button.place(relx=0.09, rely=0.17)

    # Refrigerator model selection dropbox
    model_selection_box = tk.Label(start_window, text="Refrigerator Model:", font=("Times New Roman", 10))
    Refrigerators = ["SUF-60", "SUR-60", "NCS-9080", "SF-2150", "SR-2150"]
    selected_refrigerator_model = tk.StringVar(start_window)
    selected_refrigerator_model.set("Select Refrigerator Model")
    dropdown = tk.OptionMenu(start_window, selected_refrigerator_model, *Refrigerators)
    dropdown.place(relx=0.055, rely=0.1)
    dropdown["width"] = 20

    #Date of testing text and entry
    testing_date_text = tk.Label(start_window, text="  Date of testing ", bg="light gray", font=("Times New Roman", 10))
    testing_date_text.pack()
    testing_date_text.place(relx=0.1, rely=0.25, anchor='center')
    testing_date_entry = tk.Entry(start_window, bg="#D3D3D3", highlightbackground="red", highlightcolor="red", width = 10, justify="center")
    testing_date_entry.pack()
    testing_date_entry.place(relx=0.19, rely=0.25, anchor='center')

    #Serial No. text and entry
    serial_No_text = tk.Label(start_window, text="  Serial No. ", bg="light gray", font=("Times New Roman", 10))
    serial_No_text.pack()
    serial_No_text.place(relx=0.1, rely=0.30, anchor='center')
    Serial_No_entry = tk.Entry(start_window, bg="#D3D3D3", highlightbackground="red", highlightcolor="red", width = 10, justify="center")
    Serial_No_entry.pack()
    Serial_No_entry.place(relx=0.19, rely=0.30, anchor='center')
    
    #Closing start_window button
    close_button = tk.Button(start_window, text="Close", command=start_window.destroy)
    close_button.place(relx=0.50,rely=0.9)

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