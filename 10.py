tuple_original = (1, 2, 4, 5)

tuple_modified= tuple_original[:2]+(3,)+tuple_original[2:]

print(tuple_modified)