import os
import math

debug = False

PWD = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = 'pass-scan.txt'

START_ROW = 0
END_ROW = 127

START_COL = 0
END_COL = 7

def printif(message, debug=False):
    if (debug):
        print(message)

def process_token(token, row_start, row_end, col_start, col_end):
    new_row_start = row_start
    new_row_end = row_end
    new_col_start = col_start
    new_col_end = col_end

    if (token == 'F'):
        new_row_end = row_end - math.floor((row_end - row_start) / 2)
    elif (token == 'B'):
        new_row_start = row_start + math.floor((row_end - row_start) / 2)
    elif (token == 'L'):
        new_col_end = col_end - math.floor((col_end - col_start) / 2)
    elif (token == 'R'):
        new_col_start = col_start + math.floor((col_end - col_start) / 2)
    elif (token == ''):
        printif(f'Token ignored {token}', debug)
    else:
        print(f'Unkown token {token}')

    return (new_row_start, new_row_end, new_col_start, new_col_end)

def derive_seat_id(passport):
    row_start = START_ROW
    row_end = END_ROW
    col_start = START_COL
    col_end = END_COL

    printif(f'Passport: {passport}', debug)
    tokens = list(passport)
    for token in tokens:
        printif(f'Token: {token}', debug)
        (row_start, row_end, col_start, col_end) = process_token(token, row_start, row_end, col_start, col_end)
        printif(f'Ranges - Row: ({row_start}, {row_end}) Col: ({col_start}, {col_end})', debug)

    printif(f'Final Ranges - Row: ({row_start}, {row_end}) Col: ({col_start}, {col_end})', debug)
    row = min([row_start, row_end])
    col = max([col_start, col_end])
    printif(f'Row: {row}', debug)
    printif(f'Col: {col}', debug)

    return ((row * 8) + col, row, col, passport)

# Load file
path = os.path.join(PWD, FILE_NAME)
pass_file = open(path, "r").readlines()
passports = list(map(lambda x: x.strip(), pass_file))

max_seat_id = 0
max_seat_row = 0
max_seat_col = 0
max_seat_pass = 'X'
seat_ids = []

for p in passports:
    (seat_id, row, col, passport_log) = derive_seat_id(p)
    printif(f'Seat ID: {seat_id} | {passport_log} ({row}, {col}) using {row} * 8 + {col}', debug)
    seat_ids.append(seat_id)
    if (seat_id > max_seat_id):
        max_seat_id = seat_id
        max_seat_row = row
        max_seat_col = col
        max_seat_pass = passport_log

print(f'Max SeatID: {max_seat_id} | {max_seat_pass} ({max_seat_row}, {max_seat_col}) using {max_seat_row} * 8 + {max_seat_col}')