# Password Checker

**Author:** Muhammad Zaraiz  
**Course:** Applications of ICT  
**Assignment:** Assignment 1

## Purpose

This beginner-friendly Python program checks whether an invented sample password meets five basic password requirements. It prints the checks that pass or fail and gives a score out of 5.

## Checks

The password checker looks for:

1. At least 12 characters
2. An uppercase letter
3. A lowercase letter
4. A digit
5. A special character

## How to Run

Make sure Python is installed, open a terminal in this folder, and run:

```text
python password_checker.py
```

When prompted, enter an invented sample password. Do not enter a real password.

## Example Inputs

Passing example:

```text
LongEnough1!
```

Failing example:

```text
hello
```

The program also handles empty input by reporting that no password was entered.

## Limitations

This program only checks basic character requirements. Passing all five checks does not guarantee that a password is secure. It does not check for common passwords, leaked passwords, repeated patterns, or whether a password is safe to use online. The checker is for learning purposes and should not be used as a complete security tool.
