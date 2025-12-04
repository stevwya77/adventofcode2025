PUZZLE_INPUT = "turns.txt"

'''
Extract rotations from provided document in txt file.
'''
def read_rotations(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        stripped = [line.strip() for line in lines]
        return stripped

'''
Calculate step from initial position to next by indicated rotation
direction and value. Returned value measures distance from 100 to 
ensure position remains within bounds.
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
Assign dial position per turn and returns rotation counts 
resulting in zero.
'''
def move_dial(rotations):
    # initialize dial at 50
    dial_pos = 50
    count = 0
    for step in rotations:
        # update position per turn
        dial_pos = turn(step, dial_pos)
        # count turn results pointing at 0
        if dial_pos == 0:
            count += 1
    return count

def main():
    door_pwd = move_dial(read_rotations(PUZZLE_INPUT))
    print(f'Door Password: {door_pwd}')

if __name__ == '__main__':
    main()