#1. Why are functions advantageous to have in your programs?
#ANS: Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.
#2. When does the code in a function run: when it's specified or when it's called?
#ANS: when it's called
#3. What statement creates a function?
#ANS: "def" statement creates a function
# 4. What is the difference between a function and a function call?
#ans: A function consists of the def statement and the code in its def clause.
# and  A function call is what moves the program execution into the function and the function call evaluates to the function's return value.
#5. How many global scopes are there in a Python program? How many local scopes?
#ans: There is one global scope and a local scope is created whenever a function is called.
#6. What happens to variables in a local scope when the function call returns?
#ans: When a function returns, the local scope is destroyed and all the variables in it are forgotten.
#7. What is a return value? Can a return value be part of an expression?
#ans: A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.
#8. If a function does not have a return statement, what is the return value of a call to that function?
#ans: If there is no return statement for a function, its return value is None.
#9. How do you make a function variable refer to the global variable?
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc() 
#10. What is the data type of None?
#ANS: The None keyword is used to define a null value, or no value at all.
import areallyourpetsnamederic 
#ANS: ModuleNotFoundError: No module named 'areallyourpetsnamederic'
#12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
#ANS: from spam import bacon()
# 13. What can you do to save a programme from crashing if it encounters an error?
#ans:If an error occurs in a program, we don’t want the program to unexpectedly crash so. Instead, error handling can be used to check why the error occurred and later exit the process that caused the error.
#example: Exception handling using try - except
#14. What is the purpose of the try clause? What is the purpose of the except clause?
#ans: The try block lets you test a block of code for errors.
#The except block lets you handle the error.
