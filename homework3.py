calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()

def is_contains(string, spisok):
    count_calls()
    for el in spisok:
        if string.lower() == el.lower():
            return True
    return False
]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)