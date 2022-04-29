# Create your own adventure with python here

def restart():
    answer = input("Do you want to play a game?""\N{grinning face} (yes/maybe/no)")
    if answer.lower().strip() == 'yes':
        answer = input("I like you, wanna go get Starbucks some time? (Yes/No) ")

        if answer == "Yes":
            print("Holla at me, let's set that up")
        else:
            print("you ugly, I ain't want you either anyways")
            return restart()

    elif answer == "maybe":
        answer = input("What do you mean... maybe? (you weird/Maybe/Mind your business/No)").lower().strip()

        if answer == "you weird":
            print("Okay...you're point is?")

        elif answer == "Maybe":
            print("Okay, sorry for disturbing you")
        elif answer == "Mind your business":
            print("Wow, you're rude.")
        else: 
            print("Now you do hahaha")
            return restart()
    else:
        answer = input("Too bad, you're playing anyways hahaha (ihy/leave) ").lower().strip()
        if answer == "ihy":
            print('Well, I hate you more. Goodbye.')
        else:
            print("You aren't allowed to leave yet hahaha")
            return restart()
restart()

