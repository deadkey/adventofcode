# Test how well regular chatgpt solves the problem (of course after submitting my own solution), it was fast, it had a small error that it also counted the antennas as antinodes, but it was a good solution.

def parse_input(input_map):
    """Parse the input map into a list of antennas with their positions and frequencies."""
    antennas = []
    for y, row in enumerate(input_map.splitlines()):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas


def find_antinodes(antennas, width, height):
    """Find all unique antinode locations."""
    antinodes = set()
    # Group antennas by their frequency
    freq_groups = {}
    for x, y, freq in antennas:
        freq_groups.setdefault(freq, []).append((x, y))

    # Process each frequency group
    for freq, positions in freq_groups.items():
        n = len(positions)
        for i in range(n):
            x1, y1 = positions[i]
            for j in range(i + 1, n):
                x2, y2 = positions[j]

                # Check if the distance between two antennas satisfies the resonance condition
                dx, dy = x2 - x1, y2 - y1

                # Compute positions for potential antinodes
                antinode1_x, antinode1_y = x1 - dx, y1 - dy
                antinode2_x, antinode2_y = x2 + dx, y2 + dy

                # Add valid antinodes within bounds
                if 0 <= antinode1_x < width and 0 <= antinode1_y < height:
                    antinodes.add((antinode1_x, antinode1_y))
                if 0 <= antinode2_x < width and 0 <= antinode2_y < height:
                    antinodes.add((antinode2_x, antinode2_y))

    return antinodes


def count_antinodes(input_map):
    """Count unique antinode locations within the map bounds."""
    antennas = parse_input(input_map)
    height = len(input_map.splitlines())
    width = len(input_map.splitlines()[0])
    antinodes = find_antinodes(antennas, width, height)


    return len(antinodes)


# Example usage
input_map = open("real.txt", 'r').read().strip('\n')


result = count_antinodes(input_map)
print("Number of unique locations with an antinode:", result)
