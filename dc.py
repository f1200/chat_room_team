from socket import *
from threading import *
from tkinter import *
import tkinter.font as font
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
hostIp = "6.tcp.ngrok.io"
portNumber = 16424
clientSocket.connect((hostIp, portNumber))

window = Tk()
window.title("H A C K E R   __  A R A B")
window.configure(bg='gold')
myFont = font.Font(size=12)
txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

txtYourMessage = Entry(window, width=50)
nikn="D a R k 1"
txtYourMessage.insert(0,nikn+" :")

txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def sendMessage():

    clientMessage = txtYourMessage.get()
    txtMessages.insert(END, "\n"+ clientMessage)
    clientSocket.send(clientMessage.encode("utf-8"))
    txtYourMessage.delete(0, END)
    txtYourMessage.insert(0,nikn+" :")
 

btnSendMessage = Button(window, text="أرســــال", width=20, command=sendMessage)
btnSendMessage['font']=myFont
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMessages.insert(END, "\n"+serverMessage)

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

window.mainloop()





