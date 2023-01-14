
x = None
for i in range(int(input())):
    k = int(input())
    s = input()
    l = [input() for j in range(k)]
    if 'pea soup' in l and 'pancakes' in l:
        if x == None:
        	x = s
    
if x == None:
    print('Anywhere is fine I guess')
else:
	print(x)