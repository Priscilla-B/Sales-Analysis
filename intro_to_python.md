# Introduction to Python
![](assets/images/introduction_to_python.png)

## What is Python?
Python is a general purpose programming language for solving a variety of problems.

## What are some uses of python?
- Data Analysis
- Machine Learning and Artificial Intelligence
- Web Development
- Game Development
- Mobile and Desktop Applications
- Task Automation

## Companies using Python
- Google uses python in its web search system
- ESRI uses python as an end-user customization tool for its popular GIS mapping products
- Youtube is largely written in python. Same with Reddit, Pinterest and Instagram
- Companies like Uber, Goldman Sachs, Paypal, Netflix and Google require developers and data specialists to work with python.
- Intel, Cisco, HP, Seagate, Qualcomm, and IBM use python for hardware testing

## Algorithm vs Program
- An algorithm is an idea or a way to solve a problem
- A program is a sequence of instructions written so that a computer can perform certain tasks.


## Python Syntax

### **Variables in Python**
A python variable stores a value in memory as a program runs. A variable is created by an equal to assignment.
e.g. x = 4, creates a variable called x which stores a value called 4.

![](assets/images/py-var1.png)

A python variable can be reassigned or swapped. Different variables can store the same values. 

![](assets/images/py-var2.png)

### **Math and expressions**
- **Numbers**:There are two different types of numbers for arithmetic operations in python. These are "int" (e.g., 3, -4) for whole integer numbers and "float" (e.g. 2.45, -5.67) for decimal numbers.
- **Precedence**: Arithmetic operations in python follows the same precendence rules as in mathematics. Remember *BODMAS*!
- **Expressions**:
    - Division / yields float
    - Int Division // rounds to an integer
    - The ** operator does exponentiation
    - The "modulo" or "mod" operator is the remainder after division

![](assets/images/math1.png)     ![](assets/images/math2.png)


### **Print and Input**
- The python print function `print()` takes in python data such as ints and strings and shows them in the terminal on one line of text. The items are converted to text form, separated by spaces.

![](assets/images/print1.png)

- The input function `input()` allows us to take information from a particular user. That user information can further used in a program, or printed back to the user.

![](assets/images/input1.png)


### **If and Comparison**
The `if` statement controls if some lines run or not. The if statement syntax has four parts:
- `if`
- boolean test
- colon
- indented body lines

    
```py
num = 6
if num == 6:
    print("Yay 6")
```

The simplest and most common boolean tests use `==` to compare two values and results in `True` if both values are the same, otherwise, it's `False`. Other operators like `>`, `<`, `>=`, `<=` can also be used.

The values `True` and `False` are known as Boolean values and have the data type "bool", short term for "boolean". They are usually used to control if and while loops.   The operators used in boolean tests can also be combined with the keywords `and`, `or` and `not`.These are known as logical operators. They help test for multiple conditions at the same time, or invert a boolean test(in the case of `not`).
These logical operators follow this precedence: `not` is the highest order, followed by `and` and finally `or`, similar to the precedence for the mathematical operators `-`, `*`, `+`.
Try these in your terminal: `9 < 6 and  3 < 6 or 2 < 6`,  `9 < 6 and  (3 < 6 or 2 < 6)`

- There's an optional `else:` part of an if statement that enables you to add code to run if the boolean test is `False`.

    ```py
    score = 97
    high_score = 91
    if score > high_score:
        message = "New High Score !"
    else:
        message = "Oh well!"
    ```

- We also use `elif` (else if) blocks in if statements when we need to evaluate more than two conditions and take various actions based on the boolean tests for each of those conditions. Think of them like nested if statements in excel.
    ```py
    s = 'e'
    if s == 'a':
        print("letter a")
    elif s == 'b':
        print("letter b")
    else:
        print("another letter")
    ```


### **While and For Loops**
A loop takes a few lines of code and runs them over and over again.

**While Loops**: A while-loop uses a boolean test expression to control the run of a body of lines of code. We use a while-loop when we want to run(execute) some lines of code as long as a certain condition is met, without explicitly stating the number of times we want to run those codes.
The while-loop syntax has four parts: `while`, boolean test, colon, indented body line.
```py
while test:
    indented body lines
```

