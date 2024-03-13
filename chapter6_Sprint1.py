num1= int(input("Enter First number"))
num2= int(input(" Enter second number"))

try:
    ans=num1/num2
    print(' Answer = ',ans)

except:
    print ("Cannot divide number by 0. Yse another number")



data = [[4,6,3,6],[59,2,67,4],[34,9],[33,6,8],44,2,7,9,3,7,1]

for lists in data:
    try:
        print(lists[3])
    except IndexError:
        print("No 3rd index in data list")


          
