import os

def parse_rule(rule: str):
    (freq_range, letter) = rule.split(' ')
    (low, high) = freq_range.split('-')
    return (int(low), int(high), letter)

def count_letter_occurance(letter: str, message: str):
    count = 0

    for m in list(message):
        count += (1 if m == letter else 0)

    return count

def validate(rules_password: str):
    valid = False

    try:
        (rule, password) = rules_password.split(': ')
    except ValueError:
        print('Issue')

    (low, high, letter) = parse_rule(rule)

    count = count_letter_occurance(letter, password)
    if (count >= low and count <= high):
        valid = True

    return valid

PWD = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(PWD, 'rules-and-corrupt-passwords.txt');

rules_password_array = open(path, 'r').read().split('\n')
# remove last item in array (EOF)
rules_password_array = rules_password_array[:-1]

valid_rules_count = 0
invalid_rules_count = 0
for rules_password in rules_password_array:
    is_valid = validate(rules_password)

    if (is_valid):
        valid_rules_count += 1
    else:
        invalid_rules_count += 1

print(f'Count of valid rules  : {valid_rules_count}')
print(f'Count of invalid rules: {invalid_rules_count}')