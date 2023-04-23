# import tkinter as tk
# import random
# import time

# FPS = 60
# GAME_DURATION = 60


# class AimTrainer(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("Aim Trainer")
#         self.geometry("500x500")

#         self.canvas = tk.Canvas(self, width=500, height=500)
#         self.canvas.pack()

#         self.decreasing = None
#         self.color_changes = {}
#         self.time_up_ending = ""
#         self.target = 0

#         self.score = tk.IntVar()
#         self.lives = 3

#         self.start_time = time.time()
#         self.elapsed_time = 0
#         self.color_change_time = 0.0833
#         self.target_hit_time = 2.5

#         self.start_label = tk.Label(self, text="Click to Start", font=("Helvetica", 36))
#         self.start_label.place(x=150, y=225)
#         self.start_label.bind("<Button-1>", self.start_game)

#         self.lives_label = tk.Label(self, text=f"Lives: {self.lives}")

#     class EndGame(BaseException):
#         pass

#     def end_game(self, reason):
#         for widget in self.winfo_children():
#             widget.destroy()

#         new_canvas = tk.Canvas(self, width=500, height=500)
#         new_canvas.pack()
#         new_canvas.create_text(250, 250, text="Game Over", font=("Helvetica", 36))
#         new_canvas.create_text(250, 290, text=reason)
#         new_canvas.create_text(250, 330, text=f"Final Score: {self.score.get()}")
#         raise self.EndGame(f"Game Over: {reason}")

#     def decrease_target_size(self):
# current_size = (
#     self.canvas.coords(self.target)[2] - self.canvas.coords(self.target)[0]
# )
# starting_size = 50
# desired_size = 20
# shrink_amount = starting_size - desired_size
# delay = int(1 / FPS * 1000)
# num_frames = (self.target_hit_time * FPS) + (shrink_amount * delay)
# decrease_rate = shrink_amount / num_frames
# if current_size > desired_size:
#     x1, y1, x2, y2 = self.canvas.coords(self.target)
#     x1 += decrease_rate
#     y1 += decrease_rate
#     x2 -= decrease_rate
#     y2 -= decrease_rate

#     self.canvas.coords(self.target, x1, y1, x2, y2)
#     self.canvas.update()
#     self.decreasing = self.canvas.after(delay, self.decrease_target_size)
#     def decrease_target_size(self, last_time=None):
#         if last_time is None:
#             last_time = 0

#         current_size = (
#             self.canvas.coords(self.target)[2] - self.canvas.coords(self.target)[0]
#         )
#         starting_size = 50
#         desired_size = 20
#         shrink_amount = starting_size - desired_size

#         elapsed_time = time.time() - last_time
#         decrease_rate = shrink_amount / (self.target_hit_time * FPS)
#         delay = int(1 / FPS * 1000 / shrink_amount)

#         if current_size > desired_size:
#             x1, y1, x2, y2 = self.canvas.coords(self.target)
#             x1 += decrease_rate * elapsed_time
#             y1 += decrease_rate * elapsed_time
#             x2 -= decrease_rate * elapsed_time
#             y2 -= decrease_rate * elapsed_time

#             self.canvas.coords(self.target, x1, y1, x2, y2)
#             self.canvas.update()
#             self.decreasing = self.canvas.after(
#                 delay, self.decrease_target_size, time.time()
#             )

#     def set_time_out_color_change(self):
#         try:
#             self.time_up_ending = self.canvas.after(
#                 int(self.target_hit_time * 1000),
#                 lambda: self.end_game("You took too long to hit the target!"),
#             )
#         except self.EndGame:
#             return
#         self.color_changes["orange"] = self.canvas.after(
#             int(self.color_change_time * 1000),
#             lambda: self.canvas.itemconfig(self.target, fill="orange"),
#         )
#         self.color_changes["red"] = self.canvas.after(
#             int(self.color_change_time * 1000 * 2),
#             lambda: self.canvas.itemconfig(self.target, fill="red"),
#         )

#     def on_click(self, event):
#         def reset_target():
#             self.canvas.coords(
#                 self.target,
#                 x := random.randint(75, 425),
#                 y := random.randint(75, 425),
#                 x + 50,
#                 y + 50,
#             )
#             self.canvas.itemconfig(self.target, fill="yellow")
#             self.elapsed_time = self.start_time - time.time()
#             value_time_table = {
#                 self.elapsed_time <= 10: (2.5, 0.833),
#                 self.elapsed_time > 10 <= 40: (1.75, 0.583),
#                 self.elapsed_time > 40 <= 50: (1.25, 0.416),
#                 self.elapsed_time > 50: (1, 0.333),
#             }[True]
#             self.target_hit_time, self.color_change_time = value_time_table
#             self.decrease_target_size()
#             self.canvas.after_cancel(self.time_up_ending)
#             self.canvas.after_cancel(self.color_changes["orange"])
#             self.canvas.after_cancel(self.color_changes["red"])
#             self.set_time_out_color_change()

#         overlapping_items = self.canvas.find_overlapping(
#             event.x, event.y, event.x, event.y
#         )
#         if self.target in overlapping_items:
#             self.canvas.unbind("<Button-1>")
#             self.score.set(self.score.get() + 1)
#             self.canvas.itemconfig(self.target, fill="green")
#             self.canvas.after(200, reset_target)
#             self.canvas.bind("<Button-1>", self.on_click)
#         else:
#             self.lives -= 1
#             if self.lives == 0:
#                 try:
#                     self.end_game("You ran out of lives!")
#                 except self.EndGame:
#                     return
#             self.lives_label.config(text=f"Lives: {self.lives}")

#     def start_game(self, _):
#         self.target = self.canvas.create_oval(
#             x := random.randint(75, 425),
#             y := random.randint(75, 425),
#             x + 50,
#             y + 50,
#             fill="yellow",
#         )
#         self.start_label.destroy()
#         self.decrease_target_size()
#         self.set_time_out_color_change()
#         self.canvas.bind("<Button-1>", self.on_click)

#         self.lives_label.place(x=420, y=0)
#         self.canvas.after(GAME_DURATION * 1000, lambda: self.end_game("Time is up!"))


# def run_game():
#     root = AimTrainer()
#     root.mainloop()
#     # while True:
#     #     start_time = time.time()
#     #     root.mainloop()
#     #     elapsed_time = time.time() - start_time
#     #     sleep_time = 1 / FPS - elapsed_time
#     #     if sleep_time > 0:
#     #         time.sleep(sleep_time)


# if __name__ == "__main__":
#     run_game()
import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
target_hit_time = 2.1
target = canvas.create_oval(100, 100, 150, 150)
FPS = 60


def decrease_target_size():
    current_size = canvas.coords(target)[2] - canvas.coords(target)[0]
    starting_size = 50
    desired_size = 20
    shrink_amount = starting_size - desired_size
    num_frames = target_hit_time * FPS
    decrease_rate = shrink_amount / num_frames
    delay = int(target_hit_time / decrease_rate * 1000)
    if current_size > desired_size:
        x1, y1, x2, y2 = canvas.coords(target)
        x1 += decrease_rate
        y1 += decrease_rate
        x2 -= decrease_rate
        y2 -= decrease_rate

        canvas.coords(target, x1, y1, x2, y2)
        canvas.update()
        canvas.after(delay, decrease_target_size)
    else:
        print(time.time() - start)


start = time.time()
decrease_target_size()
root.mainloop()
