# Day 3
# Batteries joltage a value from 1-9
# Each line of digits represents a single bank of batteries
# Within each bank, turn on exactly two batteries
# Joltage equals the number formed by the digits, like 12345, enable 2 and 4, number is 24
# Find largest possible joltage for each bank


def main():
    print("Processing...")
    total_charge = 0

    with open("inputs.txt", "r") as file:
        banks = file.read().splitlines()

        for battery_bank in banks:
            highest_digit_found = None
            for digit in range(9, 0, -1):
                digit_str = str(digit)
                if digit_str in battery_bank:
                    highest_digit_found = digit_str
                    break

            if highest_digit_found is None:
                print(f"Bank {battery_bank}: No valid digits found")
                continue

            first_pos = battery_bank.index(highest_digit_found)

            remaining_digits = battery_bank[first_pos + 1 :]

            second_digit_found = None
            for digit in range(9, 0, -1):
                digit_str = str(digit)
                if digit_str in remaining_digits:
                    second_digit_found = digit_str
                    break

            # If no second digit found to the right, the second number is 9
            # and we search to the left for the highest digit (excluding 9)
            if second_digit_found is None:
                digits_before = battery_bank[:first_pos]
                for digit in range(8, 0, -1):  # Start from 8, not 9
                    digit_str = str(digit)
                    if digit_str in digits_before:
                        second_digit_found = digit_str
                        break
                # Form number as second_digit + 9
                largest_number = (second_digit_found + highest_digit_found) if second_digit_found else (highest_digit_found + highest_digit_found)
                print(
                    f"Bank {battery_bank}: Found {highest_digit_found} at end (pos {first_pos}), searched left for {second_digit_found}, largest number = {largest_number}"
                )
            else:
                # Form the largest number
                largest_number = highest_digit_found + second_digit_found
                print(
                    f"Bank {battery_bank}: First digit {highest_digit_found} at pos {first_pos}, second digit {second_digit_found} from remaining, largest number = {largest_number}"
                )

            total_charge += int(largest_number)

    print("Total charge: ", total_charge)


if __name__ == "__main__":
    main()
