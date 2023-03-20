import argparse
from AutomaPy.main import DFA, TuringMachine

def main():

    description = '''
    
    AutomaPy is a Python package for working with deterministic finite automata (DFA) and Turing machines. It provides classes and methods to create, simulate, and analyze automata and their behaviors. AutomaPy can be used for educational, research, or practical purposes.
    
    AutomaPy provides some functions such as:

    The code you provided contains different functions that implement different machines using the AutomaPy package. Here's a brief description of each function:

    endingWithOneZeroOne():             This function implements a deterministic finite automaton (DFA) 
                                        that accepts strings ending with '101'.

    threeConsecutiveOne():              This function creates a DFA that accepts strings with three 
                                        consecutive '1's.

    tokenize():                         This function tokenizes the input string by splitting it into 
                                        words.

    decimalNumberDivisibleByTwo():      This function creates a DFA that accepts decimal numbers 
                                        that are divisible by 2.

    equalNumberOfOneZero():             This function creates a DFA that accepts strings with an equal 
                                        number of '1's and '0's.

    countNumberOfOneZero():             This function counts the number of '1's and '0's 
                                        in a given string.

    turingMachineEvenOnes():            This function implements a Turing machine that accepts strings 
                                        with an even number of '1's.

    
    '''

    parser = argparse.ArgumentParser(description=description, 
                                     formatter_class=argparse.RawTextHelpFormatter)
    
    # parser.add_argument('--help', action='store_true', help='display help information')
    args = parser.parse_args()
    
    if args.help:
        print(description)

if __name__ == '__main__':
    main()