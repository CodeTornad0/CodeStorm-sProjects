import tkinter as tk


def change_color(event):
    color = f"#{red.get():02x}{green.get():02x}{blue.get():02x}"
    color_sphere.itemconfig(color_sphere_id, fill=color)
    return event


root = tk.Tk()
root.geometry("300x300")
root.title("Color Selector")

red = tk.IntVar()
green = tk.IntVar()
blue = tk.IntVar()

red_scale = tk.Scale(
    root, from_=0, to=255, variable=red, orient=tk.HORIZONTAL, command=change_color
)
red_scale.pack()

green_scale = tk.Scale(
    root, from_=0, to=255, variable=green, orient=tk.HORIZONTAL, command=change_color
)
green_scale.pack()

blue_scale = tk.Scale(
    root, from_=0, to=255, variable=blue, orient=tk.HORIZONTAL, command=change_color
)
blue_scale.pack()

color_sphere = tk.Canvas(root, width=150, height=150)
color_sphere_id = color_sphere.create_oval(20, 20, 130, 130, fill="black")
color_sphere.pack(pady=15)

root.mainloop()
