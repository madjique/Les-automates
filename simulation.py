from PySimpleAutomata import NFA, automata_IO

nfa_example = automata_IO.nfa_dot_importer('Input.dot')

automata_IO.nfa_to_dot(nfa_example, 'Input', '.')

import webbrowser
import os
new = 2
url = 'file://' + os.path.realpath("input.dot.svg")
webbrowser.open(url,new=new)