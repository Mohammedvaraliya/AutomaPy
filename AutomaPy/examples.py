from AutomaPy.main import DFA, TuringMachine

# DFA for string ending with 101


class EndingWithOneZeroOne:
    def __init__(self):
        self.dfa = DFA()

        # Add the states to DFA
        self.dfa.addState("A" , {"0": "A", "1":"B"}, initial_state = True)
        self.dfa.addState("B" , {"0": "C", "1":"B"})
        self.dfa.addState("C" , {"0": "A", "1":"D"})
        self.dfa.addState("D" , {"0": "C", "1":"B"}, final_state=True)

    def check_string(self, string):
        return self.dfa.check_string(string)


# DFA for decimal number divisible by 2
class DecimalNumberDivisibleByTwo:
    def __init__(self):
        self.dfa = DFA()

        # Add the states to DFA
        self.dfa.addState("A", {"0": "A", "1": "B"}, initial_state=True, final_state=True)
        self.dfa.addState("B", {"0": "A", "1": "B"})

    def check_string(self, string):
        return self.dfa.check_string(string)


# DFA for string having "111"
class ThreeConsecutiveOne:
    def __init__(self):
        self.dfa = DFA()

        # Add the states to DFA
        self.dfa.addState("A" , {"0": "A", "1":"B"}, initial_state = True)
        self.dfa.addState("B" , {"0": "A", "1":"C"})
        self.dfa.addState("C" , {"0": "A", "1":"D"})
        self.dfa.addState("D" , {"0": "F", "1":"E"}, final_state=True)
        self.dfa.addState("E" , {"0": "E", "1":"E"})
        self.dfa.addState("F", {"0": "F", "1":"G"}, final_state=True)
        self.dfa.addState("G", {"0": "F", "1":"H"}, final_state=True)
        self.dfa.addState("H", {"0": "F", "1":"D"}, final_state=True)

    def check_string(self, string):
        return self.dfa.check_string(string)


# DFA for string having equal number of 1's and 0's
class EqualNumberOfOneZero:

    def __init__(self):
        self.dfa = DFA()

        # Add the states to DFA
        self.dfa.addState("A", {"0": "B", "1": "B"}, initial_state=True, final_state=True)
        self.dfa.addState("B", {"0": "A", "1": "A"})

    def check_string(self, string):
        return self.dfa.equalNumberOfOneZero(string)
        


# DFA counts the number of one and zero
class CountNumberOfOneZero:

    def __init__(self):
        self.dfa = DFA()

        # Add the states to DFA
        self.dfa.addState("A", {"0": "A", "1": "A"}, initial_state=True)

    def check_string(self, string):
        return self.dfa.countNumberOfOneZero(string)


# Turing machine that’s accepts the even number of 1's.
class TuringMachineEvenOnes:
    def __init__(self):
        self.tm = TuringMachine()

        # Add the states to TuringMachine
        self.tm.addState('A', {'0': ('A', '0', 'R'), '1': ('B', '0', 'R'), '_': ('B', '_', 'L')}, initial_state=True, final_state=True)
        self.tm.addState('B', {'0': ('B', '0', 'R'), '1': ('A', '0', 'R'), '_': ('A', '_', 'L')})

    def check_string(self, string):
        return self.tm.turingMachineEvenOnes(string)
    
