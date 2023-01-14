c = 0
for _ in range(int(input())):
    s = input().lower()
    if 'pink' in s:
        c+=1
    elif 'rose' in s:
        c+=1
print(c if c !=0 else "I must watch Star Wars with my daughter")
    
