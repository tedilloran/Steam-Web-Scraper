from tkinter import ttk, BOTH


class DataView(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.treeView = ttk.Treeview(parent, columns=(
            "Release Date", "Developer", "Publisher", "URL"))

        self.treeView.column("#0", width=100)
        self.treeView.column("Release Date", width=100)
        self.treeView.column("Developer", width=100)
        self.treeView.column("Publisher", width=100)
        self.treeView.column("URL", width=100)

        self.treeView.heading("#0", text="Title")
        self.treeView.heading("Release Date", text="Release Date")
        self.treeView.heading("Developer", text="Developer")
        self.treeView.heading("Publisher", text="Publisher")
        self.treeView.heading("URL", text="URL")

        self.treeView.pack(expand=True, fill=BOTH, padx=10, pady=10)
