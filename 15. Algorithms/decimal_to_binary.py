# Convert a decimal number to its binary equivalent
# 11 == 1011

def decimal_to_binary(num):
    # return bin(num)
    binary = []
    while num > 0:
        binary.insert(0, str(num % 2))
        num = num // 2
    return ''.join(binary)


print(decimal_to_binary(11))
