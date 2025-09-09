DATA TYPES

    str(varible)
#This converts any data type to a String.
    int(varible)
#This converts any data type to a Integer, or a number you can do math with.
    float(varible)
#This converts any data type to a Float, or a decimal you can do math with.
    Boolean(varible)
#This converts any data type to a True or False.
    Comment
#This is a line of code that doesnt run.
    
PRINT

    print(data)
#This prints out whatever is in the parehthesis.
    print('''string''')
#This allows you to indent a print staement onto new lines.
    print(f"string{}")
#This allows you to concatenate valribles inside a print statement.
    print("string"+varible+"String")
#This is another way to concatenate varibles inside a print statement.

VARIBLES

    Varible=input("string")
#This lets you get a input from a user.#This IS ALWAYS STRING.
    Varible=Value
#This declares a varible and assigned it to the given value.
    Varible3=Varible2+Varible1
#adds the values of two vairbles to make a new one.(Cannot be string or a Boolean)

MATH
    c=a+b
#form of addition that creates a new varible
    c=a-b
#form of subtraction that creates a new varible
    c=a*b
#form of Multiplication that creates a new varible
    c= a/b 
#This form of Division will always return a decimal or float.
    c= a % b
#This returns the remainder.(Modulus)
    +=, *=, -=, /=,
#You can use This to use an operation on a value quicker.EX. Total += 10(#This adds 10 to the varible Total.)
    x=math.ceil()
#This Rounds up to The next whole value
    x=math.floor()
#this Rounds down ro the next whole number
    math.pi
#this lets you use pi
    math.sqrt()
#This lets you find the Square root
    pow(value, value)
#Muiply a number by a power, first num is base, second is power.
    
FORMATTING

    \n 
#This makes a new Line in print.
    \t
#This creates a tab indent in print.
    \”
#This prints out quotes.
    \\
#This will print out slashes.

