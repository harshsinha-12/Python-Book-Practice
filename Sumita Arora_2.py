# Immutable: int, float, bool, string, tuples
# The variable names are stored as reference to a value object.
# Each time you change the value of the variable reference address changes.

p = 5
q = p
r = 5
print(f"p,q,r: {p,q,r}")
p = 10
r = 7
q = r
print(f"p,q,r: {p,q,r}")

# Mutable: list, set, dictionary changed at place

lst = [1,2,3,4,5]
print(lst)
lst[1] = 10
print(lst)

# Typecasting....explicit type conversion
tup = tuple(lst)
print(tup)
print(lst)