import random
import string

if __name__ == '__main__':
    chars = [chr(i) for i in range(33, 123)]
    # random.shuffle(chars)
    length = random.randint(8, 16)
    pw = ''.join(random.sample(chars, length))
    print(pw)
    # print(chars)
    # s1 = string.ascii_lowercase
    # s2 = string.ascii_uppercase
    # s3 = string.digits
    # s4 = string.punctuation
    # s = list(s1 + s2 + s3 + s4)
    # print(s)