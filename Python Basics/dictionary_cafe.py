""" Reference list and dictionaries for stock and prices """
menu_list = ['red bush', 'earl grey', 'mocha', 'late']
stock_dictionary = {
    'red bush': 20,
    'earl grey': 31,
    'mocha': 24,
    'late': 14}
price_dictionary = {
    'red bush': 3.20,
    'earl grey': 2.10,
    'mocha': 4.50,
    'late': 3.80}

# Calculate the value of each
for item in menu_list:
    ITEM_VALUE = stock_dictionary[item] * price_dictionary[item]
    # Print the value of each menu item
    print(f"The total value of {item} in stock is £{ITEM_VALUE:.2f}.")
