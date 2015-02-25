# Change PROG_NAME to path to wildebeest move generator executable
PROG_NAME = "cat"

VALID_PIECES = "SOEJCGTXHZWKPBRsoejcgtxhzwkpbr."

def is_valid(board):
    """
    Proper format for a board is 12 lines in the following format:
        line 1) 'W' or 'B'
        lines 2-9) 8 characters from VALID_PIECES list
        lines 10-12) integers
    """
    # Remove trailing new lines
    board = board.rstrip('\n')

    # Split board into lines
    lines = board.split('\n')

    # Remove newline from end of lines
    lines = [line[:-1] if line.endswith('\n') else line for line in lines]

    # Check that there are the correct number of lines in the board
    if len(lines) != 12:
        return False

    # Check that first line is either 'W' or 'B'
    if lines[0] not in ('W', 'B'):
        return False
    
    for line in lines[1:9]:
        # Check that the line is 8 characters long
        if len(line) != 8:
            return False

        # Check that each line is only composed of valid pieces
        if any(c not in VALID_PIECES for c in line):
            return False

    # Check that the last three lines are integers
    try:
        int(lines[9])
        int(lines[10])
        int(lines[11])
    except ValueError:
        return False

    return True


