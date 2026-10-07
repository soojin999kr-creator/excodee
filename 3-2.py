def min_max(numbers):
    return min(numbers), max(numbers)

user_input = input("정수들을 공백으로 구분하여 입력하세요: ")
numbers = list(map(int, user_input.split()))
minimum, maximum = min_max(numbers)
print(f"최솟값: {minimum}, 최댓값: {maximum}")