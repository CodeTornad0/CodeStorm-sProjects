import tkinter as tk
from tkinter import messagebox
from playsound import playsound


class HabitTracker(tk.Tk):
    def __init__(self, habits=None):
        tk.Tk.__init__(self)

        self.habits = habits
        if self.habits is None:
            self.habits = {}
        self.title("Habit Tracker")

        self.habit_list = tk.Listbox(self)
        for habit in self.habits:
            self.habit_list.insert(tk.END, habit)
        self.habit_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.habit_list.bind("<<ListboxSelect>>", self.show_details)

        habit_frame = tk.Frame(self)
        habit_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        habit_label = tk.Label(habit_frame, text="Habit:")
        habit_label.pack(side=tk.TOP, anchor=tk.W)
        self.habit_name = tk.StringVar()
        habit_entry = tk.Entry(habit_frame, textvariable=self.habit_name)
        habit_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        frequency_label = tk.Label(habit_frame, text="Frequency:")
        frequency_label.pack(side=tk.TOP, anchor=tk.W)
        self.habit_frequency = tk.StringVar()
        frequency_entry = tk.Entry(habit_frame, textvariable=self.habit_frequency)
        frequency_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        progress_label = tk.Label(habit_frame, text="Progress:")
        progress_label.pack(side=tk.TOP, anchor=tk.W)
        self.habit_progress = tk.StringVar()
        progress_entry = tk.Entry(habit_frame, textvariable=self.habit_progress)
        progress_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        notes_label = tk.Label(habit_frame, text="Notes:")
        notes_label.pack(side=tk.TOP, anchor=tk.W)
        self.habit_notes = tk.StringVar()
        notes_entry = tk.Entry(habit_frame, textvariable=self.habit_notes)
        notes_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        add_button = tk.Button(habit_frame, text="Add Habit", command=self.add_habit)
        add_button.pack(side=tk.TOP, pady=10)
        update_button = tk.Button(
            habit_frame, text="Update Habit", command=self.update_habit
        )
        update_button.pack()

        self.completed_button = tk.Button(
            habit_frame,
            text="Mark as Completed",
            command=self.mark_completed,
        )
        self.completed_button.pack(side=tk.BOTTOM, pady=10)

    def show_details(self, event):
        try:
            habit = self.habit_list.get(self.habit_list.curselection())
            habit_details = self.habits.get(habit, {})
            self.habit_name.set(habit)
            self.habit_frequency.set(habit_details.get("frequency", ""))
            self.habit_progress.set(habit_details.get("progress", ""))
            self.habit_notes.set(habit_details.get("notes", ""))
            return event
        except tk.TclError:
            return event

    def add_habit(self):
        habit = self.habit_name.get()
        frequency = self.habit_frequency.get()
        progress = self.habit_progress.get()
        notes = self.habit_notes.get()
        if habit == "" or frequency == "" or progress == "":
            messagebox.showerror(
                "Error", "Habit, frequency, and progress are required fields."
            )
            return
        if habit in self.habits:
            messagebox.showerror("Error", "Habit already exists.")
            return
        self.habits[habit] = {
            "frequency": frequency,
            "progress": progress,
            "notes": notes,
        }
        self.habit_list.insert(tk.END, habit)

    def update_habit(self):
        try:
            habit = self.habit_list.get(self.habit_list.curselection())
            habit_name = self.habit_name.get()
            frequency = self.habit_frequency.get()
            progress = self.habit_progress.get()
            notes = self.habit_notes.get()
            if habit_name == "" and frequency == "" and progress == "" and notes == "":
                self.habits.pop(habit)
                self.habit_list.delete(0, "end")
                for habit in self.habits:
                    self.habit_list.insert(tk.END, habit)
                return
            if habit_name == "" or frequency == "" or progress == "":
                messagebox.showerror(
                    "Error", "Habit, frequency, and progress are required fields."
                )
                return
            lst = list(self.habits.items())
            index = [i for i, (key, value) in enumerate(lst) if key == habit][0]
            self.habits.pop(habit)
            self.habits[habit_name] = {
                "frequency": frequency,
                "progress": progress,
                "notes": notes,
            }
            list_dictionary = list(self.habits.items())
            list_dictionary.insert(index, list_dictionary[-1])
            self.habits = dict(list_dictionary)
            self.habit_list.delete(0, "end")
            for habit in self.habits:
                self.habit_list.insert(tk.END, habit)
        except tk.TclError:
            return

    def mark_completed(self):
        try:
            habit = self.habit_list.get(self.habit_list.curselection())
            self.habits[habit]["progress"] = "COMPLETED"
            playsound("item_completed.mp3")
        except tk.TclError:
            return


tracker = HabitTracker()
tracker.mainloop()
