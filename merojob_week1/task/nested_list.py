list_data = [1, [2, [3, 4, [5, 6], 7], 8], 9, 10, 11, 12, 13, 14, 15, 16]
number = int(input("Enter the index for flat list:"))
flat_list = []

def nested(data, index):
    for element in data:
        if type(element) is list:
            if index == 1:
                flat_list.extend(element)
            else:
                nested(element, index - 1)
        else:
            flat_list.append(element)

nested(list_data, number)
print(flat_list)

