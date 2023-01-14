def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
t = int(input())
case = 1
for _ in range(t):
    st1 = list(input())
    st2 = list(input())

    one_zero = []
    tag_one = []
    zero_one = []
    tag_zero = []
    for i in range(len(st1)):
        if st1[i]=='1' and st2[i] == '0':
            one_zero.append(i)
        elif st1[i] == '?':
            if st2[i] == '1':
                tag_one.append(i)
            else:
                tag_zero.append(i)
        elif st1[i] == '0' and st2[i] == '1':
            zero_one.append(i)
            
    counter = 0
    flag = False
    while one_zero != []:
        x = one_zero[0]
        if zero_one != []:
            y = zero_one[0]
            swap(st1, x, y)
            one_zero = one_zero[1:]
            zero_one = zero_one[1:]
            counter += 1
        elif tag_one != []:
            y = tag_one[0]
            st1[y] = '0'
            swap(st1, x, y)
            one_zero = one_zero[1:]
            tag_one = tag_one[1:]
            counter += 2
        else:
            flag = True
            break
    if flag:
      counter = -1
    else:
        counter += len(tag_zero) + len(tag_one) + len(zero_one)
    print(f'Case {case}: {counter}')
    case+=1