students = {}

# 1. 명단 작성
while True:
    student_id = input("학번 입력 (0 입력 시 종료): ")
    if student_id == '0':
        break
    name = input("이름 입력 ('None' 입력 시 종료): ")
    if name == 'None':
        break
    students[student_id] = name

print("\n생성된 딕셔너리:", students)

# 2. 학번으로 이름 출력 및 3. 종료 ('quit')
while True:
    query = input("\n조회할 학번을 입력하세요 ('quit' 입력 시 종료): ")
    if query == 'quit':
        print("프로그램을 종료합니다.")
        break

    # 학번 존재 여부 확인
    if query in students:
        print(f"이름: {students[query]}")
    else:
        print("not found!")