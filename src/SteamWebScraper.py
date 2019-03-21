from tkinter import Tk, ttk, StringVar, Toplevel, messagebox, X, BOTH
import pandastable as pt

from components.SearchRow import SearchRow
from components.DataView import DataView


class SteamWebScraper(ttk.Frame):
    def __init__(self):
        self.root = Tk()
        ttk.Frame.__init__(self, self.root)

        self.searchRow = ttk.Frame(self.root, height=60)
        self.searchRow.pack(fill=X, ipady=5)

        self.lower = ttk.Frame(self.root)
        self.lower.pack(expand=True, fill=BOTH)

        self.root.geometry(self.getCenterPosition(600, 500))
        self.root.title("Steam Web Scraper")
        self.createWidgets()

    def getCenterPosition(self, windowWidth, windowHeight):
        screen_center_x = int(
            self.root.winfo_screenwidth()/2 - (windowWidth/2))
        screen_center_y = int(
            self.root.winfo_screenheight()/2 - (windowHeight/2))
        return "{}x{}+{}+{}".format(windowWidth, windowHeight, screen_center_x, screen_center_y)

    def createWidgets(self):
        SearchRow(self.searchRow)
        DataView(self.lower)

    def start(self):
        self.root.mainloop()


SteamWebScraper().start()
