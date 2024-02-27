import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
        df = None  # Initialize df to ensure it exists even if no file is selected
        file_path = filedialog.askopenfilename(
            title="Select an Excel file",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
        )
        # Check if a file path was selected
        if file_path:
            try:
                df = pd.read_excel(file_path)
                # Data processing can be done here :)
            except Exception as e:
                print(f"An error occurred while trying to read the file: {e}")

        return df  # Return the DataFrame (or None if no file was selected)
    
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

    ##############################################################################################################
    #################################################### Check-list ##############################################
    ##############################################################################################################

    # Function to open the checklist window
    def open_checklist():
        # Function to update the label with the checklist status
        def update_status():
            status = []
            for i, var in enumerate(check_vars):
                status.append(f"Item {i+1}: {'✓' if var.get() else '✗'}")
            status_label.config(text="\n".join(status))
        # Create a Toplevel window
        checklist_window = tk.Toplevel(root)
        checklist_window.title("Checklist")
        checklist_window.geometry("500x500")
        checklist_window.resizable(False, False)

        # Frame to hold the checkbuttons and right-align them
        checklist_frame = tk.Frame(checklist_window)
        checklist_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # List of items for the checklist
        items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']

        # Create a list to store the IntVars associated with each checkbutton
        check_vars = []

        # Create a Checkbutton for each item
        for item in items:
            var = tk.IntVar(value=0)  # 0 for not checked, 1 for checked
            check_vars.append(var)
            checkbutton = tk.Checkbutton(checklist_window, text=item, variable=var, command=update_status)
            checkbutton.pack()

        # Status label to show the checklist status
        status_label = tk.Label(checklist_window)
        status_label.pack()

        # Initialize the status label
        update_status()

        #Function for saving the check-list
        def save_check_list():
            #Save the tick and x signs and destroy window.
            a = 1+1

        #Save check list button
        Save_checklist_button = tk.Button(checklist_window, text="Save", command = save_check_list)
        Save_checklist_button.place(relx=0.5, rely=0.5)

    # Button to open the checklist
    open_checklist_button = tk.Button(start_window, text="Open Checklist", command=open_checklist)
    open_checklist_button.place(relx=0.1,rely=0.34)

############################################################################################################################################ 
############################################################################################################################################ 

    ##############################################################################################################
    #################################################### Plot type ###############################################
    ##############################################################################################################
    # plot to show drop-down
    plot_type_dropdown = tk.Label(start_window, text="Plot type:", font=("Times New Roman", 10))
    plot_types = ["Temperatures", "Current", "Voltage", "Power"]
    selected_plot_type = tk.StringVar(start_window)
    selected_plot_type.set("Select Plot to Show")
    plot_type_dropdown = tk.OptionMenu(start_window, selected_plot_type, *plot_types)
    plot_type_dropdown.place(relx=0.055, rely=0.40)
    plot_type_dropdown["width"] = 20

    ################################################################################################################
    # --------------------------------------------- saving to data base ------------------------------------------ #
    ################################################################################################################

    saving_to_db_checkbox = tk.IntVar()
    saving_to_db_checkbox = tk.Checkbutton(start_window, text="Save to Data Base ", variable=saving_to_db_checkbox)
    saving_to_db_checkbox.pack()
    saving_to_db_checkbox.place(relx=0.08,rely=0.47)

    # ------------------------------------------------------------------------------------------------------------ #

    ################################################################################################################
    # ---------------------------------------------- sending e-mails --------------------------------------------- # 
    ################################################################################################################
    sending_email_checkbox = tk.IntVar()
    sending_email_checkbox = tk.Checkbutton(start_window, text="Send report to R&D team ", variable=saving_to_db_checkbox)
    sending_email_checkbox.pack()
    sending_email_checkbox.place(relx=0.057,rely=0.52)

    # ------------------------------------------------------------------------------------------------------------- #

    #################################################################################################################
    # ------------------------------------------------ STARTING TEST ---------------------------------------------- #
    #################################################################################################################

    def plotting(df):
        if df is not None:  # Make sure df is not None
            fig = Figure(figsize=(6,5), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(df["Time"], df["T1"])
            ax.grid(True)
            canvas = FigureCanvasTkAgg(fig, master=start_window)
            canvas.draw()
            canvas.get_tk_widget().pack()
            canvas.get_tk_widget().place(relx=0.33, rely=0.05)
            canvas.get_tk_widget().lift()
        else:
            print("No DataFrame to plot")
    
    starting_test_button = tk.Button(start_window, text=" Start test \n 📈 ", command = lambda: plotting(df), font=('Lucida Handwriting', 9, 'bold'), bg="#FF7F7F")
    starting_test_button.place(relx=0.1, rely=0.58)

    #Initial plot for just visual aspect of plots in start window
    fig = Figure(figsize=(6,5), dpi=100)
    ax = fig.add_subplot(111)
    ax.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=start_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(relx=0.33, rely=0.05)
    canvas.get_tk_widget().lift()

    
        

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