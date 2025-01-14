from PIL import Image
from pystray import Icon as icon, MenuItem as item, Menu as menu
import threading

def setup_icon():
    image = Image.open("icon.png")  # Path to an icon image
    icon = icon('test', image, menu=menu(
        item('Open', on_open),
        item('Exit', on_exit)))

    icon.run()

def on_open(icon, item):
    icon.stop()
    main_window.deiconify()  # Show the main window

def on_exit(icon, item):
    icon.stop()
    app_running = False  # Set a flag to stop the application loop

def start_tray_icon():
    threading.Thread(target=setup_icon).start()

# GUI setup and other functionalities are handled here
