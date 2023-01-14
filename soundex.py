dd = {'B': '1', 'C': '2', 'D': '3',
 'F': '1', 'G': '2', 'J': '2',
 'K': '2', 'L': '4', 'M': '5', 'N': '5', 
 'P': '1', 'Q': '2', 'R': '6', 'S': '2', 'T': '3',
 'V': '1',  'X': '2',  'Z': '2'}
while 1:
    try:
        s = input()
        k = ' '
        for i in s:
            if i in dd:
                if k[-1] != dd[i]:
                    k += dd[i]
            else:
                k+=' '
        print(k.replace(' ', ''))
    except:
        break