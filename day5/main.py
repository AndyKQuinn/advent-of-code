# looking for fresh or spoiled ingredients
# db schema:
#   ingredientIDs: range(int)
#   blank line
#   integers


def puzzle_one():
    print("Processing puzzle 1...")

    with open("inputs.txt", "r") as f:
        content = f.read().strip()

        sections = content.split("\n\n")
        print("Sections: ", sections)

        fresh_ingredient_ranges = []
        for line in sections[0].split("\n"):
            start, end = line.split("-")
            fresh_ingredient_ranges.append((int(start), int(end)))

        ingredients = [int(line) for line in sections[1].split("\n")]
        count_of_fresh_ingredients = 0

        print(f"Number of ranges: {len(fresh_ingredient_ranges)}")
        print(f"Number of integers: {len(ingredients)}")
        print(f"First range: {fresh_ingredient_ranges[0]}")
        print(f"First integer: {ingredients[0]}")

        # go through each ingredient and find if it lands between a fresh_ingredient range
        # if so, add as fresh

        for ingredient in ingredients:
            for fresh_ingredients in fresh_ingredient_ranges:
                print("Fresh Ingredients: ", fresh_ingredients)

                start_num = fresh_ingredients[0]
                end_num = fresh_ingredients[1]

                if ingredient >= start_num and ingredient <= end_num:
                    print(
                        f"Found fresh value: {ingredient} inbetween {start_num} and {end_num}"
                    )
                    count_of_fresh_ingredients = count_of_fresh_ingredients + 1
                    break

        print("Count of fresh ingredients: ", count_of_fresh_ingredients)


def puzzle_two():
    # know all of IDs that fresh ingredient ranges consider to be fresh
    print("Processing puzzle 2...")

    with open("inputs.txt", "r") as f:
        content = f.read().strip()

        sections = content.split("\n\n")

        fresh_ranges_orig = []

        for line in sections[0].split("\n"):
            start, end = line.split("-")
            fresh_ranges_orig.append((int(start), int(end)))

        # sort ranges by start position
        fresh_ranges_sorted = sorted(fresh_ranges_orig, key=lambda x: x[0])

        # merge overlapping ranges
        fresh_ranges_merged = []
        for current_range in fresh_ranges_sorted:
            # if list is empty or current doesn't overlap with last merged range
            if not fresh_ranges_merged or fresh_ranges_merged[-1][1] < current_range[0]:
                fresh_ranges_merged.append(current_range)
            else:
                # overlaps - extend the last merged range
                last_range = fresh_ranges_merged[-1]
                fresh_ranges_merged[-1] = (
                    last_range[0],
                    max(last_range[1], current_range[1]),
                )

        # loop through the end results and count the numbers between the merged ranges
        total_count = 0
        for merged_range in fresh_ranges_merged:
            start, end = merged_range
            count = end - start + 1
            total_count += count

        print(f"Total count across all merged ranges: {total_count}")
        print(f"Number of merged ranges: {len(fresh_ranges_merged)}")


if __name__ == "__main__":
    # puzzle_one()
    puzzle_two()
