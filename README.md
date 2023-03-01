## AutomaPy

The package contains a set of tools and algorithms for theoretical computer science, which could include automata theory as well as other topics.

## Examples of How To Use (AutomaPy)

1. Design a program for accepting decimal number divisible by 2.

```py

from AutomaPy import DFA
result = DFA()
result.addState("A", {"0": "A", "1": "B"}, initial_state=True, final_state=True)
result.addState("B", {"0": "A", "1": "B"})
print(result.decimalNumberDivisibleByTwo("10")) # Decimal number of "10" is 2
print(result.decimalNumberDivisibleByTwo("110")) # Decimal number of "10" is 6
print(result.decimalNumberDivisibleByTwo("101")) # Decimal number of "10" is 5

```