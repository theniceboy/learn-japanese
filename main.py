import os

class Sentence:
    def __init__(self, num, jp, jph, jpa, cn):
        self.num = num.strip()
        self.jp = jp.strip()
        self.jph = jph.strip()
        self.jpa = jpa.strip()
        self.cn = cn.strip()


sentences = []

fi = open("./sentences.sep.txt", "r")

while True:
    num = fi.readline()
    if num == "":
        break
    jp = fi.readline()
    jph = fi.readline()
    jpa = fi.readline()
    cn = fi.readline()
    _ = fi.readline()

    new_sentence = Sentence(num, jp, jph, jpa, cn)
    sentences.append(new_sentence)

os.system("clear")
for sentence in sentences:
    while True:
        print(sentence.jp)
        print(sentence.jph)
        ans = input("Romaji: ")
        if ans == sentence.jpa:
            print("Correct!")
            _ = input(" --- Press enter to continue --- ")
            os.system("clear")
            break
        else:
            print("Incorrect!")
            reveal = input(" --- Press enter to continue, y to reveal the answer --- ")
            if reveal == "y":
                print(sentence.jpa)
                _ = input(" --- Press enter to continue --- ")
            os.system("clear")



