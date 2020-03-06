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
                                                                     
    #def Reduction(self):
        #on cherche les etat non accessible
        #on supprime

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
    def nfa_to_dfa(self,dfa,etatFinal):
        ## rendre l'automate simple 
        dfa_list=[]   
        dfa_list.append(self.etatInit)
        for etat_prec in dfa_list:
            for alpha in self.alphabet:
                    nvl_etat=[]
                    for i in etat_prec:
                        if (i,alpha) in self.transition_function:
                            nvl_etat.append(self.transition_function[(i,alpha)])                  
                    liist=[]
                    if len(nvl_etat)!=0:
                        for j in nvl_etat:
                            if isinstance(j,list):
                                for k in j:
                                    liist.append(k)
                            else :
                                liist.append(j)
                        for m in set(liist):
                            if m in self.etatsFinals:
                                etatFinal.add("".join(set(liist)))
                                break
                        dfa["".join(etat_prec),alpha]="".join(set(liist))
                        liist=set(liist)
                        if liist not in dfa_list:
                            dfa_list.append(liist)
        
        pass    
    def automate_simple(self):
        for i,j in self.transition_function.items():
            if i[1]=='$':
                j
                
            
              


#__main__
if __name__ == "__main__":    
#initialisation des etats et de l'alphabet

    etats = {'q0','q1','q2'}
    alphabet = {'0','1'}
    etatInitiale = {'q0'}
    etatFinale = {'q2'}

    #parametrage des instructions
    #dictionnary
    Instructions = {
        ('q0','1') : ['q1','q2'] ,
        ('q1','0') : ['q1'] ,
        ('q1','1') : ['q2'],
        ('q2','0') : 'q0'
        
    }
    execution = AutomateEtatFini(etats, alphabet, Instructions, etatInitiale, etatFinale)
    Etatf=set()
    dfa=dict()
    execution.nfa_to_dfa(dfa,Etatf)
    for x, y in dfa.items():
        print(x,'----->', y)
    print("Les etats finaux :",Etatf) 
    print("l'etat initial : ", execution.etatInit)
    
    #execution de l'automate 
#la lecture en entrée

#inp_program = list('ababbbbbbb')

   

    #la lecture en entrée
    """ inp_program = tuple('aba')
    print("Reconnaisance du mot ... ")
    #affichage de l'execution
    print("Mot reconnu : ")
    print(execution.run_with_input_list(inp_program))


    #transformation en automate reduit


    #print (execution.run_with_input_list(inp_program))
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
    print(etatFinale)"""

pass