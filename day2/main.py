import csv


def main():
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
    print("List of bad IDs: ", sumOfBadIDs)


if __name__ == "__main__":
    main()
