from tkinter import Tk, Label, Button

# Create an object of Tk Class
root = Tk()

# Set the title of the root Window
root.title("Instagram Profile Pic Downloader")

# Set the window size
root.geometry('700x400')

# Set the backgroud color of the root window
root.config(bg="#405DE6")

# Label for the heading
heading = Label(root, text='Instagram Profile Pic\n Downloader',
                bg="#F56040", font=('times new roman', 40, 'bold'))
heading.place(x=20, y=20, width=660, height=150)

# Enter Username Label
user_label = Label(root, text="Enter User Name:",
                   bg="#FCAF45", fg='black', font=('Helvetika', 14, 'bold'))
user_label.place(x=20, y=200, width=200, height=40)


# Start the GUI
root.mainloop()
