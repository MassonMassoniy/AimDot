# Created by Masson Massoniy.

from tkinter import Tk, Canvas, PhotoImage, mainloop

class AimDotApp:
    """AimDotApp is a class that creates a window with an aim dot in the center of the screen."""

    def __init__(self, dot_image_path):
        self.BACKGROUND_COLOR = "#000001"
        self.dot_image_path = dot_image_path
        self.screen = None
        self.dot_image = None
        self.dot_image_width = None
        self.dot_image_height = None
        
    def initialize_window(self):
        """Initialize the tkinter window."""

        self.screen = Tk()
        self.screen.title("Aim Dot")
        self.screen.attributes("-fullscreen", True)
        self.screen.attributes("-topmost", True)
        self.screen.resizable(False, False)
        self.screen.wm_attributes("-transparentcolor", self.BACKGROUND_COLOR)
        self.screen.configure(bg = self.BACKGROUND_COLOR)

    def load_dot_image(self):
        """Load the dot image."""

        self.dot_image = PhotoImage(file = self.dot_image_path)
        self.dot_image_width = self.dot_image.width()
        self.dot_image_height = self.dot_image.height()
    
    def create_canvas(self):
        """Create a canvas and display the dot image."""

        canvas = Canvas(
            self.screen,
            height=self.dot_image_height,
            width=self.dot_image_width,
            bg=self.BACKGROUND_COLOR,
            highlightthickness=0
        )
        canvas.place(
            relx=0.5,
            rely=0.5,
            anchor="center")
        canvas.create_image(
            self.dot_image_width // 2,
            self.dot_image_height // 2,
            image=self.dot_image,
            anchor="center"
        )

    def run(self):
        """Run the application."""

        self.initialize_window()
        self.load_dot_image()
        self.create_canvas()
        self.screen.mainloop()

if __name__ == "__main__":
    dot_image_path = r"dots/x12Dot_Tp_Y.png"
    app = AimDotApp(dot_image_path)
    app.run()