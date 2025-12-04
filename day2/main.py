import csv

from duplicate_finder import find_duplicate_subsequences


def first_puzzle():
    with open("inputs.csv", "r") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=",")

        listOfBadIDs = []

        for listOfIDs in csvReader:
            for rangeOfIDs in listOfIDs:
                startIDstr, endIDstr = rangeOfIDs.split("-")
                startID = int(startIDstr)
                endID = int(endIDstr)

                for element in range(startID, endID):
                    if len(str(element)) % 2 != 0:
                        print("Skipping...")
                        continue
                    else:
                        print("Processing...")
                        firstHalf = str(element)[: len(str(element)) // 2]
                        secondHalf = str(element)[len(str(element)) // 2 :]
                        if firstHalf == secondHalf:
                            listOfBadIDs.append(element)

    sumOfBadIDs = sum(listOfBadIDs)
    print("Puzzle 1 results:")
    print("Length of bad IDs: ", len(listOfBadIDs))
    print("Sum of all bad IDs: ", sumOfBadIDs)


def second_puzzle():
    with open("inputs.csv", "r") as csvfile:
        csvReader = csv.reader(csvfile, delimiter=",")

        listOfBadIDs = []

        for listOfIDs in csvReader:
            for rangeOfIDs in listOfIDs:
                startIDstr, endIDstr = rangeOfIDs.split("-")
                startID = int(startIDstr)
                endID = int(endIDstr)

                print("StartID: " + str(startID) + " EndID: " + str(endID))
                for integer in range(startID, endID):
                    patterns = find_duplicate_subsequences(integer)
                    if patterns:
                        print(f"Duplicate found in {integer}: {patterns}")
                        listOfBadIDs.append(integer)

    sumOfBadIDs = sum(listOfBadIDs)
    print("Puzzle 2 results:")
    print("Length of bad IDs: ", len(listOfBadIDs))
    print("Sum of all bad IDs: ", sumOfBadIDs)


if __name__ == "__main__":
    first_puzzle()
    second_puzzle()
