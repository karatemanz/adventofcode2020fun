import os
import re

PWD = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = 'passport-scanning.txt'

######
#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID) (optional)
######
REQUIRED_TOKENS = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid', 'hcl']
OPTIONAL_TOKENS = ['cid']

EYE_COLOR_TOKENS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

########
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.
########
def validate_rules(passport, debug=False):
    tokens = passport.split(' ')
    results = []

    for token in tokens:
        outcome = False
        (rule, value) = token.split(':')

        outcome = validate_rule(rule, value)

        if (debug):
            print(f'Rule: {rule} | Value: {value} | Validity: {outcome}')

        results.append(outcome)

    return all(results)

def validate_rule(rule, value):
    if (rule == 'byr'):
        outcome = len(value) == 4 and (int(value) >= 1920 and int(value) <= 2002)
    elif(rule == 'iyr'):
        outcome = len(value) == 4 and (int(value) >= 2010 and int(value) <= 2020)
    elif(rule == 'eyr'):
        outcome = len(value) == 4 and (int(value) >= 2020 and int(value) <= 2030)
    elif(rule == 'hgt'):
        if ('cm' in value):
            num_only = value.replace('cm', '')
            outcome = (int(num_only) >= 150 and int(num_only) <= 193)
        elif ('in' in value):
            num_only = value.replace('in', '')
            outcome = (int(num_only) >= 59 and int(num_only) <= 76)
        else:
            outcome = False
    elif(rule == 'hcl'):
        outcome = ('#' in value and value[0] == '#') and (len(value) == 7 and re.match("^[A-Fa-f0-9]*$", value[1:]) != None)
    elif(rule == 'ecl'):
        outcome = len(value) == 3 and (any(e in value for e in EYE_COLOR_TOKENS))
    elif(rule == 'pid'):
        outcome = len(value) == 9 and isinstance(int(value), int)
    elif(rule == 'cid'):
        # ignored / accepted regardless
        outcome = True

    return outcome

def parse_passport_input(passport_file: str):
    passports = list(map(lambda x: x.strip(), passport_file))
    passport_strings_array = []

    partial_passport = []
    for p in passports:
        if (p == ''):
            passport_strings_array.append(" ".join(partial_passport))
            partial_passport = []
            continue
        partial_passport.append(p)

    return passport_strings_array

def validate_passports(passport_strings, debug=False):
    valid_count = 0
    invalid_count = 0
    all_creds = []

    for p in passport_strings:
        valid = False
        if(all(x in p for x in REQUIRED_TOKENS) and validate_rules(p, debug)):
            valid_count += 1
            valid = True
        else:
            invalid_count += 1

        if (debug):
            all_creds.append(aggregate_cred(p, valid))

    return (valid_count, invalid_count, all_creds)

def aggregate_cred(passport, valid):
    cred = {}
    tokens = passport.split(' ')

    for token in tokens:
        for req in REQUIRED_TOKENS:
            pair = token.split(':')
            if (pair[0] == req):
                cred[req] = pair[1]

        for opt in OPTIONAL_TOKENS:
            pair = token.split(':')
            if (pair[0] == opt):
                cred[opt] = pair[1]

    print(f'Passport: {passport} | Valid: {valid}')
    return cred

###
# Start execution
###
debug = False

# Load file
path = os.path.join(PWD, FILE_NAME)
passport_file = open(path, "r").readlines()

passport_strings = parse_passport_input(passport_file)
(valid_passports_count, invalid_passports_count, all_passports_as_cred) = validate_passports(passport_strings, debug)

print(f'Valid passports: {valid_passports_count}!')
print(f'Invalid passports: {invalid_passports_count}!')
# if (debug):
#     print(f'All passports: {all_passports_as_cred}')