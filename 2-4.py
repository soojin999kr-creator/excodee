n = int(input("1에서 100 사이의 자연수를 입력하세요:"))

if n % 3 == 0 and n % 5 == 0:
    print(f"{n}은(는) 3과 5의 공배수입니다.")
elif n % 3 == 0:
    print(f"{n}은(는) 3의 배수입니다.")
elif n % 5 == 0:
    print(f"{n}은(는) 5의 배수입니다.")
else:
    print(f"{n}은(는) 3 또는 5의 배수가 아닙니다.")