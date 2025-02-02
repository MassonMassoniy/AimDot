# Created by Masson Massoniy.

from tkinter import Tk, Canvas, Toplevel, StringVar, OptionMenu, Menu, Button, Label, PhotoImage, filedialog, messagebox, _tkinter
from pystray import MenuItem, Icon
from PIL import Image, ImageDraw

from os import sys, listdir, execl

class AimDotApp:
    """AimDotApp is a class that creates a window with an aim dot in the center of the screen."""

    def __init__(self):
        self.BACKGROUND_COLOR = "#000001"
        self.saved_dot_images = listdir("dots") # List of saved dot images
        self.dot_image_path = r"dots\x8Dot_Tp_Y.png" # Default dot image path
        self.screen = None
        self.dot_image = None
        self.dot_image_width = None
        self.dot_image_height = None

    def _initialize_window(self):
        """Initialize the tkinter window."""

        self.screen = Tk()
        self.screen.title("Aim Dot")
        self.screen.attributes("-fullscreen", True)
        self.screen.attributes("-topmost", True)
        self.screen.resizable(False, False)
        self.screen.wm_attributes("-transparentcolor", self.BACKGROUND_COLOR)
        self.screen.configure(bg = self.BACKGROUND_COLOR)

        self._tray_menu()
        
        "------------------------------------------------------------------------------------"

        self._load_dot_image()
        self._create_canvas()
        
        self.screen.mainloop()

    def _tray_menu(self):
        """Create a tray menu."""
        logo = Image.new('RGB', (64, 64), color=(73, 109, 137))
        draw = ImageDraw.Draw(logo)
        draw.rectangle((0, 0, 64, 64), fill=(73, 109, 137))

        menu = (
            MenuItem('Select Dot', self._select_dot_window),
            MenuItem('Quit', self._quit)
        )

        self.tray_icon = Icon("Aim Dot", logo, "AimDot App", menu)
        self.tray_icon.run_detached()

    def _open_file_dialog(self):
        """Open a file dialog to select the dot image."""

        file_path = filedialog.askopenfilename(
                title = "Select Aim Dot Image",
                filetypes = [("PNG files", "*.png"), ("All files", "*.*")]
            )
        
        self.dot_image_path = file_path if file_path != "" else self.dot_image_path

    def _load_dot_image(self):
        """Load the dot image."""

        try:
            self.dot_image = PhotoImage(file = self.dot_image_path)
            self.dot_image_width = self.dot_image.width()
            self.dot_image_height = self.dot_image.height()
        except _tkinter.TclError:
            yesno = str(messagebox.showinfo("Aim Dot",
                                           f"No such file or directory: \"{self.dot_image_path}\"\n"
                                           "Would you like to try again?",
                                           icon = "warning",
                                           type = "yesno"))
            if yesno == "no":
                self._quit()
            elif yesno == "yes":
                self._open_file_dialog()
                self._load_dot_image()
        except Exception as e:
            messagebox.showinfo("Aim Dot",
                                f"An unknown error occurred: {e}",
                                icon = "warning")
    
    def _select_dot_window(self):
        """Select the dot image."""

        selector_window = Toplevel(self.screen)
        selector_window.title("Select Aim Dot")
        selector_window.geometry("300x100")
        selector_window.resizable(False, False)

        clicked = StringVar()
        clicked.set(self.dot_image_path.split("\\")[-1])

        drop = OptionMenu(selector_window, clicked, *self.saved_dot_images)
        drop.pack(pady = 10)

        apply_button = Button(selector_window,
                              text = "Apply",
                              command = lambda: (self._apply_dot(clicked.get()),
                                                 selector_window.destroy()))
        apply_button.pack(pady = 10)

    def _apply_dot(self, dot_image):
        """Apply the selected dot image."""

        self.dot_image_path = f"dots\\{dot_image}"
        self._load_dot_image()

        self.canvas.destroy()
        self._create_canvas()
        

    def _create_canvas(self):
        """Display the dot image on the canvas."""

        self.canvas = Canvas(
            self.screen,
            height = self.dot_image_height,
            width = self.dot_image_width,
            bg = self.BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.canvas.place(
            relx = 0.5,
            rely = 0.5,
            anchor = "center")
        self.canvas.create_image(
            self.dot_image_width // 2,
            self.dot_image_height // 2,
            image = self.dot_image,
            anchor = "center"
        )
    
    def _quit(self):
        """Quit the application."""

        self.screen.quit()
        self.screen.after(0, self.screen.destroy)
        sys.exit()

    def run(self):
        """Run the application."""
        
        self._initialize_window()

if __name__ == "__main__":
    app = AimDotApp()
    app.run()