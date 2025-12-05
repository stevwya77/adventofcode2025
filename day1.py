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
    curr_count = 0
    # separate direction and turn value
    direction = step[0]
    turn_val = int(step[1:])

    # left, decrease dial value
    if direction == 'L':
        dial_pos = dial_pos - turn_val
        if dial_pos < 1 and abs(dial_pos) != turn_val:
            curr_count += 1
        curr_count += (abs(dial_pos) // 100)
        
    # when right, increase dial value
    if direction == 'R':
        dial_pos = dial_pos + turn_val
        curr_count += dial_pos // 100
    dial_pos = dial_pos % 100
    return dial_pos, curr_count

'''
Assign dial position per turn and returns rotation counts 
resulting in zero.
'''
def move_dial(rotations):
    # initialize dial at 50
    dial_pos = 50
    count = 0
    for step in rotations:
        step_count = 0
        # update position per turn
        dial_pos, step_count = turn(step, dial_pos)
        count += step_count
    return count

def main():
    door_pwd = move_dial(read_rotations(PUZZLE_INPUT))
    print(f'Door Password: {door_pwd}')

if __name__ == '__main__':
    main()