from tkinter import *
from tkinter import ttk
import pandastable as pt

import SteamQuery 

class SteamWebScraper(ttk.Frame):
  def __init__(self):
    self.root = Tk()
    self.root.geometry(self.getCenterPosition(570, 270))
    self.root.title("Steam Web Scraper")
    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)
    ttk.Frame.__init__(self, self.root)
    self.createWidgets()

  def getCenterPosition(self, windowWidth, windowHeight):
    screen_center_x = int(self.root.winfo_screenwidth()/2 - (windowWidth/2))
    screen_center_y = int(self.root.winfo_screenheight()/2 - (windowHeight/2))
    return "{}x{}+{}+{}".format(windowWidth, windowHeight, screen_center_x, screen_center_y)

  def createWidgets(self):
    self.grid()

    currOption = StringVar()
    self.options = ttk.OptionMenu(self, currOption, *("Developer", "Publisher"))
    self.options.grid(row=0, column=0)

    inputString = StringVar()
    self.entry = ttk.Entry(self, textvariable=inputString)
    self.entry.grid(row=0, column=1)

    self.submit = ttk.Button(self, text="Submit", command=lambda: self.search(currOption.get(), inputString.get()))
    self.submit.grid(row=0, column=2)


  def search(self, option, input):
    if option == "Developer":
      data = SteamQuery.queryByDeveloper(input)
      self.showTable(data, "{} - {}".format(option, input))
    elif option == "Publisher":
      data = SteamQuery.queryByPublisher(input)
      self.showTable(data, "{} - {}".format(option, input))

  def showTable(self, data, input):
    tableWindow = Toplevel(self)
    tableWindow.geometry(self.getCenterPosition(500, 500))
    tableWindow.wm_title(input)
    resultsTable = pt.Table(tableWindow, dataframe=data, showtoolbar=True, showstatusbar=True)
    resultsTable.show()

  def start(self):
    self.root.mainloop()

SteamWebScraper().start()