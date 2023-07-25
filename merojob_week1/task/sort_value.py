data = {
    "A": "4",
    "B": "1",
    "C": "2",
    "D":"0",
    "E":"-12",
}
print(data.items())
sorted_data = dict(sorted(data.items(),key=lambda item:item[1]))
print(sorted_data)