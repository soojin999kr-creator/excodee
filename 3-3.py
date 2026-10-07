def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_input = input("문자열을 입력하세요: ")
vowel_count = count_vowels(user_input)
print(f"입력한 문자열에는 모음이 {vowel_count}개 있습니다.")