# Created by Masson Massoniy.

from tkinter import Tk, Canvas, PhotoImage, filedialog, messagebox, _tkinter
from os import sys, execl

class AimDotApp:
    """AimDotApp is a class that creates a window with an aim dot in the center of the screen."""

    def __init__(self):
        self.BACKGROUND_COLOR = "#000001"
        self.dot_image_path = r"dots/x12Dot_Tp_Y.png" # Default dot image path
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
    
    def _create_canvas(self):
        """Create a canvas and display the dot image."""

        canvas = Canvas(
            self.screen,
            height = self.dot_image_height,
            width = self.dot_image_width,
            bg = self.BACKGROUND_COLOR,
            highlightthickness=0
        )
        canvas.place(
            relx = 0.5,
            rely = 0.5,
            anchor = "center")
        canvas.create_image(
            self.dot_image_width // 2,
            self.dot_image_height // 2,
            image = self.dot_image,
            anchor = "center"
        )
    
    def _quit(self):
        """Quit the application."""

        self.screen.quit()
        self.screen.destroy()
        sys.exit()

    def run(self):
        """Run the application."""
        
        self._initialize_window()
        self._load_dot_image()
        self._create_canvas()
        self.screen.mainloop()

if __name__ == "__main__":
    app = AimDotApp()
    app.run()