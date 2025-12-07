# Day 3
# Batteries joltage a value from 1-9
# Each line of digits represents a single bank of batteries
# Within each bank, turn on exactly two batteries
# Joltage equals the number formed by the digits, like 12345, enable 2 and 4, number is 24
# Find largest possible joltage for each bank


def puzzle_one():
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
                largest_number = (
                    (second_digit_found + highest_digit_found)
                    if second_digit_found
                    else (highest_digit_found + highest_digit_found)
                )
                print(
                    f"Bank {battery_bank}: Found {highest_digit_found} at end (pos {first_pos}), searched left for {second_digit_found}, largest number = {largest_number}"
                )
            else:
                largest_number = highest_digit_found + second_digit_found
                print(
                    f"Bank {battery_bank}: First digit {highest_digit_found} at pos {first_pos}, second digit {second_digit_found} from remaining, largest number = {largest_number}"
                )

            total_charge += int(largest_number)

    print("Total charge: ", total_charge)


def puzzle_two():
    total_charge = 0

    with open("inputs.txt", "r") as file:
        banks = file.read().splitlines()

        for battery_bank in banks:
            selected_digits = []
            current_pos = -1  # Start before the first position

            for n in range(12):
                # Calculate the maximum index we can search up to
                # After selecting this digit, we need (11 - n) more digits
                # So we need at least (11 - n) positions remaining after this one
                # For n=0 (first digit): max = len - 12 = 100 - 12 = 88
                # For n=11 (last digit): max = len - 1 = 99 (can search to the very end)
                max_search_index = len(battery_bank) - 12 + n
                search_start = current_pos + 1

                # Find the highest digit in the valid range
                # Reset to 9 for each new digit position
                found_digit = False
                for digit in range(9, 0, -1):
                    digit_str = str(digit)

                    # Search from current_pos + 1 to max_search_index
                    for index in range(search_start, max_search_index + 1):
                        if battery_bank[index] == digit_str:
                            selected_digits.append(digit_str)
                            current_pos = index
                            print(
                                f"Digit {n + 1}/12: Found {digit_str} at index {index} (searched {search_start} to {max_search_index})"
                            )
                            found_digit = True
                            break

                    if found_digit:
                        break

                if not found_digit:
                    print(f"Error: Could not find digit {n + 1}")
                    break

            if len(selected_digits) == 12:
                result = "".join(selected_digits)
                result_int = int(result)
                total_charge += result_int
                print(f"Final 12-digit number: {result}")
            else:
                print(f"Warning: Only found {len(selected_digits)} digits")

    print(f"\nTotal charge: {total_charge}")


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
