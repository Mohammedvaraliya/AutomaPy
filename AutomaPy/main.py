class DFA:
    def __init__(self, input_state={}, initial_state=None, final_state=[]):
        """
        Initializes a new DFA object.

        :param input_state: A dictionary representing the transition function of the DFA.
        :type input_state: dict
        :param initial_state: The initial state of the DFA.
        :type initial_state: str
        :param final_state: The set of final states of the DFA.
        :type final_state: list
        """
        self.input_state = input_state
        self.initial_state = initial_state
        self.final_state = final_state

    def addState(self, state_name: str, paths, initial_state=False, final_state=False):
        """
        Adds a new state to the DFA.

        :param state_name: The name of the new state.
        :type state_name: str
        :param paths: A dictionary representing the transition function of the new state.
        :type paths: dict
        :param initial_state: Whether the new state is the initial state of the DFA.
        :type initial_state: bool
        :param final_state: Whether the new state is a final state of the DFA.
        :type final_state: bool
        :return: The transition function of the new state.
        :rtype: dict
        """
        a = self.input_state[state_name] = paths

        if initial_state:
            self.initial_state = state_name

        if final_state:
            self.final_state.append(state_name)

        return a

    def check_string(self, string: str):
        current_state = self.initial_state  # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True

        return False

    def endingWithOneZeroOne(self, string: str):
        """
        Checks whether a string ends with '101'.

        :param string: The input string to check.
        :type string: str
        :return: True if the string ends with '101', False otherwise.
        :rtype: bool

        States = 
            ("A" , {"0": "A", "1":"B"}, initial_state = True)\n
            ("B" , {"0": "C", "1":"B"})\n
            ("C" , {"0": "A", "1":"D"})\n
            ("D" , {"0": "C", "1":"B"}, final_state=True)

        """

        current_state = self.initial_state  # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True

        return False

    def decimalNumberDivisibleByTwo(self, string: str):
        """
        Checks whether a binary string represents a decimal number divisible by two.

        :param string: The input binary string to check.
        :type string: str
        :return: True if the binary string represents a decimal number divisible by two, False otherwise.
        :rtype: bool

        States = 
            ("A", {"0": "A", "1": "B"}, initial_state=True, final_state=True)\n
            ("B", {"0": "A", "1": "B"})
        """
        current_state = self.initial_state  # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True
        return False

    

    def threeConsecutiveOne(self, string: str):
        """
        Checks whether a string contains three consecutive ones.

        :param string: The input string to check.
        :type string: str
        :return: True if the string contains three consecutive ones, False otherwise.
        :rtype: bool

        States = 
            ("A" , {"0": "A", "1":"B"}, initial_state = True)\n
            ("B" , {"0": "A", "1":"C"})\n
            ("C" , {"0": "A", "1":"D"})\n
            ("D" , {"0": "F", "1":"E"}, final_state=True)\n
            ("E" , {"0": "E", "1":"E"})\n
            ("F", {"0": "F", "1":"G"}, final_state=True)\n
            ("G", {"0": "F", "1":"H"}, final_state=True)\n
            ("H", {"0": "F", "1":"D"}, final_state=True)
        """
        current_state = self.initial_state  # By defaul initial state

        for s in string:
            current_state = self.input_state[current_state][s]

        if current_state in self.final_state:
            return True

        return False

    def equalNumberOfOneZero(self, string: str):
        """
        Checks whether the given string has an equal number of 1's and 0's by traversing the DFA.

        Args:
            string (str): The input string to check for an equal number of 1's and 0's.

        Returns:
            bool: True if the input string has an equal number of 1's and 0's and ends in a final state,
                False otherwise.

        States = 
            ("A", {"0": "B", "1": "B"}, initial_state=True, final_state=True)\n
            ("B", {"0": "A", "1": "A"})
        """
        current_state = self.initial_state  # By defaul initial state
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
        """
        Counts the number of 1's and 0's in the given string by traversing the DFA.

        Args:
            string (str): The input string to count the number of 1's and 0's.

        Returns:
            str: A string indicating the number of 1's and 0's in the input string in the format 
                "The Number of 1's is {count_1} and number of 0's is {count_0}".

        States = 
            ("A", {"0": "A", "1": "A"}, initial_state=True)
        """
        current_state = self.initial_state  # By defaul initial state
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
        """
        Prints the current state transition table of the DFA.
        """
        for key, value in self.input_state.items():
            print(key, ":", value)

