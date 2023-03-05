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

The code creates a `DFA` object and defines four states: `A`, `B`, `C`, and `D`. The transitions between these states are defined by dictionaries that map input symbols (0 or 1) to the next state. The initial state is set to `A`, and the final state is set to `D`.

The code then uses the `endingWithOneZeroOne` method of the DFA object to check if the given strings end with the pattern `"101"`. This method takes a string as input and returns `True` if the DFA accepts the string (i.e., if it ends in the final state), and `False` otherwise.

The first call to `endingWithOneZeroOne` with the input string `"101"` returns `True` because the DFA transitions from state `A` to state `B` on the first `"1"`, then from state `B` to state C on the `"0"`, and finally from state `C` to state `D` on the "1", which is the final state.

The second call to `endingWithOneZeroOne` with the input string `"01101"` also returns `True` because the DFA follows the same transitions as in the first case, but with an additional `"0"` input that takes it from state `A` to state `C`.

The third call to `endingWithOneZeroOne` with the input string `"011011"` returns False because the DFA transitions from state `A` to state `C` on the first `"0"`, then from state `C` to state `A` on the second `"1"`, and finally from state A to state `B` on the third `"1"`, which is not the final state.


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

The code then uses the `threeConsecutiveOne` method of the DFA object to check if the given strings contain three consecutive ones. This method takes a string as input and returns `True` if the DFA accepts the string (i.e., if it ends in one of the final states), and `False` otherwise.

The first call to `threeConsecutiveOne` with the input string `"010111"` returns `True` because the DFA transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `C` on the first `"1"`, then from state `C` to state `D` on the second `"1"`, and finally to one of the final states `(F, G, or H)` on the third `"1"`.

The second call to `threeConsecutiveOne` with the input string `"01011"` returns `False` because the `DFA` transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `C` on the first `"1"`, then from state `C` to state `D` on the second `"1"`, but it does not reach a final state because there is no third `"1"`.

The third call to `threeConsecutiveOne` with the input string `"010101"` returns `False` because the DFA transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `A` on the first `"1"`, then from state `A` to state `B` on the second `"0"`, then from state `B` to state `A` on the second `"1"`, and finally from state `A` to state `B` on the third `"0"`, which is not a valid transition according to the DFA definition.


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
