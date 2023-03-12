## AutomaPy

[![Latest PyPI version](https://img.shields.io/pypi/v/AutomaPy.svg)](https://pypi.python.org/pypi/AutomaPy/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/AutomaPy.svg)](https://pypi.python.org/pypi/AutomaPy/)
[![Total downloads](https://pepy.tech/badge/AutomaPy)](https://pepy.tech/project/AutomaPy)


The package contains a set of tools and algorithms for theoretical computer science, which could include automata theory as well as other topics.


## Installation

    pip install AutomaPy


## Examples of How To Use (AutomaPy)

#### Create a program that implements a machine that accepts strings ending with '101'.

```py

from AutomaPy import DFA

dfa = DFA()

dfa.addState("A" , {"0": "A", "1":"B"}, initial_state = True)
dfa.addState("B" , {"0": "C", "1":"B"})
dfa.addState("C" , {"0": "A", "1":"D"})
dfa.addState("D" , {"0": "C", "1":"B"}, final_state=True)

print(dfa.endingWithOneZeroOne("101"))
print(dfa.endingWithOneZeroOne("01101"))
print(dfa.endingWithOneZeroOne("011011"))

```

The code creates a `DFA` object and defines four states: `A`, `B`, `C`, and `D`. The transitions between these states are defined by dictionaries that map input symbols (0 or 1) to the next state. The initial state is set to `A`, and the final state is set to `D`.

The code then uses the `endingWithOneZeroOne()` method of the DFA object to check if the given strings end with the pattern `"101"`. This method takes a string as input and returns `True` if the DFA accepts the string (i.e., if it ends in the final state), and `False` otherwise.

The first call to `endingWithOneZeroOne()` with the input string `"101"` returns `True` because the DFA transitions from state `A` to state `B` on the first `"1"`, then from state `B` to state C on the `"0"`, and finally from state `C` to state `D` on the "1", which is the final state.

The second call to `endingWithOneZeroOne()` with the input string `"01101"` also returns `True` because the DFA follows the same transitions as in the first case, but with an additional `"0"` input that takes it from state `A` to state `C`.

The third call to `endingWithOneZeroOne()` with the input string `"011011"` returns False because the DFA transitions from state `A` to state `C` on the first `"0"`, then from state `C` to state `A` on the second `"1"`, and finally from state A to state `B` on the third `"1"`, which is not the final state.


#### Design a Program for creating machine that accepts three consecutive one.

```py

from AutomaPy import DFA

dfa = DFA()

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

```

The code creates a DFA object and defines eight states: `A`, `B`, `C`, `D`, `E`, `F`, `G`, and `H`. The transitions between these states are defined by dictionaries that map input symbols (0 or 1) to the next state. The initial state is set to `A`, and the final states are set to `D`, `F`, `G`, and `H`.

The code then uses the `threeConsecutiveOne()` method of the DFA object to check if the given strings contain three consecutive ones. This method takes a string as input and returns `True` if the DFA accepts the string (i.e., if it ends in one of the final states), and `False` otherwise.

The first call to `threeConsecutiveOne()` with the input string `"010111"` returns `True` because the DFA transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `C` on the first `"1"`, then from state `C` to state `D` on the second `"1"`, and finally to one of the final states `(F, G, or H)` on the third `"1"`.

The second call to `threeConsecutiveOne()` with the input string `"01011"` returns `False` because the `DFA` transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `C` on the first `"1"`, then from state `C` to state `D` on the second `"1"`, but it does not reach a final state because there is no third `"1"`.

The third call to `threeConsecutiveOne()` with the input string `"010101"` returns `False` because the DFA transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `A` on the first `"1"`, then from state `A` to state `B` on the second `"0"`, then from state `B` to state `A` on the second `"1"`, and finally from state `A` to state `B` on the third `"0"`, which is not a valid transition according to the DFA definition.


#### Write a program for tokenization of given input.

```py

from AutomaPy import DFA

dfa = DFA()

print(dfa.tokenize("This is an example of tokenization."))

```

The `tokenize()` method of the DFA object is then used to `tokenize` a given string. This method takes a string as input and returns a list of tokens, where each token is a tuple that contains the token type and the token value.

In the given code, the `tokenize` method is called with the input string `"This is an example of tokenization."`. The method uses the predefined rules to split the input string into `tokens`, which are returned as a list of tuples. Each tuple contains a token type and the corresponding token value. For example, the first tuple in the list might be ('WORD', `'This'`), indicating that the token is a word and its value is `"This"`.


#### Design a program for accepting decimal number divisible by 2.

```py

from AutomaPy import DFA

dfa = DFA()

dfa.addState("A", {"0": "A", "1": "B"}, initial_state=True, final_state=True)
dfa.addState("B", {"0": "A", "1": "B"})

print(dfa.decimalNumberDivisibleByTwo("10")) # Decimal number of "10" is 2
print(dfa.decimalNumberDivisibleByTwo("110")) # Decimal number of "10" is 6
print(dfa.decimalNumberDivisibleByTwo("101")) # Decimal number of "10" is 5

```

The code creates a DFA that recognizes decimal numbers divisible by 2 using the AutomaPy package. The DFA has two states `("A" and "B")` and transitions based on input symbols `"0"` and `"1"`. The `decimalNumberDivisibleByTwo()` method simulates the DFA on a decimal number represented as a string and returns `True` if the DFA reaches a final state after consuming the entire string, indicating that the number is divisible by 2. The method is called with three different input strings and returns `True` for the first two and `False` for the last one, based on whether the input string represents a decimal number that is divisible by 2 or not.


#### Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

```py

from AutomaPy import DFA

dfa = DFA()

dfa.addState("A", {"0": "B", "1": "B"}, initial_state=True, final_state=True)
dfa.addState("B", {"0": "A", "1": "A"})

print(dfa.equalNumberOfOneZero("10"))
print(dfa.equalNumberOfOneZero("101100"))
print(dfa.equalNumberOfOneZero("1011"))

```

The code creates a DFA that recognizes strings containing an equal number of `1s` and `0s` using the AutomaPy package. The DFA has two states `("A" and "B")` and transitions based on input symbols `"0"` and `"1"`. The `equalNumberOfOneZero()` method simulates the DFA on an input string and returns `True` if the DFA reaches a final state after consuming the entire string, indicating that the string has an equal number of `1s` and `0s`. The method is called with three different input strings and returns `True` for the first and last one and `False` for the second one, based on whether the input string has an equal number of `1s` and `0s` or not.


#### Design a program for creating a machine which count number of 1's and 0's in a given string.

```py

from AutomaPy import DFA

dfa = DFA()

dfa.addState("A", {"0": "A", "1": "A"}, initial_state=True)

print(dfa.countNumberOfOneZero("0101"))
print(dfa.countNumberOfOneZero("01"))
print(dfa.countNumberOfOneZero("011111"))
print(dfa.countNumberOfOneZero("00000"))

```

The `countNumberOfOneZero()` method in the code counts the number of occurrences of `"0"` and `"1"` symbols in the input string and returns the count as a string.

For example, if the input string is `"0101"`, the method will return `"The number of 0's is 2 and the number of 1's is 2"`. Similarly, if the input string is `"011111"`, the method will return `"The number of 0's is 1 and the number of 1's is 5"`.


### Design a program for Turing machine that’s accepts the even number of 1's.

```py

from AutomaPy import TuringMachine

tm = TuringMachine()

tm.addState('A', {'0': ('A', '0', 'R'), '1': ('B', '0', 'R'), '_': ('B', '_', 'L')}, initial_state=True, final_state=True)
tm.addState('B', {'0': ('B', '0', 'R'), '1': ('A', '0', 'R'), '_': ('A', '_', 'L')})

print(tm.turingMachineEvenOnes("")) # True (because 0 is even number)
print(tm.turingMachineEvenOnes("1")) # False
print(tm.turingMachineEvenOnes("1111")) # True

```

The `turingMachineEvenOnes()` method checks whether a binary input string has an even number of `1's` using the Turing machine defined in the example. 

It returns a boolean indicating whether the input string is accepted by the Turing machine, which is `True` if the string has an even number of `1's` and `False` otherwise.



