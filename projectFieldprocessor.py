import tkinter as tk
from file_override import *
extension = ".arc_projectfield"




class Sender():
    def __init__(self, file):
        with open(file) as file:
            self.row_data = file.read()
            self.formed_data = self.form_data()
            self.directories, self.settings = self.gather_data()
            self.files = [File_override(directory) for directory in self.directories]
        
    
    def form_data(self):
        data = ""
        data_list = []
        for lexeme in self.row_data.split(" "):
            if lexeme not in (" ", "\n", ""):
                data += lexeme.rstrip()
        lexeme_list = [] 
        pos = [] #index of a lexeme in data(str)
        for i, char in enumerate(data):
            if char in ("{","}",";"):
                pos.append(i)
        if pos:
            for ind, i in enumerate(pos):   # ind -> next; j -> previous 
                if ind > 0 and ind < len(pos)-1:
                    j = pos[ind-1]
                    if i-j != 1:
                        lexeme = [data[j], data[j+1:i]]
                        if lexeme[1][0] not in ('"',"'") and lexeme[1][-1] not in ('"',"'"):
                            lexeme[1] = lexeme[1].replace("\n","")
                    else:
                        lexeme = [data[j]]
                    lexeme_list += lexeme
                if ind == 0:
                    lexeme = data[:i]
                    lexeme_list += lexeme
                if ind == len(pos)-1:
                    j = pos[ind-1]
                    lexeme = [data[j], data[j+1:i], data[i]]
                    if lexeme[1][0] not in ('"',"'") and lexeme[1][-1] not in ('"',"'"):
                        lexeme[1] = lexeme[1].replace("\n","")
                    lexeme_list += lexeme
            data_list += lexeme_list
            data_list = [i for i in data_list if i]
        else:
            data_list += data 

        return data_list
    
    

    def gather_data(self):
        scope = False
        indecator = False
        directories = []
        settings = []

        def gather_directories():
            for element in self.formed_data:
                if element == ";":
                    continue
                if element == "f":
                    scope = "f"
                elif element == "s":
                    scope = "s"
                elif element == "{" and scope == "f":
                    indecator = True
                elif element == "}" and scope == "f":
                    indecator = False
                else:
                    if scope == "f" and indecator and element:
                        directories.append(element[1:-1]) #["+1, "]
                    else:
                        continue
        
        gather_directories()
        return [directories, settings]