The while operation checks the boolean test expression. If it evaluates to `True`, it runs all the indented body of lines from top to bottom. It then goes back to the boolean test, check it's value again, and so on. If the test is `False`, the loop stops, and the lines of code after the loops are run.

```py
i = 0
while i < 10:
    print(i)
    i = i + 1
print("All done")
```
Considerations:
- very often the last line of the while body act as an increment factor. It increases the variable used for the boolean test in order to advance it to the ultimate end of the loop.
- while loops can have zero iterations, and that's okay
- It's possible to write a loop that never exits. This happens when the boolean test is always true. It can also happen if the last increment line is eliminated.

**For Loops**: The for loop is the most commonly used of all loops. The for-loop, also known as the "for each" loop look at each element in a collection(for example, a list) once.
```py
for num in [2, 4, 6, 8]:
    print(num)
```
The loop begins with the keyword `for` followed by a variable(in this example `num`) to use in the loop. This is followed by the keyword `in` and a collection of elements for the loop(in this example `[2, 4, 6, 8]`). After this, there is a colon(`:`) followed by the indented body lines.
The loop runs the body of lines again and again for each member of the collection.

The python `range()` function can be used to create a collection of numbers on the fly. For example `range(10)` gives a collection of numbers starting from 0 ending at 9. `range(3, 8)` gives a collection of numbers starting from 3 ending at 7. 
```py
for i in range(6):
    print(6)
```

### Functions
Functions help us divide lines of codes into sensible sub-parts. Functions are written to carry out a specific task and can be used repeatedly when needed.
There are three main types of functions:
- Built-in functions such as `print()`, `range()`, `min()`, `max()`, etc.
- User-defined functions, which are functions users create to help them perform specific tasks
- Anonymous or lambda functions, which are functions which are declared without the standard `def` keyword.

Parts of a function definition:
- **def**: a function begins with the word `def`
- **name**: the function's name, chosen by the programmer
- **parenthesis**: a pair of parenthesis `()` follows the function name
- **body lines**: lines of code which makes up the function

Functions can take in optional arguments and return values. Function arguments helps us pass information into the functions, and can be any data type or structure. The return statement enables the function to send some information whenever the function is *called*.

To "call" a function is to invoke and run its lines of code. You call a function by typing the function's name followed by `()`. You supply the function with the needed parameters if the function has one.
 ```py
 def my_function(args):
     # body of lines
     return # some value

```
**Notes**:
- You can call a function within a function, but defining a function within a function (although is legal) is not usually best practice
- When you define a variable within a function, that variable exists only within that function(local variable). Global variables are available throughout the entire file and are not bound to particular functions.
- Returning a value through a function and printing are not the same. A function's return value can be printed or stored as a variable or used directly in other lines of code. When we print a value from a function, that value only shows up on the console and cannot be used in other line of code.
A function's return value cannot be automatically seen on the console and must be printed before it can be seen on the console.

### Data Structures
Data structures are a fundamental aspect of any programming work flow. Data structures enables us to store data in a more organized and managed format which allows us to easily access stored data, relate them and perform operations on them efficiently.

Python has various built-in data structures which includes Lists, Dictionaries, Sets and Tuples. For our purpose, we will be focusing on Lists and Dictionaries, which are more commonly used.

**Lists**
Lists help us to store data in a sequential manner. A list contains series of any data type: strings, ints, other lists. Items inside a list are generally called elements.
Items in a list can be assessed by using identifiers known as "indexes". These can be thought of as addresses assigned to every element in the list based on their position in the list.

```py
empty_list = [] # create an empty list
filled_list = [1, 3, 'a', '❤️', 9,'!'] # creating a list with different kinds of data
```

- Indexing: List indexes start from 0 and goes on until the last element of the list(positive indexing). We can also access elements in a list by moving from last element to first, starting from -1. This is called positive indexing.

```py
>>> filled_list[0] # returns first element of list
1
>>> filled_list[-1] # returns last element of list
'!'
>>> filled_list[2:5] # returns third, fourth and fifth element of list
['a', '❤️', 9]
>>> filled_list[:3] # returns first three elements of list
[1, 3, 'a']
```

