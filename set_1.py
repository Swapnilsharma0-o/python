my_set = { 1,2,3,43,4,5,5,6,7,7,7,8,8,8,8,"gaurav","Pune",
            ("dbda,hpcsa","diot","dac"),frozenset({"dbda,hpcsa","diot","dac"})
          }

#print(len(my_set))
my_subset1 = {100,200,300}
my_subset2 = {1,2,3,300}

# print(my_set) 

# print("len(s) -- Return the number of elements in set s (cardinality of s)")
# print(len(my_subset1))

# print("x in s --Test x for membership in s.")
# print(100 in my_subset1)
# print(frozenset({"dbda,hpcsa","diot","dac"}) in my_set)
# print(("dbda,hpcsa","diot","dac") in my_set)
# print("dbda" in my_set)
# print("Pune" in my_set)
# print(my_subset1)
# print(my_subset2)
# print(my_set)
# print(my_subset1.issubset(my_set))
# print(my_subset2.issubset(my_set))

# if both the elements present in the set then FALSE otherwise TRUE
# print("isdisjoint(other) --Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.")
# print(my_set.isdisjoint(my_subset1))
# print(my_set.isdisjoint(my_subset2))


# if both the elements present in the set then TRUE otherwise FALSE
# print(my_subset1)
# print(my_subset2)
# print(my_set)
# print(my_subset1.issubset(my_set))
# print(my_subset2.issubset(my_set))

# MAIN SET in the whole set
# print(my_set.issuperset(my_subset1))
# print(my_set.issuperset(my_subset2))

# union (join)
# print("return_val: ", my_subset1.union(my_subset2))
# print('actual set ' , my_subset1)

# intersection (common)
# print(my_subset1.intersection(my_subset2))

# # difference()
# print(my_subset1.difference(my_subset2))

# symmetric_difference
# it writes the only elements that are not present in both sets
# print(my_subset1.symmetric_difference(my_subset2))


# it copies the one set in another new empty set.
# my_copy_set = set()
# print(my_copy_set)
# my_copy_set = my_subset1.copy()
# print(my_copy_set)


print(my_subset1)
print(my_subset2)
# adds new elements to privious set  
# my_subset1.update(my_subset2)
# print(my_subset1)

# update th set and then interction (print common value)
# my_subset1.intersection_update(my_subset2)
# print(my_subset1)


# my_subset1.difference_update(my_subset2)
# print(my_subset1)
























