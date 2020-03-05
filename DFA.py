# -*- coding: utf-8 -*-

class AutomateEtatFini:
    etat = None
    def __init__(self, etats, alphabet, transition_function, etatInit, etatsFinals):
        self.etats = etats
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.etatInit = etatInit
        self.etatsFinals = etatsFinals
        self.etat = etatInit
        return
    
    def transition_to_state_with_input(self, inp):
        if (self.etat,inp)  in self.transition_function.keys() :
            self.etat = self.transition_function[(self.etat,inp)]
            return
        self.etat = None
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
    pass

    def Reduction(self):
        #on cherche les etat  accessible
        accessiblenonverif =[]
        accessiblenonverif.append(self.etatInit)
        accessible = []
        for st in accessiblenonverif :
            accessible.append(st)
            for x in self.alphabet :
                if (st,x) in self.transition_function.keys() :
                    suiv = self.transition_function[(st, x)]
                    if suiv not in accessible :
                        accessiblenonverif.append(suiv)
        #fonction verif coacess
        def verifCoAcess(st) :
            if st in self.etatsFinals :
                return True
            else :
                lastv = False
                for x in self.alphabet :
                    if (st,x) in self.transition_function.keys()  :
                        suiv = self.transition_function[(st,x)]
                        if (st != suiv ) :
                            v = verifCoAcess(suiv)
                        else : 
                            v= False
                    else :
                        v = False
                    lastv=lastv or v
                return lastv
            
        #on cherche les etat non co-accessible
        coacces= []
        for x in self.etats :
            if verifCoAcess(x)  :
                coacces.append(x)
        #on supprime les non accessible et non coaccessible
        transitionEtat = self.etats.copy()
        for st in transitionEtat:
            if st not in accessible or st  not in coacces:
                self.etats.remove(st)
                for x in self.alphabet :
                    if (st,x) in self.transition_function.keys() :
                        del self.transition_function[(st,x)]
        pass

    def miroir(self, parameter_list):
      
        pass


#initialisation des etats et de l'alphabet

etats = {'q0','q1','q2','q3','q4'}
alphabet = {'a','b'}
etatInitiale = 'q0'
etatFinale = {'q0','q2'}

#parametrage des instructions

Instructions = {}
Instructions[('q0','a')] = 'q0'
Instructions[('q0','b')] = 'q1'
Instructions[('q1','a')] = 'q2'
Instructions[('q1','b')] = 'q0'
Instructions[('q2','a')] = 'q2'
Instructions[('q3','a')] = 'q3'
Instructions[('q3','b')] = 'q4'

#execution de l'automate 

execution = AutomateEtatFini(etats, alphabet, Instructions, etatInitiale, etatFinale)

#la lecture en entrée
inp_program = tuple('aba')

#affichage de l'execution

#print(execution.run_with_input_list(inp_program))

#transformation en automate reduit

execution.Reduction()
print(etats)
print(Instructions)

#transformation miroir