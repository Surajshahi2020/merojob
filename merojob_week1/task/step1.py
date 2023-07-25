def calculation():
    num = input("Enter the number:")
    data = {
        "100": 50,
        "50": 100,
    }.get(num,"Invalid input")
    print(data)
calculation()    