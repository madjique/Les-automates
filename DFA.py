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
            self.etat =self.transition_function[(self.etat,inp)][0]
            return
        self.etat = None
        return
    
    def in_accept_state(self):
        return self.etat in self.etatsFinals
    
    def go_to_initial_state(self):
        self.etat = self.etatInit.pop()
        self.etatInit.add(self.etat)
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
        self.etat = self.etatInit.pop()
        self.etatInit.add(self.etat)
        accessiblenonverif.append(self.etat)
        accessible = []
        for st in accessiblenonverif :
            accessible.append(st)
            for x in self.alphabet :
                if (st,x) in self.transition_function.keys() :
                    suiv = self.transition_function[(st, x)][0]
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
                        suiv = self.transition_function[(st,x)][0]
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
                if st in self.etatsFinals :
                    self.etatsFinals.remove(st)
                for x in self.alphabet :
                    if (st,x) in self.transition_function.keys() :
                        del self.transition_function[(st,x)]
        pass

    def miroir(self):
        newInstru = {}
        for st in self.etats :
            for x in self.alphabet :
                if (st,x) in self.transition_function.keys() :
                    elt = self.transition_function[(st,x)][0]
                    if (elt,x) in newInstru.keys():
                        newInstru[(elt,x)].append(st)
                    else :
                        newInstru[(elt,x)] = [st]
        self.transition_function.clear()
        for x in newInstru.keys():
            self.transition_function[x] = newInstru[x]
        #modif des etat finaux et initiaux 
        for x in self.etatInit:
            self.etatsFinals.add(x)
        for x in self.etatsFinals :
            self.etatInit.add(x)
        pass
    def Complement(self) :
        #ajouter letat  c
        self.etats.add('c')
        # rajouter les instruction restant pour chanque etat a c  
        for st in self.etats :
            for x in self.alphabet :
                if (st,x) not in self.transition_function.keys() :
                    self.transition_function[(st,x)]=['c']
        #rendre les etat finaux normaux et etat normaux finaux
        shadow = self.etatsFinals.copy()
        self.etatsFinals.clear()
        for  st in self.etats :
            if st not in shadow :
                self.etatsFinals.add(st)
        pass

#__main__
if __name__ == "__main__":    
#initialisation des etats et de l'alphabet

    etats = {'q0','q1','q2','q3','q4'}
    alphabet = {'a','b'}
    etatInitiale = {'q0'}
    etatFinale = {'q0','q2','q3'}

    #parametrage des instructions
    #dictionnary
    Instructions = {
        ('q0','a') : ['q0'] ,
        ('q0','b') : ['q1'] ,
        ('q1','a') : ['q2'] ,
        ('q1','b') : ['q0'] ,
        ('q2','a') : ['q2'] ,
        ('q3','a') : ['q3'] ,
        ('q3','b') : ['q4']
    }

    

    #execution de l'automate 

    execution = AutomateEtatFini(etats, alphabet, Instructions, etatInitiale, etatFinale)

    #la lecture en entrée
    inp_program = tuple('aba')
    print("Reconnaisance du mot ... ")
    #affichage de l'execution
    print("Mot reconnu : ")
    print(execution.run_with_input_list(inp_program))

    #transformation en automate reduit

    execution.Reduction()
    print("Trace après Reduction")
    print(etats)
    print(Instructions)
    print(etatFinale)

    #transformation miroir
    execution.miroir()
    print("Trace apres Miroir")
    print(etats)
    print(Instructions)
    print(etatFinale)

    #complement 

    execution.Complement()
    print("Trace aprs complement")
    print(etats)
    print(Instructions)
    print(etatFinale)

pass