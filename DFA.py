# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:30:41 2020

@author: Snow
"""

class DFA:
    current_state = None;
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;
    
    def in_accept_state(self):
        return self.current_state in accept_states;
    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();
    pass;



states = {'q0','q1','q2','q3','q4'};
alphabet = {'a','b'};

tf = dict();
tf[('q0','a')] = ['q1','q3'];
tf[('q0','0')] = 'q3'

tf[('q1','b')] = 'q2'
#tf[('q1','0')] = 'q2'

tf[('q2','a')] = 'q3'
#tf[('q2','0')] = 'q4'

tf[('q3','b')] = 'q3'
 
 
 
"""tf[('q3','0')] = 'q5'

tf[('q4','1')] = 'q6'
tf[('q4','0')] = 'q4'

tf[('q5','1')] = 'q3'
tf[('q5','0')] = 'q7'

tf[('q6','1')] = 'q8'
tf[('q6','0')] = 'q4'

tf[('q7','1')] = 'q8'
tf[('q7','0')] = 'q7'

tf[('q8','1')] = 'q8'
tf[('q8','0')] = 'q7' """



start_state = 'q0';
accept_states = {'q3'};

d = DFA(states, alphabet, tf, start_state, accept_states);

inp_program = list('ababbbbbbb');

print (d.run_with_input_list(inp_program));