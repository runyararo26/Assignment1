c_list = [0, 20, 37, 100]
to_f = lambda c: c * 9/5 + 32
f_list = list(map(to_f, c_list))
print(f_list)