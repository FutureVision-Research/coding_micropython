import tkinter as tk  # Import the tkinter library and call it 'tk' for short (This is a standard practice with tkinter)

# Ask the user to type their name in the console
name = input("What is your name? ")  # Stores the user's name as a string

# Create the main window
window = tk.Tk()               # Make a new Tkinter window (The window object is called "window")
window.title("Greeting App")   # Set the title of the window
window.geometry("300x150")     # Set a good window size so the window controls are easy to access

# Create a label that says hello using the name
greeting = tk.Label(           # Create a Label widget. (Widgets are GUI elements like labels, buttons, and entry boxes.)
    window,                    # Specify that this label should appear in the object named window
    text="Hello, " + name + "!",  # Set the text to say hello to the user. Notice that you don't need curly braces as you do with f-string.
    font=("Arial", 20)         # Choose a font and size
)
greeting.pack(pady=20)         # .pack stacks widgets on top of each other (vertically). pady specifies 20 pixels of vertical padding

# Start the GUI loop This keeps the window open and the script continues to run untill the window is closed.
window.mainloop()
