def ch(j):
    if(j=='a' or j=='A'):
        return '@'
    elif(j=='b' or j=='B'):
        return '8'
    elif(j=='c' or j=='C'):
        return '('
    elif(j=='d' or j=='D'):
        return '|)'
    elif(j=='e' or j=='E'):
        return '3'
    elif(j=='f' or j=='F'):
        return '#'
    elif(j=='g' or j=='G'):
        return '6'
    elif(j=='h' or j=='H'):
        return '[-]'
    elif(j=='i' or j=='I'):
        return '|'
    elif(j=='j' or j=='J'):
        return '_|'
    elif(j=='k' or j=='K'):
        return '|<'
    elif(j=='l' or j=='L'):
        return '1'
    elif(j=='m' or j=='M'):
        return '[]\/[]'
    elif(j=='n' or j=='N'):
        return '[]\[]'
    elif(j=='o' or j=='O'):
        return '0'
    elif(j=='p' or j=='P'):
        return '|D'
    elif(j=='q' or j=='Q'):
        return '(,)'
    elif(j=='r' or j=='R'):
        return '|Z'
    elif(j=='s' or j=='S'):
        return '$'
    elif(j=='t' or j=='T'):
        return "']['"
    elif(j=='u' or j=='U'):
        return '|_|'
    elif(j=='v' or j=='V'):
        return '\/'
    elif(j=='w' or j=='W'):
        return '\/\/'
    elif(j=='x' or j=='X'):
        return '}{'
    elif(j=='y' or j=='Y'):
        return '`/'
    elif(j=='z' or j=='Z'):
        return '2'
    else:
        return j
    
j=input()
t=list(j)
v=[]
for i in t:
    v.append(ch(i))
g=''.join(v)
print(g)
