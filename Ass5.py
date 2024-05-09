
import time
now = time.ctime()


qna = {
    "hi" : "hey",
    "how are you?" : "i am fine",
    "what is your name " : "my name is Sainath",
    "how old are you" : "I am 20 years old",
    "What is the time now": now,
}

while True:
    qs = input()
    if qs == "quit":
        break
    else:
        print(qna[qs])