import time
import socket
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error: {e}"
ip = get_ip_address()

monkeylist = ["monkey1", "monkey 2", "monkey 3"]
a = input(str("Are you a monkey? > "))
while True:
    a = input(str("Are you a monkey? > "))
    if a == "yes" or a == "y":
        i = input(str("What is your name? > "))
        monkeylist.append(i)
        print(f"Hi {i}! You are the {len(monkeylist)}th monkey")
        print("= Welcome to the Monkey terminal interface! =")
        print("(1.) Check the list of monkeys")
        print("(2.) Change account")
        print("(3.) Order a banana")
        l = input(str("Choose one 1-3"))
        if l == "1":
            print(monkeylist)
            for i in range(100):
                print("  ")
        elif l == "2":
            for i in range(100):
                print("  ")
        elif l == "3":
            print("Ordering banana...")
            time.sleep(10)
            print(f"Your IP address is: {ip}")
            for i in range(100):
                print("  ")
        else:
            print("Invalid Command!")
            print("-")
    elif a == "no" or a== "n":
        print("Liar, get back in your cage monkey!")
        for i in range(10):
            print(f"Your IP address is: {ip}")
            print("The Monkey Federation will bombard your home to have you executed")
            time.sleep(1)
        for i in range(100):
            print("  ")
    else:
        print("invalid command")