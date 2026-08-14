# Wap to check whether the number is palindrome or not
#return True if palindrome & return False if not palindrome 


def chkPalindrome(num):
  temp = num
  rev = 0
  
  while(temp > 0):
    dig = temp % 10
    rev = rev * 10 + dig
    temp = temp // 10
    
  if(num == rev):
    return True
  else: 
    return False
  
n = int(input('Enter number:'))
print(chkPalindrome(n))