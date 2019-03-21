from tkinter import ttk, Text, BOTH


class TextView(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        self.textView = Text(parent)
        self.textView.pack(expand=True, fill=BOTH, padx=10, pady=10)
