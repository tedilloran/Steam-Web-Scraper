from tkinter import ttk, StringVar, messagebox, LEFT, X

from .SteamQuery import queryByDeveloper, queryByPublisher


class SearchRow(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        currOption = StringVar()
        self.options = ttk.OptionMenu(
            self.parent, currOption, *("Developer", "Publisher"))
        self.options.pack(side=LEFT, padx=10)

        inputString = StringVar()
        self.entry = ttk.Entry(self.parent, textvariable=inputString)
        self.entry.pack(side=LEFT, expand=True, fill=X)

        self.submit = ttk.Button(self.parent, text="Submit", command=lambda: self.search(
            currOption.get(), inputString.get()))
        self.submit.pack(side=LEFT, padx=10)

    def search(self, option, input):
        if option == "Developer":
            data = queryByDeveloper(input)
            if data == None:
                print("Not found")
                messagebox.showwarning("{} Not Found".format(
                    option), "{} - {} not found".format(option, input))
                return
            for el in data:
                print(el)
        elif option == "Publisher":
            data = queryByPublisher(input)
            if data == None:
                print("Not found")
                messagebox.showwarning("{} Not Found".format(
                    option), "{} - {} not found".format(option, input))
                return
            for el in data:
                print(el)
