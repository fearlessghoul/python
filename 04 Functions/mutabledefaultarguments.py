def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] (unexpected)
