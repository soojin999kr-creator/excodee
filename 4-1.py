while True:
    filename=input("Enter file name: ")

    try:
        f=open(filename,"r")
        save=open(filename+".sav","w")
        num=1
        for line in f:
            print(num,line,end="")
            save.write(str(num)+" "+line)
            num+=1

        f.close()
        save.close()
        break
    except FileNotFoundError:
        print("File not found")
