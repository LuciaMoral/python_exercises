# sorting dicts

points = { "Jill": 10, "Jack": 8, "Jim": 12, "Jane": 5}

# sorting by key

#.items() returns a tuple
points1 = dict(sorted(points.items(), key = lambda x:x[0]))
print(points1)

# sorting by values
points2 = dict(sorted(points.items(), key = lambda x:x[1]))
print(points2)



#key function: to modify the sorting process

# for a tuple:
tuple1 = ((1, "a"), (4, "s"), (3, "z"), (2, "r"))

sorted_tuple = sorted(tuple1)
print(sorted_tuple)
# sort the 2nd value
def second_value(element):
    return element[1]

sort_by_element = sorted(sorted_tuple, key=second_value)
print(sort_by_element)