# Spell Checker

## Overview

This Python script uses the `spellchecker` module to check the spelling of words. If the input word is not found in the spell checker's dictionary, it suggests a corrected spelling for the word.

## Getting Started
To use this program, you should have Python installed on your computer. You can download Python from the official website [https://www.python.org/downloads/](https://www.python.org/downloads/) and install it according to the instructions provided.

## Installation

Clone this repository or download the spell_checker.py file.
Install the spellchecker module by running the following command in your terminal or command prompt:
```
pip install spellchecker
```
## Usage
To use the program, navigate to the directory where you saved the source code file and run it using the following command:
```
python spell_checker.py

```
The program will prompt you to enter a word. Enter the word and press enter. The program will check the spelling of the word and print the result.

## Functionality
The script uses the `SpellChecker` class from the `spellchecker` module to check the spelling of words. It first creates an instance of the `SpellChecker` class, and then checks if the input word is in the spell checker's dictionary using the `in` operator. If the word is in the dictionary, it prints "Correct" to the console. Otherwise, it suggests a corrected spelling for the word using the `correction()` method.

## Conclusion

This script is a simple example of how to use the `spellchecker` module to check the spelling of words in Python. However, it's important to note that the SpellChecker class may not always produce the correct spelling suggestion, especially for rare or technical words. Therefore, it's always a good idea to double-check the suggested correction if it looks suspicious.