filepath = "turns.txt"


'''
Extract rotations from provided document in txt file.
'''
def read_rotations(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        stripped = [line.strip() for line in lines]
        return stripped

'''
Update the dial value indicated by direction
and assigned turn value per step. Any value beyond
100 is disregarded.
'''
def turn(step, dial_pos):
    # separate direction and turn value
    direction = step[0]
    turn_val = int(step[1:])
    # left, decrease dial value and reset
    if direction == 'L':
        dial_pos = dial_pos - turn_val
        dial_pos = dial_pos % 100
    # when right, increase dial value and reset
    if direction == 'R':
        dial_pos = dial_pos + turn_val
        dial_pos = dial_pos % 100
    return dial_pos

'''
Assign dial position per turn and stores rotation 
count with result of zero.
'''
def move_dial(rotations):
    dial_pos = 50
    count = 0
    for step in rotations:
        dial_pos = turn(step, dial_pos)
        if dial_pos == 0:
            count += 1
    return count

print(move_dial(read_rotations(filepath)))