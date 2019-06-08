import os

class Sentence:
    def __init__(self, num, jp, jph, jpa, cn):
        self.num = num.strip()
        self.jp = jp.strip()
        self.jph = jph.strip()
        self.jpa = jpa.strip()
        self.cn = cn.strip()

fi = open("sentences.sep.txt", "r")
sentences = []


while True:
    num = fi.readline()
    if num == "":
        break
    jp = fi.readline()
    jph = fi.readline()
    jpa = fi.readline()
    cn = fi.readline()
    _ = fi.readline()


    # print(num, jp, jph, cn)
    #print(jpa)
    new_sentence = Sentence(num, jp, jph, jpa, cn)
    sentences.append(new_sentence)

    #_ = input()

progress_str = ""
try:
    fp = open("progress.txt", "r")
    progress_str = fp.read()
except:
    fp = open("progress.txt", "w")
    fp.write("1")
    progress_str = "1"

progress_str = progress_str.strip()
if progress_str.isnumeric() == False:
    progress_str = "1"


should_start = False
while True:
    os.system("clear")
    print("You have studied " + progress_str + " out of 1000. Your options:")
    print("1: Start from beginning, 2: Start from #" + progress_str + ", 3: Go to custom #, 4: Quit")
    ans = input("Take your pick: ")
    ans = ans.strip()
    if ans == "1":
        progress_str = "1"
        should_start = True
        break
    elif ans == "2":
        should_start = False
        break
    elif ans == "3":
        while True:
            start_num = input("Tell me where do you want to start? (sentence number): ").strip()
            if start_num.isnumeric == False:
                print("invalid number")
                continue
            if int(start_num) > 0 and int(start_num) < 1001:
                if int(start_num) == 1:
                    should_start = True
                else:
                    should_start = False
                progress_str = start_num
            break
        break
    elif ans == "4":
        exit()


for sentence in sentences:
    os.system("clear")
    if should_start == False:
        if sentence.num == progress_str:
            should_start = True
    if should_start:
        fpo = open("progress.txt", "w")
        fpo.write(sentence.num)
        fpo.close()
        print("#" + sentence.num)
        print(sentence.jp)
        print(sentence.jph)
        while True:
            ans = input("Type the correct romaji (type 'exit' to quit): ").strip()
            if ans == "exit":
                exit()
            if ans == sentence.jpa:
                print("Correct!")
                print("Chisese:", sentence.cn)
                _ = input(" --- press enter to continue --- ")
                break
            else:
                yn = input("Incorrect! Input 'y' to reveal answer. Input anything else to try again.")
                if yn == "y":
                    print("Your answer:", ans)
                    print("Correct ans:", sentence.jpa)
                    input("Got it? <Enter> to try again!")
                    os.system("clear")
                    print("#" + sentence.num)
                    print(sentence.jp)
                    print(sentence.jph)

