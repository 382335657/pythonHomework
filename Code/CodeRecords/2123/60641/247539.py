def main():
    num = int(input())
    x = 1

    while True:
        x2 = (x + num / x) / 2
        if x2 == x and x2 == int(x2):
            print(True)
            break
        else:
            print(False)
            break
    

if __name__ == "__main__":
    main()