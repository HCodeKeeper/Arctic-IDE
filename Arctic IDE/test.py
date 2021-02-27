from arctic_ideWIN import * #intended to be placed in package

def _generateTabs(n_ext=1):
    #n_ext - number of tabs to be added to default one
    if n_ext >= 1:
        for n in range(n_ext):
            program.CreateTab()


program = GUI()
_generateTabs(10)
program.mainloop()