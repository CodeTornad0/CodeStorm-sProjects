import tkinter as tk
from tkinter import messagebox
import traceback
import sys


class TextEditor(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.undo_stack = []
        self.redo_stack = []

        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Text Editor")

        self.text = tk.Text(self)
        self.text.pack(fill="both", expand=True)

        undo_button = tk.Button(self, text="Undo", command=self.undo)
        undo_button.pack(side="left")

        redo_button = tk.Button(self, text="Redo", command=self.redo)
        redo_button.pack(side="left")

        run_button = tk.Button(
            self,
            text="Run Code",
            command=lambda: self.run_code(self.text.get("0.0", "end")),
        )
        run_button.pack(side="left")

        self.text.bind("<Key>", self.update_stacks)
        self.text.bind("<ButtonRelease-1>", self.update_stacks)

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.undo_stack.pop())
            text = self.text.get("1.0", "end")
            self.text.delete("1.0", "end")
            self.text.insert("1.0", text.split()[0 : len(text.split()) - 1])

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.redo_stack.pop())
            redo = self.undo_stack[-1]
            text = self.text.get("1.0", "end")
            self.text.delete("1.0", "end")
            self.text.insert("end", f"{text.strip()} {redo}")

    def update_stacks(self, event):
        state = self.text.get("1.0", "end")
        self.undo_stack.clear()
        for item in state.split():
            self.undo_stack.append(item)
        self.redo_stack.clear()
        return event

    def run_code(self, code):
        try:
            exec(code)
        except Exception as error:
            tb = traceback.extract_tb(sys.exc_info()[2])
            if tb:
                line_number = tb[-1].lineno
                error_message = f"Line {line_number}: {error}"
            else:
                error_message = str(error)
            messagebox.showerror("Error", error_message)


editor = TextEditor()
editor.mainloop()
