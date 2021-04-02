from tkinter import filedialog
from typing import Annotated

class File():
    default_ext = ".py"
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
        if _file is object:
            _file.write(textSrc)
            _file.close()


    def open(worker): #worker - GUI
        _files = filedialog.askopenfiles()
        if _files:
            for _file in _files:
                tab = worker.CreateTab(_file.name)
                tab.UpdateFileObj(_file)
                tab.textField.insert(_file.read())
                _file.close()
            return True
        else:
            return False

