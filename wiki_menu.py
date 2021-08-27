from tkinter import *
from tkinter.messagebox import *
import sys


class WikiSearch():
    def OpenSearchBox(root):
        #here for wiki search
        import wiki


def main(root, text, menubar):

    WikiSearchVar = WikiSearch()

    wiki_menu = Menu(menubar)
    wiki_menu.add_command(label="Open Wiki Search", command=WikiSearchVar.OpenSearchBox)
    menubar.add_cascade(label="Options", menu=wiki_menu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
