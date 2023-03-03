## AutomaPy

The package contains a set of tools and algorithms for theoretical computer science, which could include automata theory as well as other topics.


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
#### Write a program for tokenization of given input.

```py

from AutomaPy import DFA

dfa = DFA()

print(dfa.tokenize("This is an example of tokenization."))

```
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
#### Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

```py

from AutomaPy import DFA

dfa = DFA()

dfa.addState("A", {"0": "B", "1": "B"}, initial_state=True, final_state=True)
dfa.addState("B", {"0": "A", "1": "A"}, final_state=True)

print(dfa.equalNumberOfOneZero("10"))
print(dfa.equalNumberOfOneZero("101100"))
print(dfa.equalNumberOfOneZero("1011"))

```
#### Design a program for creating a machine which count number of 1's and 0's in a given string.

```py

from AutomaPy import DFA

dfa.addState("A", {"0": "A", "1": "A"}, initial_state=True)

print(dfa.countNumberOfOneZero("0101"))
print(dfa.countNumberOfOneZero("01"))
print(dfa.countNumberOfOneZero("011111"))
print(dfa.countNumberOfOneZero("00000"))

```
