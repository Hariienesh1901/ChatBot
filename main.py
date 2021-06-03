import datetime

import pywhatkit

print("Example: Tell me the time, Play Sun Goes Down, Send a mail, Search Hello World"
      "Info about Python")


def run_chatbot():
    command = input("Enter a command: ")

    if 'time' in command:
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print('The time is ' + dt_string)

    elif 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)

    elif 'info about' in command:
        about = command.replace('info about', '')
        pywhatkit.info(about)

    elif 'search' in command:
        search = command.replace('search', '')
        pywhatkit.search(search)

    elif 'mail' in command:
        sender = input("From: ")
        password = input("Password: ")
        title = input("Title: ")
        body = input("Body: ")
        to = input("To: ")
        pywhatkit.send_mail(sender, password, title, body, to)

    else:
        print("Try: Tell me the time, Play Sun Goes Down, Send a mail, Search Hello World, Info about Python")


while True:
    run_chatbot()
