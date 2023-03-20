## AutomaPy

[![Latest PyPI version](https://img.shields.io/pypi/v/AutomaPy.svg)](https://pypi.python.org/pypi/AutomaPy/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/AutomaPy.svg)](https://pypi.python.org/pypi/AutomaPy/)
[![Total downloads](https://pepy.tech/badge/AutomaPy)](https://pepy.tech/project/AutomaPy)

The package contains a set of tools and algorithms for theoretical computer science, which could include automata theory as well as other topics.

## Installation

    pip install AutomaPy

## Examples of How To Use (AutomaPy)

#### 1. Create a program that implements a machine that accepts strings ending with '101'.

```py

from AutomaPy.examples import EndingWithOneZeroOne

dfa = EndingWithOneZeroOne()

print(dfa.check_string("101"))

```

The code creates a `DFA` object and defines four states: `A`, `B`, `C`, and `D`. The transitions between these states are defined by dictionaries that map input symbols (0 or 1) to the next state. The initial state is set to `A`, and the final state is set to `D`.

The code then uses the `endingWithOneZeroOne()` method of the DFA object to check if the given strings end with the pattern `"101"`. This method takes a string as input and returns `True` if the DFA accepts the string (i.e., if it ends in the final state), and `False` otherwise.

The first call to `endingWithOneZeroOne()` with the input string `"101"` returns `True` because the DFA transitions from state `A` to state `B` on the first `"1"`, then from state `B` to state C on the `"0"`, and finally from state `C` to state `D` on the "1", which is the final state.

The second call to `endingWithOneZeroOne()` with the input string `"01101"` also returns `True` because the DFA follows the same transitions as in the first case, but with an additional `"0"` input that takes it from state `A` to state `C`.

The third call to `endingWithOneZeroOne()` with the input string `"011011"` returns False because the DFA transitions from state `A` to state `C` on the first `"0"`, then from state `C` to state `A` on the second `"1"`, and finally from state A to state `B` on the third `"1"`, which is not the final state.

#### 2. Design a Program for creating machine that accepts three consecutive one.

```py

from AutomaPy.examples import ThreeConsecutiveOne

dfa = ThreeConsecutiveOne()

print(dfa.check_string("111")) # True
print(dfa.check_string("11100")) # True
print(dfa.check_string("1100")) # False

```

The code creates a DFA object and defines eight states: `A`, `B`, `C`, `D`, `E`, `F`, `G`, and `H`. The transitions between these states are defined by dictionaries that map input symbols (0 or 1) to the next state. The initial state is set to `A`, and the final states are set to `D`, `F`, `G`, and `H`.

The code then uses the `threeConsecutiveOne()` method of the DFA object to check if the given strings contain three consecutive ones. This method takes a string as input and returns `True` if the DFA accepts the string (i.e., if it ends in one of the final states), and `False` otherwise.

The first call to `threeConsecutiveOne()` with the input string `"010111"` returns `True` because the DFA transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `C` on the first `"1"`, then from state `C` to state `D` on the second `"1"`, and finally to one of the final states `(F, G, or H)` on the third `"1"`.

The second call to `threeConsecutiveOne()` with the input string `"01011"` returns `False` because the `DFA` transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `C` on the first `"1"`, then from state `C` to state `D` on the second `"1"`, but it does not reach a final state because there is no third `"1"`.

The third call to `threeConsecutiveOne()` with the input string `"010101"` returns `False` because the DFA transitions from state `A` to state `B` on the first `"0"`, then from state `B` to state `A` on the first `"1"`, then from state `A` to state `B` on the second `"0"`, then from state `B` to state `A` on the second `"1"`, and finally from state `A` to state `B` on the third `"0"`, which is not a valid transition according to the DFA definition.

#### 3. Write a program for tokenization of given input.

```py

from AutomaPy import Tokenizer

tokenizer = Tokenizer()

print(tokenizer.tokenize("This is an example of tokenization."))

```

The `tokenize()` method of the Tokenizer object is then used to `tokenize` a given string. This method takes a string as input and returns a list of tokens, where each token is a tuple that contains the token type and the token value.

In the given code, the `tokenize` method is called with the input string `"This is an example of tokenization."`. The method uses the predefined rules to split the input string into `tokens`, which are returned as a list of tuples. Each tuple contains a token type and the corresponding token value. For example, the first tuple in the list might be ('WORD', `'This'`), indicating that the token is a word and its value is `"This"`.

#### 4. Design a program for accepting decimal number divisible by 2.

```py

from AutomaPy.examples import DecimalNumberDivisibleByTwo

dfa = DecimalNumberDivisibleByTwo()

print(dfa.check_string("111")) # True
print(dfa.check_string("11100")) # True
print(dfa.check_string("1001")) # False

```

The code creates a DFA that recognizes decimal numbers divisible by 2 using the AutomaPy package. The DFA has two states `("A" and "B")` and transitions based on input symbols `"0"` and `"1"`. The `decimalNumberDivisibleByTwo()` method simulates the DFA on a decimal number represented as a string and returns `True` if the DFA reaches a final state after consuming the entire string, indicating that the number is divisible by 2. The method is called with three different input strings and returns `True` for the first two and `False` for the last one, based on whether the input string represents a decimal number that is divisible by 2 or not.

#### 5. Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

```py

from AutomaPy.examples import EqualNumberOfOneZero

dfa = EqualNumberOfOneZero()

print(dfa.check_string("111000")) # True
print(dfa.check_string("111001")) # False
print(dfa.check_string("1100")) # True

```

The code creates a DFA that recognizes strings containing an equal number of `1s` and `0s` using the AutomaPy package. The DFA has two states `("A" and "B")` and transitions based on input symbols `"0"` and `"1"`. The `equalNumberOfOneZero()` method simulates the DFA on an input string and returns `True` if the DFA reaches a final state after consuming the entire string, indicating that the string has an equal number of `1s` and `0s`. The method is called with three different input strings and returns `True` for the first and last one and `False` for the second one, based on whether the input string has an equal number of `1s` and `0s` or not.

#### 6. Design a program for creating a machine which count number of 1's and 0's in a given string.

```py

from AutomaPy.examples import CountNumberOfOneZero

dfa = CountNumberOfOneZero()

print(dfa.check_string("111000")) # True
print(dfa.check_string("111001")) # False
print(dfa.check_string("1100")) # True

```

The `countNumberOfOneZero()` method in the code counts the number of occurrences of `"0"` and `"1"` symbols in the input string and returns the count as a string.

For example, if the input string is `"0101"`, the method will return `"The number of 0's is 2 and the number of 1's is 2"`. Similarly, if the input string is `"011111"`, the method will return `"The number of 0's is 1 and the number of 1's is 5"`.

#### 7. Design a program for Turing machine that’s accepts the even number of 1's.

```py

from AutomaPy.examples import TuringMachineEvenOnes

dfa = TuringMachineEvenOnes()

print(dfa.check_string("101111")) #False because 5 is odd (there is 5 1's)
print(dfa.check_string("101")) #True because 2 is even (there is 2 1's)

```

The `turingMachineEvenOnes()` method checks whether a binary input string has an even number of `1's` using the Turing machine defined in the example.

It returns a boolean indicating whether the input string is accepted by the Turing machine, which is `True` if the string has an even number of `1's` and `False` otherwise.

#### You can enter following command to see what functions this package have.

```bash
AutomaPy --help
```
