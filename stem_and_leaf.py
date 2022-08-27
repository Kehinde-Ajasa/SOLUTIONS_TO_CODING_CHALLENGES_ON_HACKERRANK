"""This code is used to get the stem and leaf of a particular number
the code goes further in sorting out the stem and leaf to a dictionary
Inspired by MAT 161"""

print('If numbers greater than one please separate by space')
while True:

    try:
        def convert_to_integer():
            """Accept user input and return a list
            of all inputs in integer format."""
            user_input = input('Please enter you values:))')
            split_input = user_input.split()
            main_data = list()
            for i in split_input:
                main_data.append(int(i))  # appending the integer value of the input
            return main_data


        def get_power(single_value):
            """Using result from any particular function
            to produce the power to be divided by."""
            temp_list = list()
            for i in str(single_value):
                temp_list.append(i)
            if len(temp_list) > 1:
                power = 10 ** (len(temp_list) - 1)
            else:
                power = 10  # for numbers that are only in the unit
            return power


        def get_stem_and_leaf():
            """Creating a dictionary,
            The dictionary would have a key of stem
            and it would have a value of leaf"""
            stem_and_leaf = dict()
            for values in convert_to_integer():
                stem, leaf = values // get_power(values), values % get_power(values)
                if stem in stem_and_leaf:
                    stem_and_leaf[stem].append(leaf)  # auto creation of key and adding a value
                else:
                    stem_and_leaf[stem] = [leaf]  # adding the values of key as a preset list
            return stem_and_leaf


        print(get_stem_and_leaf())
    except ValueError:
        print('Invalid input check your input and try again')

    try_again = input('Would you like to try again(Y/N): ').lower()
    if try_again == 'y':
        continue
    else:
        print('Thank You')
        break
