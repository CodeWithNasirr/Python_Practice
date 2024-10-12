#  How do you sort a dictionary by its values?

# my_dict = {'a': 3, 'b': 1, 'c': 2}
# sort=dict(sorted(my_dict.items(),key=lambda item : item[1]))
# print(sort)

#In this code we are not using sort,sorted in build functions 
def bubble_sort(arr):
    num=len(arr)
    for i in range(num):
        for j in range(0,num-i-1):
            # print(j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    item=[]
    for x in arr:
        if x not in item:
            item.append(x)
    return item



list=[21,322,4,1,4,34,6,432,6423,34,6,74]
x=bubble_sort(list)
print(x)