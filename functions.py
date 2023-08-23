import string


def multiply(x, y):
    result = x * y
    return result


answer = multiply(4, 4)
# print(answer)


for i in range(6):
    answer2 = multiply(2, i)
    # print(answer2)


def isPalindrom(string):

    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].lower() == string.lower()


# word = input("please enter a word to check   ")
# if isPalindrom(word):
#    print("'{}' is a palindrom ".format(word))
# else:
#    print("'{}' is not a palindrom".format(word))


# print(isPalindrom("ala"))


def isPalindromString(text):

    diff1 = text.translate(str.maketrans('', '', string.punctuation))
    diff2 = "".join(diff1.split())

    # return diff2
    return isPalindrom(diff2)


word1 = input("Please enter text her:  ")
print(isPalindromString(word1))
