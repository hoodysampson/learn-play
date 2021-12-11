def comma(seqs):
    seqs=str(seqs)
    pm='' if not seqs.startswith('-') else '-'
    seqs=seqs if not seqs.startswith('-') else seqs[1:]
    flt = seqs[seqs.find('.'):] if '.' in seqs else ''
    seqs=seqs if '.' not in seqs else seqs[:seqs.find('.')]
    result=''
    while seqs:
        seqs,rear=seqs[:-3],seqs[-3:]
        result= rear+','+result if result else rear
    return pm+result+flt

def comma_r(seqs):
    seqs = str(seqs) if type(seqs) is not str else seqs
    seqs, rear = seqs[:-3], seqs[-3:]
    if seqs:
        return comma_r(seqs)+','+rear
    else:
        return rear


def money(N,numwidth=0,currency='$'):
    """
    Format number N for display with commas, 2 decimal digits, leading $ and sign, and optional padding: "$ -xxx,yyy.zz". numwidth=0 for no space padding, currency='' to omit symbol, and non-ASCII for others (e.g., pound=u'\xA3' or u'\u00A3').
    """
    return '%s%*s'%(currency,numwidth,comma(N))

if __name__=='__main__':
    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests: print(comma(test))


        print('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2 ** 32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv)==1:
        selftest()
    else:
        print(money(float(sys.argv[1]),int(sys.argv[2])))






# print(money(-12234.723654,30,currency='￥'))