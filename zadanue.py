calls = o
def count_calls():
    call = calls + 1
    global calls

def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()
