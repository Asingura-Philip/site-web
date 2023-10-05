# funcion that prints hello world
def function():
    print("hello world")


# function()

# program that prints out numbers from 1 - 80 but 4 numbers per line


def nums():
    for i in range(1, 81):
        print(i, end=' ')
        if i % 4 == 0:
            print()


# nums()

# write a function that converts temperature


def main():
    print("degree converter")
    print("please enter degrees in celicius to be converted")
    tc = float(input())
    print("the degrees to be converted are " + str(tc))
    converted = convert(tc)
    print("converted temp is " + str(converted))


def convert(a):
    tc = ((a * 1.8) + 32)

    return tc


main()

# write a function that returns the name an age of a person as a list
print("hello ,,, what is your name?")
name = input()
print("hello " + name + " ,,what is your age")
age = input()
