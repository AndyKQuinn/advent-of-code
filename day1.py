with open("inputs.txt", "r") as file:
    string = file.read()

    currentNumber = 50
    countOfZeroes = 0

    for line in string.splitlines():
        if line.startswith("L"):
            numberToDecrement = int(line[1:])

            currentNumber = (currentNumber - numberToDecrement) % 100
            print(currentNumber)

            if currentNumber == 0:
                countOfZeroes += 1
        else:
            numberToIncrement = int(line[1:])
            currentNumber = (currentNumber + numberToIncrement) % 100
            print(currentNumber)

            if currentNumber == 0:
                countOfZeroes += 1

    print("Total count of zeroes: ", countOfZeroes)
