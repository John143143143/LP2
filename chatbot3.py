import time
now = time.time()

qna={
    "hi":"hey",
    "how are you?":"I am fine",
    "what is your name":"my name is sainath",
    "how old are you?" : "I am 20 years old",
    "what is time now":now
}

while True:
    qs = input()
    if qs == "quit":
        break
    else:
        print(qna[qs])