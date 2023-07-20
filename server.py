from calendar import c
from socket import *
from tkinter import scrolledtext
import random
serverPort = 2323
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("localhost",serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    score=0

    completed=[]

    qanda=[
        ["Who is the author of the book 'Nineteen Eighty Four'\nA. Thomas Hardy\nB. Emile Zola\nC. George Orwell\nD. Walter Scott","C"],
        ["Who wrote 'War and Peace'?\nA. Leo Tolstoy\nB. Mahatma Gandhi\nC. Charles Dickens\nD. Kipling","A"],
        ["What is the name of the biggest planet in our solar system?\nA. Jupiter\nB. Saturn\nC. Sun\nD. Earth","A"],
        ["Who invented the Car?\nA. Charles Babbage\nB. Elon Musk\nC. Johannes Gutenberg\nD. Carl Benz","D"],
        ["This yellow cartoon character lives in a pineapple under the sea.\nA. Simpsons\nB. Spongebob\nC. Bert\nD. Tweety","B"],
        ["On Wednesdays we wear ______.\nA. Red\nB. Black\nC. Pink\nD. Green","D"],
        ["Which of the following statements is not applicable for cable internet access?\nA)Analog signal is converted to digital signal in DSLAM\nB)Cable modem connects home PC to Ethernet port\nC)It includes HFCs\nD)It is a shared broadcast medium","A"],
        ["If the residence is not located within 5 to 10 miles of the Central Office, the residence must resort to an alternative form of Internet access. Which of the access networks does this represent?\nA)DSL\nB)Cable\nC)FTTH\nD)Dial-Up","A"],
        ["_____are used for cellular phone, satellite, and wireless LAN communications.\n A)Radio waves\n B)Infrared waves\n C)Microwaves\n D)None of the mentioned","C"],
        ["The huge distance of 36,000 KMs from ground station through satellite back to ground station introduces a substantial signal propagation delay of ______.\nA)280 seconds\nB)28 seconds\nC)2 seconds\nD)280 milliseconds","D"]]


    for count in range(5):
        while True:
            n=random.randint(0,9)
            if n not in completed:
                completed.append(n)
                break
            else:
                n=random.randint(0,9)
        connectionSocket.send(qanda[n][0].encode())
        answer = str(connectionSocket.recv(1024).decode())
        answer=answer.upper()
        print(answer)
        if (answer==qanda[n][1]):
            response="Correct"
            score=score+1
        else:
            response="Wrong"
        connectionSocket.send(response.encode())

    connectionSocket.send(str(score).encode())

    print("quiz is over")

    if (score>=4):
        grade="A"
    elif (score>=3):
        grade="B"
    elif (score>=2):
        grade="C"
    else:
        grade="F"
    connectionSocket.send(str(grade).encode())

    connectionSocket.close()