ANSI CODES
    \033[0m
#This resets the format back to normal.
    \033[1m
#This makes text bold.
    \033[3m
#This makes text Italic.
    \033[4m
#This makes text bold red.
    \033[1;32m
#This makes text bold green.
    \033[1;33m
#This makes text bold yellow.
    \033[1;34m
#This makes text bold blue.
    \033[1;35m
#This makes text bold magenta.
    \033[1;40m
#This makes text have a black background.

STRING METHODS

    string.lower()
#This will make string all lowercase.
    string.upper()
#This will make string all uppercase.
    string.strip()
#This will delete any extra spaces.
	string.insert(num,value)
#This inserts the new value at the beginning of the list. 
    type()
#This will output what type of data your variable is.
    string.replace(“value”,”replacement”)
#This will replace characters in a string.
    String[start:stop:step]
#This will slice pieces of text.(using index numbers)
    variable=string1[len(string)::-1]
#This will reverse slice the string, staring from the back.
    len(string)
#This will return how many items are in a string. (starting at 1)
    string.find(“character”)
#This will help find an index number of a character in an instance. 
    string.rfind(“character”)
#This will find the index number of a character in an instance furthest from the start.
    varible=“Word” in variable1
#This will check if a word is in a string. It will output a True or False. (Boolean)
    LENGTH()
#This finds the number of characters in a string
    char.islower()
#this will check to see if a string/charcter is lowercase
    char.isupper()
#this will check to see if a string/charcter is uppercase
    char.isalnum()
#this will check to see if a charcter is a number.
CONCATENATION
         
    string.format()
#This will allow any data type to be inputted into a string. The string must have { }. You can add more than one by using commas inside of the parentheses. The words will be replaced in order of the brackets. (first word will go into the first pair of brackets)

LISTS/DICTIONARIES/TUPLES/STACKS
         
    string.split()
#This will separate text into word separated by commas and brackets. (A list.)
    varible=[“text”,”text”]
#A list of items separated by commas.
    list=[int(n) for n in input(“print statement”).split()]
#This will allow an input of numbers to be split into a list.
    List[0]
#This can be used to access an item in a list.(indexed starting at 0)
    listname[0]+0
#Use This to do any type of math with integers in a list.
	del list[index]
#use this to delete an item in a list by index
    list.append(“item”)
#This adds an item to the end of the list.
    list.extend([2,3,4,5,6])
#You can use This to extend a list with another, if you just use a string then it will put each character into that list.
    list.insert(2,”word”)
#You can insert an item into an index part of a list.
    list.remove(“string”)
#List can be used to remove the first instance of a string in a list.
	list.reverse()
#this will reverse the list.
    variable=list.pop(0)
#This is used to pull and item but still have assigned to a value.
    len(list)
#To find how many items are in a list.
    list[1]=”string”
#To replace an item in a list.
    rows=[1,2,3]
    cols=["red","orange","yellow","green"]
    for i in rows:
         col=[]
         for j in cols:
            col.append(j)
         list.append(col)
#This is how we turn two 1D lists into one 2D lists by running thru “cols” thru the number “rows” and adding it to a new list named “col”
    list.sort()
#To sort alphabetically or numerically.
    list.sort(reverse=True)
#To sort alphabetically or numerically in reverse.
    round()
#Use This to round a number.
    Dictionary={key:value,}
#This is how a dictionary is set up, a list structure with curly braces. Each item is a pair with a Key and a Value. 
    print(Dictionary[key])
#This will print out a specific key in a dictionary.
    dictionary[key]=newvalue
#This will change a key and value in a dictionary, if there is no key with #This name it will add #This item to the dictionary. 
    Dictionary.pop(key)
#This will remove any item in the dictionary. (the entire pair.)
    print(len(dictionary))
#This will print the length of the dictionary. Starts at 1.
    Tuple=(“item”,)
A tuple is an unchangeable list, they cannot be added to or subtracted from. 
    print(tuple[0])
#You can access items in a tuple just like a list or dictionary.
    varible="".join(list)
#this takes a list and makes it into one line of string
    list=list(varible1)
#this takes a varible and makes it into a list split up by character

IF STATEMENTS
         
    If x in variable:
	Code to run
#This give the computer instructions that tells a computer to do something if another thing happens. #This is followed by a condition. (x represents each item in a list.)
    If varible and varible:
#Returns true if both conditions are met.
    If variable or variable is met:
#Returns true if one variable is met.
    If not variable:
#Returns true if false, and vice versa.
    elif:
#This tells the computer what to do if a condition is met.(you can have as many of these as you want.)
    Else:
#This tells the computer what to do if the condition isn't met. (you can have one)
    If variable is in dictionary:
#This if statement will check if your variable is a key or value in your dictionary.
    If variable is in dictionary:
#This if statement will check if your variable is Not a key or value in your dictionary.
    For x in dictionary:
            print(x)
#This will print they keys in the dictionary.
    For x in (dictionary.values())
        print(x)
#This will print the values in the dictionary in a for loop.
    For x in (dictionary.items())
        print(x)
#This will print the Items/pairs in the dictionary in a for loop.

CONDITIONS

>
#greater than.
>=
#greater than or equal to.
<
#less than
<=
#less than or equal.
==
#equal to
!=
#not equal

LOOPS

For x in variable:
	Code to run
#This is for addressing each piece of data in a sequence.(list,dictionary, or tuple.)You can put a for loop inside of a for loop.(nested for loop)
    list=[“string” for i in variable]
#One line for loop.(outprints a list)
    List=[[j for j in variable] for i in range(rows)]
#One line nested for loop.(outprints a list)
    For x in range(0,0):
#This works to run through all those integers in the loop. #This will print a list if printed.
    For x in range(integer)
            varible = varible + integer 
#You can use #This to update an integer variable.
    for x in variable:
            If x in variable:
#You can put a if statement in a for loop.
    While variable == value:
#These can be used to iterate/ repeat a command while a condition is true. ANY TYPE OF OPERATOR CAN BE USED INSTEAD OF THE EQUALS
    For i in variable:
            For i in variable:
#Nested for loop, outer loop is slow and inner loop is faster.
    Rows
#This is when you have a variable set to equal multiple lists. Each list is 1 row (needed for a nested for loop)
    Columns
#This is when you have a variable set to equal multiple lists. Each item in one list counts as one column.([1,2,4]=3 columns])(needed for a nested for loop)
    my_list[i][j]
#This represents every item in every row and list. 
    variable=int
    list=[]
    For i in range(int):
            list.append(0)
#This creates a new list that is (int) elements long with append(0) value big. Assigns #This to list=[].
    For x in list:
            For x in dictionary:
                    Running code
#These for loops run through every value in a list, then line 2 checks if it's in the dictionary, then runs the bottom code.

FUNCTIONS

    def name():
            Code to run
#This defines a function so you can use multiple lines of code at one time.
    name()
#This is calling the function to use the code inside of it.
    Def name ()
            variable=data
#This is a local variable that can only be used in a function
    global
#This is a keyword that can be placed before a variable name to make a local variable global.

GIT REFERENCES


    git revert <sha>
    git push
#Safe undo of pushed commit

    git commit --amend -m "Better message"
#Fix last commit before push


    git restore --source=<sha> path/to/file
#Restore one file from a past commit

    git restore path/to/file
#Discard local changes (one file)


TEXT FILES/IMPORT FILES

    Variable=open(“textname.txt”,”r”)
#This opens a text file to read it 
    print(varible.read())
#This calls back to the variable that opened the file, reads it, and prints the result. 
    Variable.readline()
#This reads the first line in a read file.
    Variable.readlines()
#This reads the entire file.
    Import os
#this imports a .py file.
    os.path.function(path)
#This imports a function from an imported .Py file
    os.path.isfile(path)
#This specifies if the file exsits
    os.path.isdir(path)
#This specifies if the directory exsits
    os.path.remove(path)
#This removes the file from the directory
    os.path.basename(path)
#This returns the "basename of the file given
    os.peth.dirname(path)
#This returns the directory name of where the file is located.
    import sys
#Imports the computer system files.
    sys.path ['',
#This shows the automatic list python makes when you create a new .py file.
#This is all the directories it will use to search for modules when importing.
#Using the ['', on a new line will print the current directory.



DATE TIME LIBRARY

    import datetime
#This imports the datetime Library
    x=datetime.datetime.now()
# the current date and time down to the milisecond.
        x=datetime.datetime.today()
#The current date and time to the seconds. 
    print(x.strftime())
#formats the dattime into str and prints it.
    print(x.strftime("%X"))
#Prints the time
    print(x.strftime("%m"))
#Prints the current two digit month
    print(x.strftime("%d"))
#Prints the current two digit day
    print(x.strftime("%Y"))
#Prints the current Four digit Year.

TRY BLOCKS
#these are formatted like a loop.
    try:
#Tests code for errors
    except:
#Code to run if an error happens
    else:
#Code to run if no errors happens
    finally:
#Code to run regardless of any other blocks

OBJECT-ORIENTED PROGRAMMING

    class name:
#this creates a class, A blueprint for an object.
    def __init__(self, parameters):
#this initalizes the class and defines its parameters. There must be a self parameter.
    self.parameter1=parameter1
    self.parameter2=parameter2  
    self.parameter3=parameter3
#this sets up under wher ethe class is initalized. This takes each attribute and assigns
#it to itself.
    Varible=class(1,2,3)
#this creates an Object/Instance
    print(varible.attribte)
#this prints out the attribute assigned to the object.(you an also concatentate Varible.
#attribute inside a print statement.
    class.attribute=value
#Adds an attribute to a class OR changes an exsisting one by the same name.
    delattr(class, attribute)
#Removes an attribute.
    del class.sttribute
#deletes all values you have assigned to the attribute.

RECURSION

#a Recursion function will call itself until a condition is met.
    def Recursive_Funct(parameters):
        if base_condition:
            return result
        else:
            return result:
#There are two main parts of a Recursive Function.
#Base Case: The stoppung condition that prevents infinite looping:
#Recursive Case: The part of the function tha calls itself with modified parameters.


        
        
        
    




    




    




