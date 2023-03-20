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

print(dfa.check_string("101"))

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

print(dfa.check_string("111")) # True
print(dfa.check_string("11100")) # True
print(dfa.check_string("1001")) # False

```

#### 5. Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

```py

from AutomaPy import EqualNumberOfOneZero

dfa = EqualNumberOfOneZero()

print(dfa.check_string("111000")) # True
print(dfa.check_string("111001")) # False
print(dfa.check_string("1100")) # True

```

#### 6. Design a program for creating a machine which count number of 1's and 0's in a given string.

```py

from AutomaPy import CountNumberOfOneZero

dfa = CountNumberOfOneZero()

print(dfa.check_string("111000")) # True
print(dfa.check_string("111001")) # False
print(dfa.check_string("1100")) # True

```

#### 7. Design a program for Turing machine that’s accepts the even number of 1's.

```py

from AutomaPy import TuringMachineEvenOnes

dfa = TuringMachineEvenOnes()

print(dfa.check_string("101111")) #False because 5 is odd (there is 5 1's)
print(dfa.check_string("101")) #True because 2 is even (there is 2 1's)

```

#### You can enter following command to see what functions this package have.

```bash
AutomaPy --help
```
