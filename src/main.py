##
## ELEVATOR PROJECT, 2021
## elevator
## File description:
## main
##

import sys

#This is the usage of the program

HELP = "USAGE = The first argument is the execution binary of the program\n"\
    "The second argument is the command (either goUp or goDown)\n"\
    "The third argument is the number of arguments to go up or down\n"\
    "EXECUTION = python3 elevator [goUp or goDown] [nb of floores]\n"\

def atoi(str): #With this function, we convert an string to an integer (atoi = array to int)
    res = 0
    for i in range(len(str)):
        res = res * 10 + (ord(str[i]) - ord('0'))
    return res

def elevator(argv):
    n = atoi(argv[2])
    
    if argv[2] > '0' and argv[2] < '9': #Here we say that the elevator cannot go in invalid directions (0, letters, special characters)
        if argv[1] == "goUp":
            print("The elevator goes up", n, "floors !\n")
        elif argv[1] == "goDown":
            print("The elevator goes down", n, "floors !\n") #Here, if we ask to go up, we go up, if not, we go down
    else:
        print("The elevator can only go up or down !\n") #If there is an error in the command, we print an error

def main(argv, argc):
    if argc == 2 and argv[1] == "-help":
        print(HELP)
        return 0
    if argc != 3:
        print("There can only be 3 arguments !\n") #If there is more than 3 arguments or less than 3 arguments, this is an error
        return -1
    elevator(argv) # We call the elevator function !
    return 0