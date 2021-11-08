# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
my_dict = dict()

for i in range(n):
    x = input().split()
    my_dict[x[0]] = x[1]

while True:
    try:
        key = input()
        
        if key in my_dict:
            print(key, '=', my_dict[key], sep='')
        else:
            print('Not found')
    except:
        break
