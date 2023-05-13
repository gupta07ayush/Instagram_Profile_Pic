from tkinter import Tk, Label, Button, Entry, PhotoImage, messagebox
import instaloader


# create object of instaloader class
insta_obj = instaloader.Instaloader()


# Function which will download the instagram profile Pic
def download():
    # get the user name from entry box
    username = user_entry.get()

    # download the profile pic
    insta_obj.download_profile(username, profile_pic_only=True)

    # Display this message in terminal
    print('Downloading Image')

    # display the message after downloading the image
    messagebox.showinfo('Success', 'Profile Pic is successfully downloaded.')


# Create an object of Tk Class
root = Tk()

# Set the title of the root Window
root.title("Instagram Profile Pic Downloader")

# Set the window size
root.geometry('700x400')

# Set the backgroud color of the root window
root.config(bg="#405DE6")

# create an object of logo file
logo_image = PhotoImage(file='instagram.png')

# Label for Logo image
logo_label = Label(root, image=logo_image, bg='#405DE6')
logo_label.place(x=90, y=310)
logo_label = Label(root, image=logo_image, bg='#405DE6')
logo_label.place(x=570, y=310)

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
                         bg="#FD1D1D", fg='black', font=('Helvetika', 18, 'bold'), command=download)
download_button.place(x=260, y=310, width=200, height=60)


# Start the GUI
root.mainloop()
