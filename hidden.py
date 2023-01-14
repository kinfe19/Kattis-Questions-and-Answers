def main():
    p, s = input().split()
    f = 1
    for i in range(len(s)):
        if p == '':
            break
        elif s[i] == p[0]:
            p=p[1:]
        elif s[i] in p:
            f = 0
            break
    if not f or p!='':
        print('FAIL')
    else:
        print('PASS')
if __name__ == '__main__':
    main()