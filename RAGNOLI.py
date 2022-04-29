while True:
    import string

    # LOWER PART
    try:
        size = int(input('Enter the amount of alphabeths you want: '))

        left_hand_side_length = size
        width = ((size + (size - 1)) * 2) - 1
        List = list(string.ascii_lowercase)
        count = 1
        counter = 0
        sliced_list = (List[:size])
        sliced_list.reverse()
        reference_number = 1
        referenced_number = 0

        # UPPER PART

        while reference_number != size:
            new_list = (sliced_list[counter:referenced_number])
            new_list.reverse()
            Rangoli_pattern = (sliced_list[:reference_number] + new_list)
            reference_number += 1
            referenced_number += 1
            print(('-'.join(Rangoli_pattern).center(width, '-')))

        # LOWER PART

        while size > 0:
            new_list = (List[count:left_hand_side_length])
            Rangoli_pattern = (sliced_list[:size] + new_list)
            count += 1
            size -= 1
            print(('-'.join(Rangoli_pattern).center(width, '-')))
        redo = input('Y/N:' )
        if redo == 'y':
            break
        else:
            continue
    except ValueError:
        print('not found')