n=int(input())
for i in range(n):
    p=input()
    if p=='P=NP':
        print('skipped')
    else:
        print(eval(p))
