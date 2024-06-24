"""
Project Name: P1: Yondu Udonta
Author: Cody Behling
Course: CS1400-X01

This program is supposed to help divide up the shares of plunder to Yondu Udonta and Peter Quill's crew.
Yondu's share, Peter's share, and the rest of the crew's shares are different amounts.
Any extra units will be put into a separate RBF.

Aside from simply the applications of the concepts we've been learning, the biggest thing I learned was:
Don't overthink things! I spent more time than I should've trying to figure out how to properly calculate shares.
But this is the final draft of my program once I was able to get it all figured out.

Users will enter two inputs:
1) The number of crew members needing a cut and
2) The amount of units needing to be divvied out.
The program will then make several calculations and ultimately print four outputs:
1) Yondu's share
2) Peter's share
3) The crew members' shares
4) The RBF funds
If inputs are too low or high, the program will print error messages to the user as needed.
"""


def main():

    """
    Program starts here.
    """
    try:
        # (1) replace pass with your code
        # user inputs
        reavers = int(input("How many total Reavers are in the crew? "))
        units = int(input("How many total units were plundered? "))

    except ValueError:
        print("Enter postive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # pre-cut calculations
    preCut = (int(reavers) - 2) * 3
    preRemainder = int(units) - int(preCut)

    # manager cut calculations
    yonduInitial = int(preRemainder * 0.13)
    postYondu = int(preRemainder) - int(yonduInitial)
    peterInitial = int(postYondu * 0.11)
    postPeter = int(postYondu) - int(peterInitial)

    # final cut calculations
    crewFinal = int(postPeter) // int(reavers)
    rbfFinal = int(postPeter) % int(reavers)
    yonduFinal = int(yonduInitial) + int(crewFinal)
    peterFinal = int(peterInitial) + int(crewFinal)

    # program outputs
    print("Yondu's share: " + str(yonduFinal) + " units")
    print("Peter's share: " + str(peterFinal) + " units")
    print("Crew members' shares: " + str(crewFinal) + " units each")
    print("RBF funds: " + str(rbfFinal) + " units")


if __name__ == "__main__":
    main()
