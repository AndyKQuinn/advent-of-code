def count_matching_neighbors(grid, row, col, target="@"):
    """Count adjacent positions with a specific value"""
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    count = 0

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] == target:
                count += 1

    return count


def puzzle_one():
    print("Processing puzzle 1...")

    with open("inputs.txt", "r") as f:
        grid = [line.strip() for line in f if line.strip()]

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        total_count = 0

        for row in range(rows):
            for col in range(cols):
                current = grid[row][col]

                if current == "@":
                    adjacent_count = count_matching_neighbors(
                        grid, row, col, target="@"
                    )
                    print(f"Position ({row},{col}) - Adjacent @: {adjacent_count}")

                    if adjacent_count >= 4:
                        print("Position invalid - adjacent count: ", adjacent_count)
                        continue
                    else:
                        total_count += 1
                        print("Position valid, count incremented")

        print(f"Total @ within reach of forklift: {total_count}")


def move_paper_roll(grid: list[str], rows: int, cols: int, total_moved=0):
    count_of_updated = 0
    updated_grid = [list(row) for row in grid]

    for row in range(rows):
        for col in range(cols):
            current = updated_grid[row][col]

            if current == "@":
                adjacent_count = count_matching_neighbors(
                    updated_grid, row, col, target="@"
                )

                if adjacent_count >= 4:
                    continue
                else:
                    count_of_updated += 1

                    updated_grid[row][col] = "."

    updated_grid_str = ["".join(row) for row in updated_grid]

    if count_of_updated > 0:
        print(
            f"Updated {count_of_updated} rolls this pass, total so far: {total_moved + count_of_updated}"
        )
        return move_paper_roll(
            updated_grid_str, rows, cols, total_moved + count_of_updated
        )
    else:
        return updated_grid_str, total_moved


def puzzle_two():
    print("Processing puzzle 2...")

    with open("inputs.txt", "r") as f:
        grid = [line.strip() for line in f if line.strip()]

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        _, total_moved = move_paper_roll(grid, rows, cols)
        print(f"Total rolls moved: {total_moved}")


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
