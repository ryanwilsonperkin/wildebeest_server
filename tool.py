import os
import subprocess
import tempfile

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
    board = board.rstrip()

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

def get_results(board):
    """
    Runs the wildebeest move generating executable and returns results.
    - Creates a temporary directory
    - Saves board contents to file in temporary directory
    - Runs the move generating executable on the board file
    - Copies the generated files into memory
    - Removes all generated files
    - Removes temporary directory
    - Returns list of contents of generated files
    """

    # Create a new temp directory
    tmp_dir = tempfile.mkdtemp()
    print tmp_dir

    # Save board.txt to temp directory
    board_filename = os.path.join(tmp_dir, 'board.txt')
    with open(board_filename, 'w') as board_file:
        board_file.write(board)

    # Change current working directory to temp directory
    orig_wd = os.curdir
    os.chdir(tmp_dir)

    # Call wildebeest move generating executable
    ret_val = subprocess.call([PROG_NAME, board_filename])
    if ret_val != 0:
        return None

    # Delete board.txt from temp directory
    os.remove(board_filename)

    # Get contents of new boards from temp directory and delete the files
    new_boards = []
    for new_board_filename in os.listdir(tmp_dir):
        with open(new_board_filename) as new_board_file:
            lines = [line for line in new_board_file]
            new_boards.append(''.join(lines))
        os.remove(new_board_filename)

    # Change back to original working directory
    os.chdir(orig_wd)

    # Delete temp directory
    os.rmdir(tmp_dir)

    return new_boards
