import tkinter as tk
from gui import GUI

def main():
    root = tk.Tk()
    app = GUI(root)  # Initialize the GUI class with the root window
    root.mainloop()

if __name__ == "__main__":
    main()
