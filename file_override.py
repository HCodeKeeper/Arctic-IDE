class File_override():
    def __init__(self, directory):
        self.name = directory
    

    def read(self):
        try:
            with open(self.name) as file:
                return file.read()
        except:
            return "empty file"