print('Python Syntax:')

print('The program below is the basic python syntax')
print('print(\'Hello World\')\n')

print('Python Indentation:') 
print('Indentaion in python is very importent becasue if the indentation is not right\
 then the output can diff. or interpreter can thorw an error.')
print('For example:')
print('\
if 5 == 5:\n\
\tprint(\'True\')\n')
print('Here the indentation show that the \'print\' Keyword is a part of if statement.\
 If the condition is true then the print statement will be executed')

#Python Comments

print("Python Comments")

print('\nComments are basically used for in-code documentation. They are \
comment statements are not executed by interpreted.\n\nThere are two types of comments in python.\
\n1.Single Line Comment:\nSingle line comment is used to comment a single line.For eg.\n')

print('#This a comment')
print('print(\'Hello World\')\n')

print('2. Multi-Line Comment:\nMulit-ine comment is used to comment a Multiple lines.For eg.\n')

print('\'\'\'This a \ncomment\'\'\'')
print('print(\'Hello World\')\n')

#Pytohn Variables

print('\nPython Variables:')

print("Rules for python Variables")

print("1. Variable must start with an alphabet or underscore(_).\
\n2. Make sure a variable doesn't contain any spacing or special characters in between\
 name of the varibale.\n3.Python variables are case-sensitive.\
\n4.\'A\' and \'a\' are diff. variables.\n\n")

print('Creating Variables:')
print('Python has no command for declaring a variable.\
\nA variable is created the moment you first assign a value to it.For Example:\n')
print('x = 5\ny = \"John\"')

print('Variables do not need to be declared with any particular type, and can \
even change type after they have been set.\n')

print('Casting:\n')
print('If you want to specify the data type of a variable, this can be done with casting.\n')

print('x = str(3) #x will be \'3\'')
print('y = int(3) #x will be 3')
print('z = float(3) #x will be 3.0')

print('\nGet the type:\n')
print('x = 5\ny = \"John\"')
print('type(x)')
print('type(y)\n')

print('Output:')
print('integer\nstring\n')

#Global Variables
print('Global Variables:\n')

print('Variables that are created outside of a function \
are known as global variables.\nGlobal variables can be used\
 by everyone, both inside of functions and outside.')

print('x = \"Hallo!\"')
print("def myfunc():\n\tprint(x + \',Ich bin Keshav Swami\')")
print('\nmyfunc()\n\n')

print('The global Keyword:\n')
print('Normally, when you create a variable inside a function, that variable is local, \
and can only be used inside that function. To create a global variable inside \
a function, you can use the global keyword.')
print('For Eg.:')
print("def myfunc():\n\tglobal x\n\tx = \"Hallo!,\"")
print('\nmyfunc()')
print('\nprint(x + \'Ich bin Keshav Swami\')')

#Data Types
print('\n\nData Types:')
print('Python has the following data types built-in by default, in these categories:\n')
print('Text type:\tstr')
print('Numeric types:\tint, float, complex')
print('sequence types:\tlist, tuple, range')
print('Mapping type:\tdict')
print('Boolean type:\tbool')

print('\n\nType Conversion:\n')
print('You can convert from one type to another with the int(), float(), and complex() methods:')
print('x = 1 #int\ny = 2.8 #float\nz = 1j #complex')
print('\n#convert from int to float:')
print('a = float(x)')
print('\n#convert from float to int:')
print('a = int(y)')
print('\n#convert from int to complex:')
print('a = complex(x)')
print('\nNote: You cannot convert complex numbers into another number type.\n\n')

#Python Casting:

print('Python Casting:')
print('\nCasting in python is therefore done using constructor functions:')
print('\t1.int() - constructs an integer number from an integer literal, a float literal \n\
\t\t\t(by removing all decimals), or a string literal (providing the string represents a whole number).\
\n\tfloat() - constructs a float number from an integer literal, a float literal or a \n\
\t\t\tstring literal (providing the string represents a float or an integer).\
\n\tstr() - constructs a string from a wide variety of data types, including \n\
\t\t\tstrings, integer literals and float literals.')
