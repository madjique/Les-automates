# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:30:41 2020

@author: Snow
"""

class AutomateEtatFini:
    Etat = None
    def __init__(self, etats, alphabet, transition_function, etatInit, etatsFinals):
        self.etats = etats
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.etatInit = etatInit
        self.etatsFinals = etatsFinals
        self.Etat = etatInit
        return
    
    def transition_to_state_with_input(self, input_value):
        if ((self.etat, input_value) not in self.transition_function.keys()):
            self.etat = None
            return
        self.etat = self.transition_function[(self.etat, input_value)]
        return
    
    def in_accept_state(self):
        return self.etat in etatsFinals
    
    def go_to_initial_state(self):
        self.etat = self.etatInit
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()
    pass

    #def Reduction(self):
        #on cherche les etat non accessible
        #on supprime
        #on cherche les etat non co-accessible
        #on supprime




#initialisation des etats et de l'alphabet

etats = {'q0','q1','q2','q3','q4'}
alphabet = {'a','b'}
etatInitiale = 'q0'
etatFinale = {'q3'}

#parametrage des instructions

Instructions = dict()
Instructions[('q0','a')] = ['q1','q3']
Instructions[('q1','b')] = 'q2'
Instructions[('q2','a')] = 'q3'
Instructions[('q3','b')] = 'q3'
 
#execution de l'automate 

execution = AutomateEtatFini(etats, alphabet, Instructions, etatInitiale, etatFinale)

#la lecture en entrée

inp_program = list('ababbbbbbb')

#affichage de l'execution

print (execution.run_with_input_list(inp_program))


#transformation en automate reduit
