from tkinter import Tk, Label, Button, Entry

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
user_label.place(x=20, y=210, width=200, height=40)

# User name Entry field
user_entry = Entry(root, bg="#C13584", fg='white', border=5,
                   font=('Helvetika', 14, 'bold'))
user_entry.place(x=240, y=210, width=440, height=40)
user_entry.focus()
user_entry.configure(insertbackground='yellow')

# Download Button
download_button = Button(root, text="Download", border=10, cursor='circle #833AB4',
                         bg="#FD1D1D", fg='black', font=('Helvetika', 18, 'bold'))
download_button.place(x=260, y=310, width=200, height=60)


# Start the GUI
root.mainloop()
