# -*- coding: utf-8 -*-
import os
import time
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
        #self.etat = None
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
        return self.etat in self.etatsFinals
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
    
    def nfa_to_dfa(self) :
        ## rendre l'automate simple
        dfa=dict()
        dfa_list=[] 
        etatFinal=set()          
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
                        dfa["".join(etat_prec),alpha]=["".join(set(liist))]
                        liist=set(liist)
                        if liist not in dfa_list:
                            dfa_list.append(liist)  
        self.etatsFinals.clear()   
        self.transition_function.clear()        
        self.transition_function.update(dfa)
        for i in etatFinal :
            self.etatsFinals.add(i)
        pass    
    def automate_simple(self):
        simple=dict()
        l=set()
        for i,j in self.transition_function.items():
            if i[1]=='$':
                l.add(i[0])
                for x in j:
                    for alpha in self.alphabet:
                        if (x,alpha) in self.transition_function:    
                            simple[(i[0],alpha)]=self.transition_function[(x,alpha)]
        for i in l:
            self.etatsFinals.add(i)
            self.transition_function.pop((i,'$'))
        self.transition_function.update(simple)
        pass
                
            

def  afficher(etats,etatInitiale,etatFinale,Instructions) :
    time.sleep(3)
    f = open("input.dot","w")
    #generation du text 
    DotTextToFile =" digraph { \n"
    DotTextToFile += "fake [style=invisible]\nfake -> s0 [style=bold]\n"
    #ecriture des etats
    for x in etats :
        DotTextToFile += x 
        if x in etatFinale and x in etatInitiale :
            DotTextToFile += " [root=true , shape=doublecircle]"
        else :
            if x in etatInitiale :
                DotTextToFile += " [root=true]"
            if x in etatFinale :
                DotTextToFile += " [shape=doublecircle]"
        DotTextToFile+="\n"
    #ecriture  des transition
    for x in Instructions.keys() :
        for i in Instructions[x] :
            DotTextToFile+= x[0] + " -> " + i +"[label=\""+x[1]+"\"] \n"
    #fermeture de l'acollade
    DotTextToFile += "\n }"
    #ecriture dans le fichier
    f.write(DotTextToFile)
    #execution de la simmulation
    os.popen("python simulation.py")
    pass
   
#__main__
if __name__ == "__main__":    
#initialisation des etats et de l'alphabet
    print ("avertissement : si pour entrer plusieurs element séparer avec des espaces !")
    etats = set(input("les etat : " ).split(" "))
    alphabet =set(input("l'alphabet : ").split(" "))
    etatInitiale = set(input("etat initial : ").split(" "))
    etatFinale = set(input("etats finales :  ").split(" "))
    #parametrage des instructions
    #dictionnary
    nb=int(input("Entrer le nombre d'instruction : "))
    Instructions ={
        ('a','b') : ['d']
    }
    Instructions.clear()

    for x in range(nb):
        print("intruction num ",x," :")
        e = input("l'etat courant : ")
        l = input(" lecture de : ")
        etat = input("passage a l'etat : ").split(" ")
        Instructions[(e,l)]= etat


    """Instructions = {
        ('q0','a') : ['q1'],
        ('q1','c') : ['q2'],
        ('q1','$') : ['q2','q3'],
        ('q2','b') : ['q2','q3'],
        ('q2','a') : ['q2'],
        ('q2','$') : ['q3'],
        ('q3','$') : ['q4']
    }"""
         

    
    execution = AutomateEtatFini(etats, alphabet, Instructions, etatInitiale, etatFinale)
    

    
    #rendre l'automate simple
    execution.automate_simple()
    print("******Automate simple*******")
    for i,j in execution.transition_function.items():
        print(i,'--->',j)
    print("les etats finaux : ",execution.etatsFinals)
    print("l'état initial : ",execution.etatInit)
    #afficher(etats,etatInitiale,etatFinale,Instructions)
    
    #test NFA to DFA
    execution.nfa_to_dfa()
    print("******Automate Deterministe*******")
    for i,j in execution.transition_function.items():
        print(i,'--->',j)
    print("les etats finaux : ",execution.etatsFinals)
    print("l'état initial : ",execution.etatInit)
    #afficher(etats,etatInitiale,etatFinale,Instructions)
    
    print("******Reconaissance d'un mot*******")
    inp_program = tuple('a')
    #affichage de l'execution
    print("Mot  : ","".join(inp_program))
    print("Resultat : ",execution.run_with_input_list(inp_program))

    #transformation en automate reduit
    execution.Reduction()
    print("******Automate Reduit*******")
    for i,j in execution.transition_function.items():
        print(i,'--->',j)
    print("les etats finaux : ",execution.etatsFinals)
    print("l'état initial : ",execution.etatInit)
    #afficher(etats,etatInitiale,etatFinale,Instructions)
    
    #transformation miroir
    execution.miroir()
    print("******Miroir*******")
    for i,j in execution.transition_function.items():
        print(i,'--->',j)
    print("les etats finaux : ",execution.etatsFinals)
    print("l'état initial : ",execution.etatInit)
    #afficher(etats,etatInitiale,etatFinale,Instructions)
   
    #complement 
    execution.Complement()
    print("******Complement*******")
    for i,j in execution.transition_function.items():
        print(i,'--->',j)
    print("les etats finaux : ",execution.etatsFinals)
    print("l'état initial : ",execution.etatInit)
    #afficher(etats,etatInitiale,etatFinale,Instructions)"""
 
    
    
pass