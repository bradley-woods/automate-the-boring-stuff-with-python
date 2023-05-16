# Automate the Boring Stuff with Python
# Chapter 4 - Lists: Comma Code

# Comma separated string function
def comma(list_items):
    list_string = ""
    if list_items == []:
        return "Enter a populated list"
    else:
        for i in range(len(list_items)-1):
            item = list_items[i]
            list_string = f"{list_string}{item}, "
        list_string = f"{list_string}and {list_items[-1]}"
        return list_string


# Prints "apples, bananas, tofu, and cats"
print(comma(['apples', 'bananas', 'tofu', 'cats']))

# Test case where empty list [] is passed
print(comma([]))