class Tokenizer:
    def tokenize(self, input_str):
        """
        Splits a string into tokens.

        :param input_str: The input string to tokenize.
        :type input_str: str
        :return: A list of tokens.
        :rtype: list
        """
        tokens = []
        word = ""

        for char in input_str:
            if char.isalnum() or char.isalpha():
                word += char

            else:
                if word:
                    tokens.append(word)
                    word = ""
        
        if word:
            tokens.append(word)
            word = ""
            
        return tokens



class TuringMachine:
    def __init__(self, input_state={}, initial_state=None, final_state=[]):
        """
        Initializes a new TuringMAchine object.

        :param input_state: A dictionary representing the transition function of the TuringMachine.
        :type input_state: dict
        :param initial_state: The initial state of the TuringMachine.
        :type initial_state: str
        :param final_state: The set of final states of the TuringMachine.
        :type final_state: list
        """
        self.input_state = input_state
        self.initial_state = initial_state
        self.final_state = final_state

    def addState(self, state_name: str, paths, initial_state=False, final_state=False):
        """
        Adds a new state to the TuringMachine.

        :param state_name: The name of the new state.
        :type state_name: str
        :param paths: A dictionary representing the transition function of the new state.
        :type paths: dict
        :param initial_state: Whether the new state is the initial state of the TuringMachine.
        :type initial_state: bool
        :param final_state: Whether the new state is a final state of the TuringMachine.
        :type final_state: bool
        :return: The transition function of the new state.
        :rtype: dict
        """
        a = self.input_state[state_name] = paths

        if initial_state:
            self.initial_state = state_name

        if final_state:
            self.final_state.append(state_name)

        return a

    def turingMachineEvenOnes(self, input_str):
        """
        Simulates a Turing machine on a given input string.

        This function takes an input string and simulates a Turing machine on it using a set of predefined rules. The rules are stored in the `input_state` dictionary, which maps each state to a dictionary of transitions, where each transition is defined as a tuple of the form (new_state, write_value, move_dir).

        Args:
            input_str (str): The input string to simulate the Turing machine on.

        Returns:
            bool: True if the Turing machine accepts the input string, False otherwise.

        Raises:
            KeyError: If the current state does not have a transition defined for the current input symbol.

        Example:
            >>> input_state = {
            ...     'A': {'0': ('A', '0', 'R'), '1': ('B', '0', 'R'), '_': ('B', '_', 'L')},
            ...     'B': {'0': ('B', '0', 'R'), '1': ('A', '0', 'R'), '_': ('A', '_', 'L')}
            ... }
            >>> initial_state = 'A'
            >>> final_state = {'A'}
            >>> tm = TuringMachine(input_state, initial_state, final_state)
            >>> tm.turing_machine('011')
            True
            >>> tm.turing_machine('1101')
            False
        """
        current_state = self.initial_state
        tape = list(input_str)
        i_head = 0

        if len(input_str) == 0:
            return True

        while True:
            if tape[i_head] not in self.input_state[current_state]:
                return False

            new_state, write_value, move_dir = self.input_state[current_state][tape[i_head]]
            tape[i_head] = write_value

            if move_dir == 'R':
                i_head += 1
            elif move_dir == 'L':
                i_head -= 1

            current_state = new_state

            if current_state in self.final_state and i_head >= len(tape):
                return True
            elif current_state not in self.input_state or i_head >= len(tape) or i_head < 0:
                return False


if __name__ == "__main__":

    dfa = DFA()
    tm = TuringMachine()

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
    dfa.addState("B", {"0": "A", "1": "A"})

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

    # Design a program for Turing machine that’s accepts the even number of 1's.(Success)
    '''
    tm.addState('A', {'0': ('A', '0', 'R'), '1': ('B', '0', 'R'), '_': ('B', '_', 'L')}, initial_state=True, final_state=True)
    tm.addState('B', {'0': ('B', '0', 'R'), '1': ('A', '0', 'R'), '_': ('A', '_', 'L')})

    print(tm.turingMachineEvenOnes("")) # True (because 0 is even number)
    print(tm.turingMachineEvenOnes("1")) # False
    print(tm.turingMachineEvenOnes("1111")) # True
    '''
