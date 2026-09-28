def linearSearch(li, searchEle):
  for ind in range(0, len(li)):
    if(searchEle == li[ind]):
      return ind
  else:
    return -1
  
li = [12, 45, 65, 79, 99]

ele = int(input('enter element to find:'))

res= linearSearch(li, ele)

if(res != -1):
  print(f' {ele} is present at index {res}.')
else:
  print(f'{ele}, is not present in the list.')
