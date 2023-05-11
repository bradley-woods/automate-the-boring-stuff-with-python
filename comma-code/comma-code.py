# Automate the Boring Stuff with Python
# Chapter 4 - Lists

# Comma seperated string
def comma(list_items):
    list_string = ""
    for i in range(len(list_items)-1):
        item = list_items[i]
        list_string = f"{list_string} {item},"
    list_string = f"{list_string} and {list_items[-1]}"
    return list_string


# prints "apples, bananas, tofu, and cats"
print(comma(['apples', 'bananas', 'tofu', 'cats']))
