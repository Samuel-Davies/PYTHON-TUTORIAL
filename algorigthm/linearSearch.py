
position = -1

def search(list,n):

    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['position'] = i
            return True
        i += 1
    return False


list = [5,8,4,6,9,2]

n= 3


if search(list, n):
    print('found at ', position,)
else:
    print('Not Found')