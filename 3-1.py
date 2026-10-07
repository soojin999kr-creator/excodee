def calc(*args,**kwargs):
    op=kwargs.get('op','+')

    if not args:
        return 0

    if op=='+':
        return sum(args)
    elif op=='*':
        result=1
        for num in args:
            result*=num
        return result
    else:
        raise ValueError("지원되지 않는 연산자입니다. '+' 또는 '*'만 가능합니다.")

print(calc(1,1,4,op='+'))
print(calc(1,2,op='*'))