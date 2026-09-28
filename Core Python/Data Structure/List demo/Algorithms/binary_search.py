def binarySearch(li, searchEle):
  beg = 0 
  end = len(li) -1
  
  while(beg <= end):
  #print('beg:', beg)
  #print('end:', end)
  
    mid = (beg+end)//2
  #print('mid:', mid)
  #print('search_el:', searchEle)
  #print('mid_ele:', midele)

    if(searchEle == li[mid]):
      return mid
    
    elif(searchEle < li[mid]):
      end = mid - 1
    elif(searchEle > li[mid]):
      beg= mid +1
  else:
    return -1
li = [10, 20 , 30 ,40 , 50 , 60]
ele = int(input('enter element to find:'))

res= binarySearch(li, ele)

if(res != -1):
  print(f' {ele} is present at index {res}.')
else:
  print(f'{ele}, is not present in the list.')
