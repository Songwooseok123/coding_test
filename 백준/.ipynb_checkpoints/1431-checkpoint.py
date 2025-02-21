n= 5
arr = ['ABCD',
'145C',
'A',
'A910',
'Z321']
n = int(input())

def sums(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr.sort(key = lambda x:(len(x), sums(x), x))

for i in arr:
    print(i)
