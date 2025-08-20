n = int(input("Enter a number:"))
temp = n 
s=0

while n > 0:
    rem = n % 10
    s = (s * 10 ) + rem 
    n = n // 10

if ( temp == s ):
    print("Palindrome")
else :
    print("Not a palindrome")
