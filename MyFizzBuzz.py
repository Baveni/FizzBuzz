print "Welcome to my FizzBuzz game! What it does you ask? Simple, you enter a number from 1 to 100"
print "If a number is divisible with 3, it will say Fizz! and if a number si divisible with 5 it will say Buzz!"
print "If a number si divisible with 3 and 5 it will say FizzBuzz!"

num = int(raw_input("Please punch in a number from 1 to 100!>>"))
answer = "Y"
while answer == "Y":
    for x in range(1, num + 1):
        if (x % 3 == 0) and (x % 5 == 0):
            print "FizzBuzz!"
        elif x % 3 == 0:
            print "Fizz!"
        elif x % 5 == 0:
            print "Buzz!"
        else:
            print x

    while True:
        print "would you like play one more time?"
        answer = raw_input()
        if answer not in "YN":
            print "You have to type Y or N only"
        else:
            break
print "Thank you for playing."

