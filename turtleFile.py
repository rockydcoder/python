''' TurtleControl.py
Ask the user for commands for a turtle. The turtle
excutes that command. Our supported commands are:
Q for quit   Example Q
L for Left   Example L 90
R for right  Example R 45
F for forward Example F 200
U for UP
D for Down
H for Heading
B for Back
C for Circle
S for Speed
'''
from turtle import *
def parseCommand (tinput):
    param = 0
    cmd = ""
    if tinput:
        tinput = tinput.upper()  # make our data uppercase
        tinput = tinput.strip() # remove trailing whitespace
        cmdList = tinput.split() # split the tinput string into list
        cmd = tinput[0]  # cmd = first item in List

        if len (cmdList) > 1:  # do we have a second value?
            param = float( cmdList[1]) # store it in 'param'
        return cmd,param

def main():
    leo = Turtle()
    leo.shape ("turtle")
    while True:
        tinput = raw_input("TurtleControl; Command for Leonardo?")
        cmd,param = parseCommand(tinput)
        # handle our cmd with a big list of if elif statements.

        if cmd == "Q":   # exit the while loop
            break
        elif cmd == "L": # turn left
            leo.left(param)
        elif cmd == "R": # turn right
            leo.right(param)
        elif cmd== "F": # go forward
            leo.forward (param)
        elif cmd== "C": # go up
            leo.circle (param)
            

if __name__=="__main__":
    main()
    print("Done!")