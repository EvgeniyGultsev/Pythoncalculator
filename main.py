from Calculator import Calculate

if __name__ == '__main__':
    launch = Calculate
    f = open("test.txt", "r")
    for i in f:
        b, command, c = i.split(sep=" ")
        if command == "+":
            print(launch.add("", b, c))
        elif command == "-":
            print(launch.substract("", b, c))
        elif command == "*":
            print(launch.multiply("", b, c))
        elif command == "/":
            print(launch.divide("", b, c))
