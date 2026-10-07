while True:
    filename = input("Enter file name: ")

    try:
        f=open(filename,"r")

        text=f.read()

        characters=len(text.replace(" "," ").replace("\n"," "))
        words=len(text.split())
        lines=len(text.split())

        print("characters: ", characters)
        print("words: ", words)
        print("lines: ", lines)

        f.close()

    except FileNotFoundError:
        print("File not found")

