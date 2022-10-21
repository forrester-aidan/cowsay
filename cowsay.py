from heifer_generator import HeiferGenerator  # imports the HeiferGenerator class into this file
import sys  # imports the sys module into this file


def main():  # Main method
    message = ""
    cowImage = HeiferGenerator.cowImages[0]

    for index in range(len(sys.argv)):  # Loops through the list of arguments
        if index == 0:  # Excludes file name
            continue
        elif index == 1 and sys.argv[index] == "-l":  # Checks for the -l command
            availableCows = ""
            for cowName in range(len(HeiferGenerator.cowNames)):
                if cowName + 1 == len(HeiferGenerator.cowNames):
                    availableCows += HeiferGenerator.cowNames[cowName]
                else:
                    availableCows += HeiferGenerator.cowNames[cowName] + " "

            print("Cows available: " + availableCows)  # Prints the cows available
            quit()
        elif index == 1 and sys.argv[index] == "-n":  # Checks for the -n command in the index of 1
            if sys.argv[index + 1] != "heifer" and sys.argv[index + 1] != "kitteh":  # Rules out other cows
                print("Could not find %s cow!" % sys.argv[index + 1])
                quit()
            else:
                if sys.argv[index + 1] == "kitteh":
                    cowImage = HeiferGenerator.cowImages[1]  # Changes the cow image
        else:
            if index - 1 == 1 and sys.argv[index - 1] == "-n":  # Removes the type of cow from the message, if stated
                continue
            else:
                if index + 1 == len(sys.argv):
                    message += sys.argv[index]
                else:
                    message += sys.argv[index] + " "
    print(message)  # Prints the message and cow image
    print(HeiferGenerator.quoteLines + cowImage)


if __name__ == '__main__':
    main()
