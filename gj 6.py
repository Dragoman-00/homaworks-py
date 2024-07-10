#1
def print_params(a = 1, b = 'строка', c = True):
     print(a,b,c)

print_params()
print_params(b = 25)
print_params(c=[1,2,3])
#2
values_list = "Терка", 5, True
values_dict = {"a": 2, "b": True, "c": 4}
print_params(*values_list)
print_params(**values_dict)
#3
values_list_2 = 2, True
print_params(*values_list_2, 42)


