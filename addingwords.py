d  = {}
while True:
    try:
        total = input().split()
        command, *query = total
        if command == "def":
            d[query[0]] = int(query[1])

        elif command == "calc":
            query = query[:-1]
            z = ' '.join(total)
            try:
                l = []
                op = '+-'
                for i in query:
                    if not i in op:
                        l.append(str(d[i]))
                    else:
                        l.append(i)
                c =''.join(l)
                ans = eval(c)
                dd = {b:a for a,b in d.items()}
                print( z[5:] +' '+dd[ans])
            except:
                print(z[5:] + " unknown")
        elif command == "clear":
            d={}
            dd={}
    except:
        break