# this is tested and works in linux kubuntu terminal
# it does not work in IDLE

# import sleep to allow pausing
from time import sleep

# import only system and name from os
from os import system, name 

# define our clear function
def clear():

 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 
# print out some text
print('hello geeks\n'*10)
 
# sleep for 1 seconds after printing output
sleep(1)
 
# now call function we defined above
clear()

print('and one last print')
