def swap_case(s):
    new_string = []
    for i in s:
        if i.islower() == True:
            new_string.append(i.upper())
        elif i.isupper() == True:
            new_string.append(i.lower())
        else:
            new_string.append(i)
    return ''.join(new_string)
String = 'adebayo afolabi'
result = swap_case(String)
print(result)