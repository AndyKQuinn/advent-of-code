def get_second_answer():
    with open("inputs.txt", "r") as file:
        inputFile = file.read().strip().splitlines()

        currentNumber = 50
        countOfZeroes = 0

        for line in inputFile:
            direction = line[0]
            clicks = int(line[1:])

            if direction == "R":
                for _ in range(clicks):
                    currentNumber += 1
                    if currentNumber % 100 == 0:
                        print("ZERO FOUND at: " + str(currentNumber))
                        countOfZeroes += 1
            elif direction == "L":
                for _ in range(clicks):
                    currentNumber -= 1
                    if currentNumber % 100 == 0:
                        print("ZERO FOUND at: " + str(currentNumber))
                        countOfZeroes += 1
        print("Count of zeroes: ", countOfZeroes)


def main():
    # get_first_answer()
    get_second_answer()


if __name__ == "__main__":
    main()
