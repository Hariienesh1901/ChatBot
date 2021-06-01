import datetime
import pywhatkit

print("Example: Tell me the time, Play Sun Goes Down, Send a mail, Send a WhatsApp message, Search Hello World, "
      "Info about Python")

command = input("Enter a command: ")

if 'time' in command:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('The time is' + dt_string)

if 'play' in command:
    song = command.replace('play', '')
    pywhatkit.playonyt(song)

if 'info about' in command:
    about = command.replace('info about', '')
    print(pywhatkit.info(about))

if 'search' in command:
    search = command.replace('search', '')
    pywhatkit.search(search)

else:
    print("Try: what's the time, play Sun Goes Down, info about Python, search Hello World.")
