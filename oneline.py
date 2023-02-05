import PySimpleGUI

print(PySimpleGUI.Window('',[[PySimpleGUI.Input(), PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Cancel')]]).read())