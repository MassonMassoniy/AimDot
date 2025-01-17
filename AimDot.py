#created by Masson Massoniy

from tkinter import Tk, Canvas, PhotoImage

screen = Tk()
screen.title("Aim Dot")

screen.attributes("-fullscreen", True)
screen.attributes("-topmost", True)
screen.resizable(False, False)

screen.configure(bg= "#000001")
screen.wm_attributes("-transparentcolor", "#000001")

screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
dot_radius = screen_width * 0.001

dot_image = PhotoImage(file= "dots/x12Dot_Tp_Y.png")

canvas = Canvas(screen, height= dot_image.height(), width= dot_image.width(), bg= "#000001", highlightthickness=0)
canvas.place(relx= 0.5, rely= 0.5, anchor= "center")

canvas.create_image(dot_image.width() / 2, dot_image.height() / 2, image= dot_image, anchor= "center")

screen.mainloop()