- List Operations:
    - len(list): acess the length of a list
        ```py
        >>>len(filled_list)
        6
        ```
    - for x in list: loop over list elements
        ```py
        >>> for x in filled_list:
                print(x)
        1
        3
        'a'
        '❤️'
        9
        '!'
        ```
    - list.append(element): add an element to the end of a list to increase its length by 1.
        ```py
        >>> filled_list.append('hello')
        [1, 3, 'a', '❤️', 9,'!', 'hello']
        >>> new_list = [4, 5, 6]
        >>> filled_list.append(new_list) # you can append one list to another 
        >>> filled_list
        [1, 3, 'a', '❤️', 9,'!', 'hello', [4, 5, 6]] # new list gets added as a single element
        >>> len(filled_list)
        8
        ```
    
    - list.pop(): remove the element from the end of the list and return it, decreasing list length by 1. Can also give an index to use to remove item. i.e. list.pop(index)
        ```py
        >>> filled_list.pop()
        [4, 5, 6]
        >>> filled_list.pop(2)
        'a'
        ```
    
    - list.remove(elem): searches for first instance of elem in list and removes it. Does not return removed item.
        ```py
        >>> filled_list.remove(3)
        >>> filled_list
        [1, '❤️', 9, '!', 'hello']
        ```
    - list.extend(list2): adds all elements in list2 to end of list one by one. Different from append which will add all of list2 as one element at end of list1
        ```py
        >>> filled_list.extend(new_list)
        >>> filled_list
        [1, '❤️', 9, '!', 'hello', 4, 5, 6]
        ```
    
    - min(list), max(list): finds the smallest and largest element in list
        ```py 
        >>> new_list = [4, 5, 6]
        >>> min(new_list)
        4
        >>> max(new_list)
        6
        ```
    - load a list with data: a common way to load a list with data, is to start with an empty list, then loop over some sort of data, and then fill the list with items from the data at each iteration of the loop.
        ```py
        lst = []
        for i in range(10):
            lst.append(i)
        print(lst)
        ```

    - We can also use list comprehensions to fill a list with data with one line of code. Comprehensions enable us to fill a collection such as another list.
        ```py
        >>> lst = [i for i in range(10)]
        >>> lst
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> even_list = [elem for elem in lst if elem % 2 == 0 and elem != 0] # you can add conditionals to comprehenions


**Dictionaries**
Dictionaries are used to store date in key:value pairs. Dictionaries are written in curly brackets. Dictionary items are ordered, changeables and does not allow duplicates. An analogy that can help understand how dictionaries work is like a phone book that has various telephone numbers and the names of the owners. Each name and telephone number can be thought of as a key/value pair, where the name is the key and the number is as the value.

- Dictionary Operations
    - Creating a dictionary
        ```py
        >>> empty_dict = {}
        >>> phone_dict = {"Priscilla": 123, "Yvonne": 456}
        ```
    - Add a key/value pair to a dictionary: dict[key] = value
        ```py
        >>> phone_dict["Bernard"] = 789
        >>> phone_dict
        {'Priscilla': 123, 'Yvonne': 456, 'Bernard': 789}
        ```

    - Acessing a dictionary value using key
        ```py
        >>> phone_dict["Yvonne"]
        123
        ```

    - len(dict): count the number of key/value pairs in a dictionary
        ```py
        >>> len(phone_dict)
        3
        ```
    - dict.keys() returns an interable of all keys in dictionary which can be looped over to get each key.
    - dict.values() returns an interable of all values in dictionary which can be looped over to get each value.
    - dict.items() returns an interable of key/value pairs
    ```py
    >>> phone_dict.keys()
    dict_keys(['Priscilla', 'Yvonne', 'Bernard'])
    >>> phone_dict.values()
    dict_values([123, 456, 789])

    # using for loops
    >>> for key in phone_dict.keys():
    ...    print(key)
    Priscilla
    Yvonne
    Bernard
    ```

**Strings**
A python string stores text as a sequence of individual characters in quotation marks.

- String operations
    - len(string): returns lenght of a string, which is the number of individual characters in string
    - str(integer): convert an int to string
    - int(string): convert a string to an int
    - string indexing: works same as list indexing

- Formatting strings
The string.format() function is a handy way to convert values and format them into a string

- String join: ''.join(lst) takes a list of string parameters and joins it to one big string.
    ```py
    >>> ''.join(['e', 'x', 'c', 'e', 'l'])
    'excel'
    ```





## What is Pandas
### DataFrame Operations
- Read data
- operations and agregate functions
- groupby
- np.where with pandas