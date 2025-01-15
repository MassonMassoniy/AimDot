#created by Masson Massoniy

from tkinter import Tk, Canvas

screen = Tk()
screen.title("Aim Dot")

screen.attributes("-fullscreen", True)
screen.attributes("-topmost", True)
screen.resizable(False, False)

screen.configure(bg= "#000000")
screen.wm_attributes("-transparentcolor", "#000000")

screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
dot_radius = screen_width * 0.001

dot = Canvas(screen, height= 20, width= 20, bg= "#FFFF00", highlightthickness=0)
dot.place(relx= 0.5, rely= 0.5, relheight= 0.002, relwidth= 0.001, anchor= "center")

screen.mainloop()