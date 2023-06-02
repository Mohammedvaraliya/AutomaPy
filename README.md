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

from AutomaPy import EndingWithOneZeroOne

dfa = EndingWithOneZeroOne()

print(dfa.check_string("101")) # True

```

#### 2. Design a Program for creating machine that accepts three consecutive one.

```py

from AutomaPy import ThreeConsecutiveOne

dfa = ThreeConsecutiveOne()

print(dfa.check_string("111")) # True
print(dfa.check_string("11100")) # True
print(dfa.check_string("1100")) # False

```

#### 3. Write a program for tokenization of given input.

```py

from AutomaPy import Tokenizer

tokenizer = Tokenizer()

print(tokenizer.tokenize("This is an example of tokenization."))

```

#### 4. Design a program for accepting decimal number divisible by 2.

```py

from AutomaPy import DecimalNumberDivisibleByTwo

dfa = DecimalNumberDivisibleByTwo()

print(dfa.check_string("10")) # Decimal number of "10" is 2
print(dfa.check_string("110")) # Decimal number of "10" is 6
print(dfa.check_string("101")) # Decimal number of "10" is 5

```

#### 5. Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

```py

from AutomaPy import EqualNumberOfOneZero

dfa = EqualNumberOfOneZero()

print(dfa.check_string("10")) # True
print(dfa.check_string("101100")) # True
print(dfa.check_string("1011")) # False

```

#### 6. Design a program for creating a machine which count number of 1's and 0's in a given string.

```py

from AutomaPy import CountNumberOfOneZero

dfa = CountNumberOfOneZero()

print(dfa.check_string("111000")) # The Number of 1's is 3 and number of 0's is 3
print(dfa.check_string("111001")) # The Number of 1's is 4 and number of 0's is 2
print(dfa.check_string("1100")) # The Number of 1's is 2 and number of 0's is 2

```

#### 7. Design a program for Turing machine that’s accepts the even number of 1's.

```py

from AutomaPy import TuringMachineEvenOnes

tm = TuringMachineEvenOnes()

print(tm.check_string("")) # True (because 0 is even number)
print(tm.check_string("1")) # False
print(tm.check_string("1111")) # True

```

#### You can enter following command to see what functions this package have.

```bash
AutomaPy --help
```
