# WAP to check if a list contains a palindrome of elements. [1, 2, 3, 2, 1]
num = [1,2,2,1]
copy1= num.copy()
num.reverse()
if(copy1 == num):
    print("Yes, it contains elements of palindrome")
else:
    print("It does not contain elements of palindrome")