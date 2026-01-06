# Grocery List
# Outputs a sorted grocery list with item counts

grocery_list = {}

while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        print()
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item}")
        break
