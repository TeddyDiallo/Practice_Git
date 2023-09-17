def sum_list(mylist):
    sum = 0
    for i in mylist:
        sum += i
    return sum 

def product_list(mylist):
    product = 1
    for i in mylist:
        product *= i
    return product 

def reverse_list(mylist):
    result = []
    j = -1
    for i in range(len(mylist)):
        result.append(mylist[j])
        j -=1
    return result