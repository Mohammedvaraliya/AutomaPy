class DFA:
    def __init__(self, input_state = {}, initial_state = None, final_state = []):
        self.input_state = input_state
        self.initial_state = initial_state
        self.final_state = final_state

    def addState(self, state_name: str, paths, initial_state=False, final_state=False):
        a = self.input_state[state_name] = paths

        if initial_state:
            self.initial_state = state_name

        if final_state:
            self.final_state.append(state_name)

        return a
    
    def endingWithOneZeroOne(self, string:str):
        current_state = self.initial_state # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True

        return False
    
    def decimalNumberDivisibleByTwo(self, string: str):
        current_state = self.initial_state  # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True
        return False

    def tokenize(self, input_str):
        tokens = []
        word = ""

        for char in input_str:
            if char.isalnum() or char.isalpha():
                word += char

            else:
                if word:
                    tokens.append(word)
                    word = ""
        return tokens

    def threeConsecutiveOne(self, string: str):
        current_state = self.initial_state  # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True

        return False
    
    def equalNumberOfOneZero(self, string: str):
        current_state = self.initial_state # By defaul initial state
        count_0 = 0
        count_1 = 0

        for s in string:
            # Transition to next state
            if s == "0":
                count_0 += 1
            if s == "1":
                count_1 += 1 
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state and count_0 == count_1:
            return True

        return False
    
    def countNumberOfOneZero(self, string: str):
        current_state = self.initial_state # By defaul initial state
        count_0 = 0
        count_1 = 0

        for s in string:
            # Transition to next state
            if s == "0":
                count_0 += 1
            if s == "1":
                count_1 += 1 
            current_state = self.input_state[current_state][s]

        return f"The Number of 1's is {count_1} and number of 0's is {count_0}"

    def print_state(self):
        for key, value in self.input_state.items():
            print(key, ":", value)


dfa = DFA()


if __name__ == "__main__":

    # Create a program that implements a machine that accepts strings ending with '101'.(Success)
    '''
    dfa.addState("A" , {"0": "A", "1":"B"}, initial_state = True)
    dfa.addState("B" , {"0": "C", "1":"B"})
    dfa.addState("C" , {"0": "A", "1":"D"})
    dfa.addState("D" , {"0": "C", "1":"B"}, final_state=True)

    print(dfa.endingWithOneZeroOne("101"))
    print(dfa.endingWithOneZeroOne("01101"))
    print(dfa.endingWithOneZeroOne("011011"))
    '''

    # Design a Program for creating machine that accepts three consecutive one.(Success)
    '''
    dfa.addState("A" , {"0": "A", "1":"B"}, initial_state = True)
    dfa.addState("B" , {"0": "A", "1":"C"})
    dfa.addState("C" , {"0": "A", "1":"D"})
    dfa.addState("D" , {"0": "F", "1":"E"}, final_state=True)
    dfa.addState("E" , {"0": "E", "1":"E"})
    dfa.addState("F", {"0": "F", "1":"G"}, final_state=True)
    dfa.addState("G", {"0": "F", "1":"H"}, final_state=True)
    dfa.addState("H", {"0": "F", "1":"D"}, final_state=True)

    print(dfa.threeConsecutiveOne("010111"))
    print(dfa.threeConsecutiveOne("01011"))
    print(dfa.threeConsecutiveOne("010101"))
    '''

    # Write a program for tokenization of given input.. (Success)
    '''
    print(dfa.tokenize("This is an example of tokenization."))
    '''

    # Design a program for accepting decimal number divisible by 2.(Success)
    '''
    dfa.addState("A", {"0": "A", "1": "B"}, initial_state=True, final_state=True)
    dfa.addState("B", {"0": "A", "1": "B"})

    print(dfa.decimalNumberDivisibleByTwo("10")) # Decimal number of "10" is 2
    print(dfa.decimalNumberDivisibleByTwo("110")) # Decimal number of "10" is 6
    print(dfa.decimalNumberDivisibleByTwo("101")) # Decimal number of "10" is 5
    '''

    # Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.(Success)
    '''
    dfa.addState("A", {"0": "B", "1": "B"}, initial_state=True, final_state=True)
    dfa.addState("B", {"0": "A", "1": "A"}, final_state=True)

    print(dfa.equalNumberOfOneZero("10"))
    print(dfa.equalNumberOfOneZero("101100"))
    print(dfa.equalNumberOfOneZero("1011"))
    '''

    # Design a program for creating a machine which count number of 1's and 0's in a given string.(Success)
    '''
    dfa.addState("A", {"0": "A", "1": "A"}, initial_state=True)

    print(dfa.countNumberOfOneZero("0101"))
    print(dfa.countNumberOfOneZero("01"))
    print(dfa.countNumberOfOneZero("011111"))
    print(dfa.countNumberOfOneZero("00000"))
    '''

