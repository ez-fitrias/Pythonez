user = input("> ").lower()
status = 'unknown'
statusflag = 'unknown'
while user != "quit":
    if user == statusflag:
        print(f"the car already {status}")
    elif user == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("status - show current condition")
        print("quit - quit the game")
    elif user == "start":
        print("car started...ready to go")
        status = "started"
        statusflag = 'start'
    elif user == "stop":
        print("car stopped")
        status = "stopped"
        statusflag = 'stop'
    elif user == "status":
        print('current condition : ', status)
    else:
        print("I don't understand...")
    user = input("> ").lower()
