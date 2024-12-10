# Test how well o1 solves the problem (of course after submitting my own solution), it took it 1 min 4 s but it solved it in the first try.

def count_antinodes(input_map):
    lines = input_map.splitlines()
    height = len(lines)
    width = len(lines[0]) if height > 0 else 0

    # Parse antennas from the map
    antennas = []
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch != '.':
                antennas.append((x, y, ch))

    # Group antennas by frequency
    freq_groups = {}
    for x, y, freq in antennas:
        freq_groups.setdefault(freq, []).append((x, y))

    antinode_positions = set()

    # For each frequency group, find antinodes from each pair of antennas
    for freq, positions in freq_groups.items():
        n = len(positions)
        for i in range(n):
            x1, y1 = positions[i]
            for j in range(i + 1, n):
                x2, y2 = positions[j]
                dx = x2 - x1
                dy = y2 - y1

                # Antinodes for this pair
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                # Add if within bounds
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinode_positions.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinode_positions.add(antinode2)

    # Include all antenna locations, as they can also count as antinodes
    #for x, y, _ in antennas:
    #    antinode_positions.add((x, y))

    return len(antinode_positions)


# Example usage:
input_map = open("real.txt", 'r').read().strip('\n')

result = count_antinodes(input_map)
print("Number of unique locations with an antinode:", result)
