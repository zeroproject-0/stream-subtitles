from window import App
from tkinter import *
import sys
import os


def close():
  sys.exit()


def create_window():
  root = Tk()
  root.geometry('350x450')
  root.resizable(False, False)
  root.title('Stream Subtitles')
  icon = os.path.join(os.path.dirname(__file__), "static", "logo.")
  if os.name == 'nt':
    root.iconbitmap(icon + "ico")
  else:
    root.iconbitmap("@" + icon + "xbm")

  Grid.rowconfigure(root, 0, weight=1)
  Grid.columnconfigure(root, 0, weight=1)

  app = App(root)

  root.protocol("WM_DELETE_WINDOW", close)

  root.mainloop()


if __name__ == '__main__':
  create_window()
