def power (base,pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result
print(power(3,2))
