from functools import reduce 

listed = ["i","love", "you"]
upper = list(map(str.upper, listed))
concatenated_string = reduce(lambda x, y: x + y, upper)
print(concatenated_string)