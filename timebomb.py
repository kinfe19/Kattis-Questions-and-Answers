d = ['**** ** ** ****', '  *'*5, '***  *****  ***', '***  ****  ****',
 '* ** ****  *  *', '****  ***  ****', '****  **** ****',
  '***  *  *  *  *', '**** ***** ****', '**** ****  ****']


from math import ceil
l = [input() for i in range(5)]

ln = ceil(len(l[0]) / 4)
p = ['' for i in range(ln)]

for _ in range(5):
    for i in range(ln):
        j = i*4
        if i == 0:
            j = 0
        k = j+3
        if i==ln-1:
            v = l[_][j:k]
            v += ' '*(3-len(v))
            p[i] += v
            

        else:
            p[i] += l[_][j:k]


try:
    v = ''.join([str(d.index(i)) for i in p])
    if int(v) % 6==0:
        print('BEER!!')
    else:
        print('BOOM!!')
except:
    print('BOOM!!')