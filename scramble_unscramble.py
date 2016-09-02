#By AndyTheDandyOne
#A funny way to scramble a message and then, unscramble back to its original
#content.
#In the code bellow, you will visually see on the console when you run the app
#the process of getting the orignal message, converting it to numbers, then back
#to single characters and finally back to the orignal message.
#Feel free to change things aroun if you see fit.

def convertToNumbers():
    scrambles = []
    split = []
    unscramble = []

    text = open('movie_quotes.txt')
    original = text.read()
    print(original)

    for codes in original:
        split.append(codes)
        scrambles.append(ord(codes))

    print(scrambles)

    for crazyNumbers in scrambles:
        unscramble.append(chr(crazyNumbers))

    print(unscramble)

    finalResult = ''.join(unscramble)
    print finalResult
    display = text.close()


convertToNumbers()
