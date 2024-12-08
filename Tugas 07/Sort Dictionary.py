my_dict = {'b': 2, 'a': 3, 'c': 1}

# Sorting by keys
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'a': 3, 'b': 2, 'c': 1}

my_dict = {'b': 2, 'a': 3, 'c': 1}

# Sorting by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'c': 1, 'b': 2, 'a': 3}

# Sorting by keys in reverse order
sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print(sorted_by_keys_desc)  # Output: {'c': 1, 'b': 2, 'a': 3}

# Sorting by values in reverse order
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_values_desc)  # Output: {'a': 3, 'b': 2, 'c': 1}

my_dict = {'b': 2, 'a': 3, 'c': 1}

# Custom sort: length of the key (though not typical for dictionaries)
sorted_by_custom = dict(sorted(my_dict.items(), key=lambda item: len(item[0])))
print(sorted_by_custom)  # Output: {'b': 2, 'a': 3, 'c': 1}

# Jika tidak mau buat variable baru
for key, value in sorted(my_dict.items(), key=lambda item: item[1]):
    print(key, value)
