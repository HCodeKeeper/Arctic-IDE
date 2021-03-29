import subprocess
extensions = {
    "Python2.x" : "python2",
    "Python3.x" : "python3",
    "Python3.6" : "python3.6",
    "Python3.9" : "python3.9",
    "Python" : "python"
}


def compile(file=None, language=""):
    if not language:
        return os.popen("echo Your file hasn't any file extension, so you can't run the program")
    elif file == None:
        return os.popen("echo Your file hasn't been saved yet, so it doesn't exist")
    else:
        if "Python" in language:
            return python_compile(file, extensions[language])


def python_compile(file, interpretator):
    command = f"{interpretator} {file}"
    proc = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8")
    output = f"{proc.stdout}\n{proc.stderr}"
    return output