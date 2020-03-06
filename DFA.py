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
        return self.etat in self.etatsFinals
    
    def go_to_initial_state(self):
        self.etat = self.etatInit
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()
  
    
    def nfa_to_dfa(self):
        ## rendre l'automate simple
        dfa=dict()
        dfa_list=[]              
        dfa_list.append(self.etatInit)
        for etat_prec in dfa_list:
            for alpha in alphabet:
                    nvl_etat=[]
                    if isinstance(etat_prec,str):
                        etat_prec=[etat_prec]
                    for i in etat_prec:
                        print(i)
                        nvl_etat.append(self.transition_function[(i,alpha)])                  
                    liist=[]
                    for j in nvl_etat:
                        if isinstance(j,list):
                            for k in j:
                                liist.append(k)
                        else :
                            liist.append(j)
                    dfa[(etat_prec,alpha)]=liist
                    nvl_etat=set(nvl_etat)
                    if nvl_etat not in dfa_list:
                        dfa_list.append(nvl_etat)
        
        
        print(dfa)
        pass                                       
                                              
    #def Reduction(self):
        #on cherche les etat non accessible
        #on supprime
        #on cherche les etat non co-accessible
        #on supprime




#initialisation des etats et de l'alphabet

etats = {'q0','q1','q2'}
alphabet = {'a','b'}
etatInitiale = 'q0'
etatFinale = 'q2'

#parametrage des instructions

Instructions = dict()
Instructions[('q0','a')] = ['q1','q2']
Instructions[('q1','b')] = 'q2'

 
#execution de l'automate 

execution = AutomateEtatFini(etats, alphabet, Instructions, etatInitiale, etatFinale)

execution.nfa_to_dfa()

#la lecture en entrée

#inp_program = list('ababbbbbbb')

#affichage de l'execution

#print (execution.run_with_input_list(inp_program))


#transformation en automate reduit
