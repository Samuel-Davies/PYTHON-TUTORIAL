# is don't really understand why the else block doesn't match the 
position = -1

def search(list,n):

   l = 0    #lower bound
   u = len(list)-1

   while l <= u:    # upper Bound
       mid = (l + u) // 2

       if list[mid] ==n:
           globals()['position']= mid
           return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid -1
    return False

        
            


list = [4,7,8,12,45,99,10234,546,346,3456,675,35,5433,55]

n= 45


if search(list, n):
    print('found at ', position,)
else:
    print('Not Found')