def product_except_self(input_tuple):
    result=[]
    total=1
    for num in input_tuple:
        total*=num
    for num in input_tuple:
        x=total//num
        result.append(x)
    return tuple(result)

# Example usage
original_tuple = (1, 2, 3, 4)
result = product_except_self(original_tuple)
print(result)  # Output: (24, 12, 8, 6)
