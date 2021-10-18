upper,lower,digit_odd,digit_even = [],[],[],[]
for i in input():
    if i.isupper():
        upper.append(i)
    if i.islower():
        lower.append(i)
    if i.isdigit():
        if int(i) % 2 == 0:
            digit_even.append(i)
        if int(i) % 2 != 0:
            digit_odd.append(i)

print(*sorted(lower),*sorted(upper),*sorted(digit_odd),*sorted(digit_even),sep='')