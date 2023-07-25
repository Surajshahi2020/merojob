dict = {
    "name": "Suraj shahi",
    "age": "25",
}

swap = {v: k for k, v in dict.items()}

values = input("Enter the key or value: ")

if values in dict:
    result = dict[values]
else:
    result = swap.get(values, "Not found")

print(result)
