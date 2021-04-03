from tkinter import filedialog
import tkinter as tk
from typing import Annotated
import os
from projectFieldprocessor import *

class File():
    default_ext = ".arc"
    filetypes = [
        ("All files", ".*"),
        ("Python", ".py"),
        ("C", ".c"),
        ("C++", ".cpp"),
        ("C#", ".cs"),
        ("Java", ".java"),
        ("Javascript", ".js"),
        ("Arctic", ".arc")
    ]
    initialdir = ""

    def save_as(textSrc="", default_ext=default_ext, filetypes=filetypes, initialdir=initialdir): #TO BE CALLED IN GUI.tab.UpdateFileObj -> method()
        _file = filedialog.asksaveasfile(
            initialdir=initialdir,
            defaultextension=default_ext,
            filetypes=filetypes
        )
        if _file != None:
            _file.write(textSrc)
            _file.close()
        return _file


    def save(textSrc="", _file=False): #_file = GUI.tab.fileObj, textSrc --> GUI.tab.TextField.content
        if _file:
            with open(_file.name, 'w') as _file:
                _file.write(textSrc)


    def open(worker): #worker - GUI
        _files = filedialog.askopenfiles()
        if _files:
            for _file in _files:
                tab = worker.CreateTab(os.path.basename(_file.name))
                tab.UpdateFileObj(_file)
                tab.textField.insert(tk.INSERT, _file.read())
                _file.close()
            return True
        else:
            return False
    

    def open_a_project(worker): #worker - GUI
        _file = filedialog.askopenfile()
        if os.path.splitext(_file.name)[1] == extension:
            files = Sender(_file.name).files
            if files:
                for file in files:
                    if file.name:
                            tab = worker.CreateTab(os.path.basename(file.name))
                            tab.UpdateFileObj(file)
                            tab.textField.insert(tk.INSERT, file.read())
                    else:
                        return 1

                return True
        return 2

