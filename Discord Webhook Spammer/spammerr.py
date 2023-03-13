import dhooks, os, platform, threading
import time
import random

class Spammer:
    def __init__(self) -> None:
        self.system = platform.system()
    def spam(self, wbk, msg, dly):
        global counter
        counter = 0
        if self.system == "Windows" or self.system == "windows":
            os.system("cls")
        else:
            os.system("clear")
        webhok = dhooks.Webhook(wbk)
        while True:
            try:
                thread = threading.Thread(target=webhok.send(msg))
                thread.daemon = True
                thread.start()
            except Exception as e:
                print('\033[31m' + "Unkown Error Occured\n" + f"Error Message is : {str(e)}" + "Message count : " + str(counter))
            else:
                counter += 1
                print('\u001b[32m' + "Succesfull, Message =>" + ", " + "Your Total spamming message => " + str(counter))
            time.sleep(int(dly))
    def random_spammer(self, wbk, dly):
        global counter
        counter = 0
        if self.system == "Windows" or self.system == "windows":
            os.system("cls")
        else:
            os.system("clear")
        webhok = dhooks.Webhook(wbk)
        while True:
            try:
                thread = threading.Thread(target=webhok.send(Spammer.random_words()))
                thread.daemon = True
                thread.start()
            except Exception as e:
                print('\033[31m' + "Unkown Error Occured\n" + f"Error Message is : {str(e)}" + "Message count : " + str(counter))
            else:
                counter += 1
                print('\u001b[32m' + "Succesfull" + ", " + "Your Total spamming message => " + str(counter))
            time.sleep(int(dly))
    def random_words():
        asd = []
        file = open("random_words.txt", "r")
        for f in file.readlines():
            asd.append(f)
        return random.choice(asd)


webhook = input("Enter your webhook : ")
msg = input("İf you write random program will send random words\nEnter your Message : ")
delay = str(input("Enter your delay value : "))
if delay == "":
    delay = 0
if __name__ == '__main__':
    try:
        if msg == "random" or msg == "RANDOM":
            Spammer().random_spammer(webhook, delay)
        else:
            Spammer().spam(webhook, msg, delay)
    except KeyboardInterrupt:
        if platform.system() == "Windows":
            os.system("cls")
            print("total number of messages sent successfully : " + str(counter))
            time.sleep(0.5)
            exit()
        else:
            os.system("clear")
            print("total number of messages sent successfully " + str(counter))
            time.sleep(0.5)
            exit()
    except Exception as e:
        print(str(e))
