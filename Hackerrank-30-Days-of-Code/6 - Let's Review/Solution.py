# Enter your code here. Read input from STDIN. Print output to STDOUT

NumOfLines = int(input())               # taking first input 2


for j in range(NumOfLines):             # makes sure we take all the lines as n
    
    s = input()                         # taking 1st and 2nd line
    evens, odds = '',''

    for i in range(len(s)):
        if i % 2 == 0:
            evens += s[i]
        else:
            odds += s[i]

    print(evens, odds)  
