import socket
import webbrowser
import os
from datetime import datetime

import wikipedia
from pyjokes import pyjokes

if _name_ == "_main_":
    while True:
        query = input("Enter A Message To Start Chatting:\n")
        query = query.lower()

        if 'ip address' in query:
            print("Finding")
            hname = socket.gethostname()
            results = socket.gethostbyname(hname)
            print(hname)
            print(results)
            print('Host name is:ROHIT')
            print(hname)
            print('IP address is :')
            print(results)
        # break

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open("https://www.google.com/search?q=" + query)
            print('data is showned in google chrome')


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            print("User asked to Locate")
            print(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
            print('data is showned in browser')



        elif "write a note" in query:
            print("What should i write, sir")
            note = input('Enter Your Note:-\n')
            file = open('junior.txt', 'w')
            print("Your note has been saved")
            file.write(note)

        elif "show note" in query:
            print("Showing your Notes")
            file = open("junior.txt", "r")
            print(file.read())
            print(file.read(6))

        elif 'jokes' in query:
            print('wait,hmmm')
            print(pyjokes.get_joke())

        elif 'open youtube' in query:
            webbrowser.open("http://youtube.com")
            print("youtube is opened")

        elif 'open twitter' in query:
            webbrowser.open("http://twitter.com")
            print("twitter is opened")

        elif 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com")
            print("chatgpt is opening ")

        elif 'open google' in query:
            webbrowser.open("http://google.com")
            print("google is opened")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")
            print("spotify is opened")

        elif 'time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'date' in query:
            now = datetime.now()
            print('Current date and time is:')
            print(now)
        elif 'who invited you' in query:
            print(
                "At first I was just an idea, then a bunch of people at electronics and computer science Department put their heads together. And now here I am ! The Junior!")
        elif 'who are you' in query:
            print("I am your Assistant Sir! Junior ")
            print("i have all permissions about Devil Security server(DSS) and high-tech security")

        elif 'hi' in query:
            print("how can i help you sir? ")

        elif 'my college name' in query:
            print('Your college name is shah and anchor kutchhi engineering college ,Sir')

        elif 'what is happening today in my college ? ' in query:
            print('today is mini project review, which will be held in shah and anchor kutchhi engineering college,Sir')

        elif 'open files' in query:
            apppath = "C:\\Windows\\explorer.exe"
            os.startfile(apppath)
            print('Files are being opened')

        elif 'close file' in query:
            os.system("taskkill /f /im explorer.exe")
            print('File Manager is closed')

        elif 'open cmd' in query:
            apppath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(apppath)
            print('terminal being opened')

        elif 'close cmd' in query:
            os.system("Taskkill /f /im cmd.exe")
            print('terminal is closed')

        elif 'exit' in query:
            print('GoodBye!!!!')
            break
        else:
            print("Sorry !! I can't understand")