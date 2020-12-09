import os

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
        if(all(x in p for x in REQUIRED_TOKENS)):
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