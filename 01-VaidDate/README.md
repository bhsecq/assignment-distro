Object-Oriented Programming  
Spring 2024 
Class 30 - INTERMEDIATE


# Getting Help 

* Card game [video lecture](https://drive.google.com/file/d/1lb_jEPVUz7pJPG8qPUVsL_f7t0oLG7SK/view?usp=sharing) and [demo code](https://replit.com/@mcarlberg/HW25DemoCardGame) 

* Class materials: Class 28 [whiteboard problems](https://docs.google.com/document/d/1Tymh8DzghSOVQohID6bldedubhL_jdUZw2ys5h2puiQ/edit?usp=sharing) and Class 29 [presentation on functions](https://docs.google.com/presentation/d/1Oo8YyS3l1MlMjmmMpK5ZMDbzlxhc8QDV0b9Jm2S-LP4/edit?usp=sharing)

* Lots of function [examples](https://replit.com/@mcarlberg/Sp24-HW27-FunctionsPractice-SOLUTIONS#main.py) (all HW 27 solutions included)

* W3Schools tutorial on [functions](https://www.w3schools.com/python/python_functions.asp)
   
* Relevant [flash cards](https://drive.google.com/file/d/1Pbpyg1eRtImUo-kD8Pbx9Y5JPk1WavrA/view?usp=sharing)

* Extended [reading](https://drive.google.com/file/d/1PVRf7MvHokHhCdiz7o4ey2tsB_nZSbgv/view?usp=sharing)

* All [Getting Help material](https://github.com/mattcarlberg/OOP-Sp24-Reference) from previous classes

# Challenge

Define a function named `is_valid_date()` with input/output behaviour `string --> bool`.

It determines whether an input string is of the form MM/DD/YYYY.  The date is considered valid if MM is an integer from 1-12, DD is an integer from 1 - 31 and YYYY is an integer from 1900 onwards.  While the  year must be written with four digits in order to be valid, the month and day could be single digits.  In other words, remember that 01/01/2021 and 1/1/2021 are both valid ways to write the same date.

# Function Name

is_valid_date()


# Function Input 

One parameter, which is a string.

# Output

Return True if the input string is a valid date, False otherwise. 

# Initial Test Code

You should always initially try out your program on small test cases that you code yourself in `main.py`.  Here are some examples:

```
x = "one/07/2003"
y = is_valid_date(x)
print(y)
```

should print the `False`


```
a = "1/07/2003"
b = is_valid_date(a)
print(b)
```

should print the `True`


# Automated Tests

**You should always initially try out your program on small test cases that you code yourself in `main.py`.**

After your own test code is working, try the automated tests by going to the "Shell" tab and typing:

```
python3 TestDate.py
``
