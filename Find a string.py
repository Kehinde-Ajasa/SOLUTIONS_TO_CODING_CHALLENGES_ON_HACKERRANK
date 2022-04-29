string = input('Enter main string: ')
sub_string = input('Enter substring: ').strip()

def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        new_string = string[i:(i + len(sub_string))]
        if new_string == sub_string:
            counter += 1
    return counter

count = count_substring(string, sub_string)
print(count)