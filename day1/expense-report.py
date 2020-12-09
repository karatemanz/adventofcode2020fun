import os

def to_int(toInt: str):
    variable = None

    try:
        variable = int(toInt)
    except ValueError:
        variable = None

    return variable

PWD = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(PWD, 'expense-report.txt');

report_array = list(filter(lambda y: y != None, map(lambda x: to_int(x), open(path, 'r').read().split('\n'))))
report_array.sort();

answer = None;

for i in range(len(report_array)):
    for j in range(len(report_array)):
        combo = report_array[i] + report_array[j]
        if (combo == 2020):
            print(f'Pair is: ({report_array[i]}, {report_array[j]}) = {combo}!')
            answer = report_array[i] * report_array[j]
            break
    if (answer != None):
        break

print(f'Answer 1 is: {answer}')

answer = None;

for i in range(len(report_array)):
    for j in range(len(report_array)):
        for k in range(len(report_array)):
            combo = report_array[i] + report_array[j] + report_array[k]
            if (combo == 2020):
                print(f'Set is: ({report_array[i]}, {report_array[j]}, {report_array[k]}) = {combo}!')
                answer = report_array[i] * report_array[j] * report_array[k]
                break
        if (answer != None):
            break
    if (answer != None):
        break

print(f'Answer 2 is: {answer}')