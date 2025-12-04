filepath = "turns.txt"

def turn(step, dial_pos):
    turn_val = int(step[1:])
    if step[0] == 'L':
        dial_pos = dial_pos - turn_val
        if dial_pos < 0:
            if len(str(dial_pos)) > 2:
                dial_pos = (dial_pos % 100)
    if step[0] == 'R':
        dial_pos = dial_pos + turn_val
        if dial_pos > 99:
            dial_pos = dial_pos % 100
    return dial_pos

def read_rotations(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        stripped = [line.strip() for line in lines]
        return stripped

def move_dial(rotations):
    dial_pos = 50
    count = 0
    for step in rotations:
        dial_pos = turn(step, dial_pos)
        if dial_pos == 0:
            count += 1
    return count

print(move_dial(read_rotations(filepath)))