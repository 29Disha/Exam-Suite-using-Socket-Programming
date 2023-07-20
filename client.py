from socket import *
serverName = "localhost"
serverPort = 2323
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort)) 
print("\n\n\t\t\t\tWelcome to GK Quiz\n")

for i in range (5):
    print("\nQuestion ",i+1,"\n")
    ques = clientSocket.recv(1024) 
    print(ques.decode())
    answer = input("Enter Answer\n") 
    clientSocket.send(answer.encode()) 
    check1 = clientSocket.recv(1024) 
    print("From Server: ", check1.decode()) 

score = clientSocket.recv(1024)
print("\n\nSCORE: ", score.decode())

grade = clientSocket.recv(1024)
print("\n\nGRADE: ", grade.decode())

clientSocket.close()