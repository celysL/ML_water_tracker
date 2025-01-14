import tkinter as tk
from PIL import Image, ImageTk
from pystray import Icon as icon, MenuItem as item, Menu as menu
import threading
from camera import Camera  # Import your Camera class

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter and OpenCV Application")
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)  # Hide instead of close

        # Initialize camera to None initially
        self.camera = None
        self.is_camera_running = False

        self.setup_gui()
        threading.Thread(target=self.setup_system_tray).start()

    def setup_gui(self):
        # Label
        self.label = tk.Label(self.root, text="This is the main window")
        self.label.pack()

        # Buttons to start and stop the camera
        self.start_button = tk.Button(self.root, text="Start Camera", command=self.start_camera)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Camera", command=self.stop_camera, state=tk.DISABLED)
        self.stop_button.pack()

        # Canvas for Camera Feed
        self.canvas = tk.Canvas(self.root, width=640, height=480, bg="black")
        self.canvas.pack()

    def start_camera(self):
        """Start the camera feed."""
        if not self.is_camera_running:
            self.camera = Camera()  # Initialize the camera
            self.is_camera_running = True
            self.start_button.config(state=tk.DISABLED)  # Disable Start button
            self.stop_button.config(state=tk.NORMAL)  # Enable Stop button
            self.update_camera()

    def stop_camera(self):
        """Stop the camera feed."""
        if self.is_camera_running:
            self.is_camera_running = False
            if self.camera:
                self.camera.release()  # Release the camera resource
                self.camera = None  # Ensure the camera object is reset
            self.canvas.delete("all")  # Clear the canvas
            self.start_button.config(state=tk.NORMAL)  # Enable Start button
            self.stop_button.config(state=tk.DISABLED)  # Disable Stop button

    def update_camera(self):
        """Continuously update the camera feed."""
        if self.is_camera_running and self.camera:
            ret, frame = self.camera.get_frame()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        if self.is_camera_running:
            self.root.after(10, self.update_camera)  # Refresh every 10ms

    def hide_window(self):
        """Minimize to system tray instead of closing."""
        self.root.withdraw()

    def show_window(self):
        """Restore the main window from the system tray."""
        self.root.deiconify()

    def exit_application(self):
        """Stop the application."""
        self.stop_camera()  # Ensure the camera is stopped before exiting
        if self.icon:
            self.icon.stop()
        self.root.destroy()

    def setup_system_tray(self):
        image = Image.open("icon.png")  # Ensure the icon.png is in the correct path
        self.icon = icon('AppName', image, menu=menu(
            item('Open', lambda: self.show_window()),
            item('Exit', lambda: self.exit_application())))
        self.icon.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
