import random

words = ["hangman", "python", "developer", "apple", "banana"]

while True:
    word = random.choice(words)
    guessed_letters = []
    trials = 6

    print("\n--- 행맨 게임 시작 ---")

    while trials > 0:
        display = ""
        all_guessed = True
        for char in word:
            if char in guessed_letters:
                display += char
            else:
                display += "_"
                all_guessed = False

        print("\n현재 단어:", display)

        if all_guessed:
            print("Good Job!")
            break

        guess = input("글자를 입력하세요: ").lower()

        if guess in guessed_letters:
            print("이미 입력한 글자입니다.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"맞습니다! '{guess}'가 단어에 포함되어 있습니다.")
        else:
            trials -= 1
            print(f"Nope! {trials} trials left")

    if trials == 0:
        print(f"\nFail! 정답은 '{word}' 입니다.")

    again = input("\n게임을 계속 하시겠습니까? (y/n): ")
    if again.lower() != 'y':
        print("게임을 종료합니다.")
        break