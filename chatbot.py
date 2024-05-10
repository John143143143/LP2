import random
greetings=["Hello!","Hi there!","Hey!"]
farewell=["Have a good day!","Good bye!","See you soon!"]
responses=["Could you please repeat that!","Im sorry, I didn't get that"]

def generate_resopnse(msg):
    msg = msg.lower()
    if msg.startswith("hi") or msg.startswith("hello"):
        return random.choice(greetings)
    elif msg.startswith("bye"):
        return random.choice(farewell)
    else:
        return random.choice(responses)
    
def chat():
    print("Chatbot starts here!!")
    while True:
        user_msg = input("You: ")
        response = generate_resopnse(user_msg)
        print("Chatbot: ",response)
        if user_msg == "bye":
            return
        
if __name__== "_main_":
    chat()