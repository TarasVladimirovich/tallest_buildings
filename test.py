

while True:
    file_input = input("Please enter file path:\n")
    # file_input = '/Users/taraskoshletskyi/Downloads/2020run.txt'
    if not file_input:
        continue
    num_of_lines = 0
    empty_lines = 0
    line_with_z = 0
    line_with_and = 0
    with open('/Users/taraskoshletskyi/Downloads/2020run.txt') as file:
        for line in file:
            num_of_lines += 1
            if not len(line.strip()):
                empty_lines += 1
            if 'z' in line:
                line_with_z += 1
            if 'and' in line:
                line_with_and += 1
    result = f'{"total lines":<20}: {num_of_lines:<2}\n' \
             f'{"empty lines":<20}: {empty_lines:<2}\n' \
             f'{"lines with z":<20}: {line_with_z:<2}\n' \
             f'{"lines with and":<20}: {line_with_and:<2}\n'
    print(result)
    choise = input("Do you want more:\n").lower()
    if 'no' == choise:
        break

