# Author: Jake Graef and Michael Sheinman
# Date: Jam. 12, 2018
# Filename: Final Project
# Description: Online Casino

# I'm importing time and system to use them for printing in one line(later)
import time
import sys
import random
import os.path  # I imported os.path so I can see if the text file exists and delete text files
import smtplib


# Don't get into this too much, it's just how I make colors
class Bcolors:
    red = '\033[91m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    NOTHING = '\033[48m'
    BLACK = '\033[97m'


# I just made this into variable so I don't have to write it over every time
youremail = "casinogames99@gmail.com"
# Other Varaibles I need to define at top
kicked_out = False
graph = []


# This are functions, they're easier to use than over indenting things. We put the games/email work into the functions.

# This function sends the progress email
def email_progress():
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    inFile = open(sign_in_user_name + '.txt', "r")
    w = inFile.readlines()
    fromaddr = 'casinogames99@gmail.com'

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['Subject'] = "MJ Casino"

    body = "Hope you are enjoying the Casino! Here is your progress!"

    msg.attach(MIMEText(body, 'plain'))

    filename = str(w[0].strip()) + "graph.txt"
    attachment = open(str(w[0].strip()) + "graph.txt", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "mikejack")
    text = msg.as_string()
    server.sendmail(fromaddr, w[2], text)
    server.quit()


# This function sends the sign up email
def email_sign_up():
    w = [new_user_name, new_user_password, new_user_mail]
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    img_data = open("Casino.PNG", 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'MJ Casino'
    msg['From'] = 'jake.graef99@gmail.com'
    msg['To'] = 'jake.graef99@gmail.com'

    text = MIMEText("Welcome to MJ Casino, an online game with a variety of gambling fun! Enjoy " + str(w[0]) + '!')
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("Casino.PNG"))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('casinogames99@gmail.com', 'mikejack')
    s.sendmail(youremail, w[2], msg.as_string())
    s.quit()


# This function deletes the email
def email_delete():
    inFile = open(sign_in_user_name + '.txt', "r")
    w = inFile.readlines()
    w = w[0].split('\n') + w[1].split('\n') + w[2].split('\n')
    for i in range(3):
        w.remove('')
    if kicked_out == True:
        content = 'Your account has been deleted because you have lost all your money ' + str(w[0]) + '!'
    else:
        content = 'Your account has been deleted! We are sorry that you are leaving us ' + str(w[0]) + '!'
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart

    img_data = open("Casino.PNG", 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'MJ Casino'
    msg['From'] = 'jake.graef99@gmail.com'
    msg['To'] = 'jake.graef99@gmail.com'

    text = MIMEText(content)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("Casino.PNG"))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('casinogames99@gmail.com', 'mikejack')
    s.sendmail(youremail, w[2], msg.as_string())
    s.quit()


# dices game
def dices():
    global graph  # globalizing outside variables
    global total
    global sign_in_user_name
    print("Ready to throw some dices?")
    dealer = 0
    user = 0
    betting_money = 1000000000
    while betting_money > total:
        while True:
            try:
                betting_money = float(input("Enter amount of money you want to bet: ").lstrip())
                if betting_money > total:
                    print("You can't bet more than what you have")
                elif betting_money <= 0:
                    print("You can't bet 0/below 0")
                else:
                    break
            except ValueError:
                print('Only integers!')
        dice_one = " ___\n" \
                   "|   |\n" \
                   "| * |\n" \
                   "| 1 |"
        dice_two = " ___\n" \
                   "|   |\n" \
                   "|* *|\n" \
                   "| 2 |"
        dice_three = " ___\n" \
                     "|*  |\n" \
                     "|* *|\n" \
                     "| 3 |"
        dice_four = " ___\n" \
                    "|* *|\n" \
                    "|* *|\n" \
                    "| 4 |"
        dice_five = " ___\n" \
                    "|* *|\n" \
                    "|* *|\n" \
                    "|*  |\n" \
                    "| 5 |"
        dice_six = " ___\n" \
                   "|* *|\n" \
                   "|* *|\n" \
                   "|* *|\n" \
                   "| 6 |"
        all_dices = {1: dice_one, 2: dice_two, 3: dice_three, 4: dice_four, 5: dice_five, 6: dice_six}
        all_values = list(all_dices.values())
        all_keys = list(all_dices.keys())
        for i in range(3):
            your_dice = random.choice(all_keys)
            for char in "Your dice....\n":
                print(char, end="")
                sys.stdout.flush()  # this flushes the buffer
                time.sleep(.1)
            print(all_dices[your_dice])
            dealer_dice = random.choice(all_keys)
            for char in "Dealer dice....\n":
                print(char, end="")
                sys.stdout.flush()
                time.sleep(.1)
            print(all_dices[dealer_dice])
            if dealer_dice == your_dice:
                print("That's a draw")
            elif dealer_dice > your_dice:
                print("Dealer point!")
                dealer += 1
            else:
                print("User point!")
                user += 1
            print("Dealer: {}".format(dealer))
            print("User: {}".format(user))
        if dealer > user:
            print("Dealer wins! ")
            total -= betting_money
            break
        elif dealer < user:
            print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
            total += betting_money
        elif dealer == user:
            print("Seems like it was a draw")
    print("\n" + str(sign_in_user_name) + "\'s balance: $%s" % total)
    graph.append(total)


# slot machine
def slot_machine():
    global graph  # globalizing outside variables
    global total
    global sign_in_user_name
    print("Ready to pull the leaver in our slot machine?")
    symbols = ['♦', 'BAR', '7', '☺']
    symbol = []
    betting_money = 1000000000
    while betting_money > total:
        while True:
            try:
                print('| ' + str(sign_in_user_name) + "\'s balance: $%s" % total + ' |')  # printing balance of user
                betting_money = float(input("Enter amount of money you want to bet: ").lstrip())
                if betting_money > total:
                    print("You can't bet more than what you have")
                elif betting_money <= 0:
                    print("You can't bet zero/below zero.")
                else:
                    break
            except ValueError:
                print('Only integers!')
        print('Ok lets spin!')
        print('----------')
        print('|', end=" ")
        sys.stdout.flush()
        for i in range(3):
            time.sleep(2)
            character = random.choice(symbols)
            symbol.append(character)
            print(character, end=" ")
            sys.stdout.flush()
        print('|')
        print('----------')
        if symbol[0] == symbol[1] == symbol[2]:
            print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
            total += betting_money
        elif symbol[1] == symbol[2] or symbol[1] == symbol[0] or symbol[0] == symbol[2]:
            print('You got a pair! You win half the money gambled!')
            total += (betting_money / 2)
            break
        else:
            print('No matches! You lose!')
            total -= betting_money
            break
    print("\n" + str(sign_in_user_name) + "\'s balance: $%s" % total)
    graph.append(total)


# flaming hot slot
def flaming_hot_slot():
    global graph  # globalizing outside variables
    global total
    global sign_in_user_name
    print("Welcome to our hot slot machine!!")
    winHotSlot = False
    # This is the betting money while loop
    while True:
        try:
            print('| ' + str(sign_in_user_name) + "\'s balance: $%s" % total + ' |')  # printing balance of user
            betting_money = float(input("How much money would you like to bet: "))
            if betting_money > total:
                print("You can't bet above your total ")
            elif betting_money <= 0:
                    print("You can't bet zero/below zero.")
            else:
                break
        except ValueError:
            print("This is not money, please only use integers")
    # This list stores signs that will later be randomized.
    signs = ["◘", "A", "♠", "♣", "♦", "♥", "☻", "7", '0']
    lists = []
    correct = 0
    # This loop will run 5 times
    for i in range(5):
        # I now randomize the list with 5 different
        a = [random.choice(signs), random.choice(signs), random.choice(signs), random.choice(
            signs), random.choice(signs), '', '', '', '', '']
        combined = ' '.join(a)
        time.sleep(1)
        for i in range(len(a) - 5):
            if a[i] == a[i + 1] or a[i + 1] == 'A' or a[i] == 'A':
                if a[i + 1] == a[i + 2] or a[i + 2] == 'A' or a[i +1] == 'A':
                    correct += 1
                    if a[i + 2] == a[i + 3] or a[1 + 3] == 'A' or a[i+2] == 'A':
                        correct += 1
                        if a[i + 3] == a[i + 4] or a[i + 4] == 'A' or a[i + 3] == 'A':
                            correct += 1
        print(combined)
    if correct == 0:
        print("No matches, seems like you lose")
        result = 0
    elif correct == 1:
        print("You win!")
        result = betting_money * 1
    elif correct == 2:
        print("Big win!!")
        winHotSlot = True
        print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
        result = betting_money * 2
    elif correct == 3:
        winHotSlot = True
        print("Mega win!!!")
        print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
        result = betting_money * 3
    else:
        print("SUPER WIN")
        winHotSlot = True
        print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
        result = betting_money * correct
    print("Your bet: %s$" % betting_money)
    if result - betting_money > 0:
        earn = result - betting_money
        print("You earned %s$ " % earn)
        doubleornothing = ''
        while True:
            if doubleornothing == '':
                doubleornothing = input("Do you want to try and go double? ")
            if doubleornothing == 'yes':
                blackRed = ['red', 'black']
                randomCard = random.choice(blackRed)
                print("I picked random card")
                userChoice = input("Guess whether the card is red or black: ")
                if userChoice == randomCard:
                    print("You're right!")
                    earn *= 2
                    print("You now earned: $%s" % earn)
                    winHotSlot = True
                    again = input("Do you want to try and go double again  ")
                else:
                    print("Nope! The random card was %s!" % randomCard)
                    print("You lose! You get none of the winnings!:(")
                    total -= earn + betting_money
                    again = False
                if again == 'yes':
                    pass
                    doubleornothing='yes'
                else:
                    break
            else:
                break

    if winHotSlot:
        total += earn
    elif result - betting_money == 0:
        print("You only earned %s$, meaning nothing in your balance changes" % betting_money)
    else:
        print("You didn't earn anything, you lost all the %s$" % betting_money)
        total -= betting_money
    print("\n" + str(sign_in_user_name) + "\'s balance: $%s" % total)
    graph.append(total)


# blackjack
def blackjack():
    num = 0
    numD = 0
    global graph  # globalizing outside variables
    global sign_in_user_name
    global total
    print("Welcome to the Blackjack table!")
    cards1 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
              'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    user = []
    dealer = ['?']
    betting_money = 1000000000
    while betting_money > total:
        while True:
            try:
                betting_money = float(input("Enter amount of money you want to bet: ").lstrip())
                if betting_money > total:
                    print("You can't bet more than what you have")
                elif betting_money <= 0:
                    print("You can't bet zero/below zero.")
                else:
                    break
            except ValueError:
                print('Only integers!')
        print('Ok lets start!\nDealing Cards', end=' ')
        for i in range(3):
            time.sleep(1)
            print('.', end='')
            sys.stdout.flush()
        for b in range(2):
            chosenC = random.choice(cards1)
            user.append(chosenC)
            cards1.remove(chosenC)
            if chosenC == 'A' and num < 11:
                chosenC = 11
            elif chosenC == 'A' and num >= 11:
                chosenC = 1
            elif chosenC == 'K' or chosenC == 'J' or chosenC == 'Q':
                chosenC = 10
            else:
                chosenC = chosenC
            chosenC = int(chosenC)
            num += chosenC
        chosenD = random.choice(cards1)
        dealer.append(chosenD)
        cards1.remove(chosenD)
        if chosenD == 'A':
            chosenD = 11
        elif chosenD == 'K' or chosenD == 'J' or chosenD == 'Q':
            chosenD = 10
        else:
            chosenD = chosenD
        chosenD = int(chosenD)
        print('\nYour cards:', user)
        print('Your total:', num)
        print('Dealer:', dealer)
        numD += chosenD
        while True:
            hit = input('Would you like to hit or stay? ')
            if hit == 'hit':
                chosenC1 = random.choice(cards1)
                user.append(chosenC1)
                cards1.remove(chosenC1)
                if chosenC1 == 'A' and num < 11:
                    chosenC1 = 11
                elif chosenC1 == 'A' and num >= 11:
                    chosenC1 = 1
                elif chosenC1 == 'K' or chosenC1 == 'J' or chosenC1 == 'Q':
                    chosenC1 = 10
                else:
                    chosenC1 = chosenC1
                chosenC1 = int(chosenC1)
                num += chosenC1
                if num >= 22:
                    print('Your cards:', user)
                    print('Your total:', num)
                    print('Sorry your over 21! You lose!')
                    total -= betting_money
                    break
                elif num == 21:
                    print('Your cards:', user)
                    print('Your total:', num)
                    print('You got Blackjack! I would recommend staying!')
                else:
                    print('Your cards:', user)
                    print('Your total:', num)
                    print('Dealer:', dealer)
            elif hit == 'stay':
                newD = random.choice(cards1)
                dealer.remove('?')
                dealer.append(newD)
                cards1.remove(newD)
                if newD == 'A' and num < 11:
                    newD = 11
                elif newD == 'A' and num >= 11:
                    newD = 1
                elif newD == 'K' or newD == 'J' or newD == 'Q':
                    newD = 10
                else:
                    newD = newD
                print('Dealer:', dealer)
                numD += int(newD)
                print('Dealer total:', numD)
                while numD < num:
                    ask = input('Press enter to advance!')
                    ask = ask.lower()
                    if ask == '':
                        pass
                    else:
                        pass
                    if numD >= 17:
                        print('Dealer must stay once past 17!')
                        break
                    else:
                        print('Dealer will pick up!')
                        newD1 = random.choice(cards1)
                        dealer.append(newD1)
                        cards1.remove(newD1)
                        if newD1 == 'A' and num < 11:
                            newD1 = 11
                        elif newD1 == 'A' and num >= 11:
                            newD1 = 1
                        elif newD1 == 'K' or newD1 == 'J' or newD1 == 'Q':
                            newD1 = 10
                        else:
                            newD1 = newD1
                        print('Dealer:', dealer)
                        numD += int(newD1)
                        print('Dealer total:', numD)
                if numD >= 17:
                    break
            else:
                print('You must input "hit" or "stay"!')
                pass
        if numD > num and numD <= 21:
            print('Dealer wins!')
            total -= betting_money
            break
        if numD > num and numD > 21:
            print('Dealer went over 21!')
            print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
            total += betting_money
            break
        if num > 21:
            break
        if numD < num:
            print(Bcolors.BOLD + "__    __  _____   _   _        _          __  _   __   _  "
                                 "\n\ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
                                 "\n \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
                                 "\n  \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
                                 "\n  / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
                                 "\n /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| \n" + Bcolors.NOTHING)
            total += betting_money
        if numD == num:
            print('It is a draw! Ties go to house!')
            total -= betting_money
            break
    print("\n" + str(sign_in_user_name) + "\'s balance: $%s" % total)
    graph.append(total)


# roulette
def roulette():
    betting_list=[]
    global graph  # globalizing outside variables
    global total
    global sign_in_user_name
    # This dictionary stores the amount of money the user bets for each game
    current_bets = {1: 0, 2: 0, 3: 0, 4: 0}
    bet1 = False
    bet2 = False
    bet3 = False
    bet4 = False
    # Loop to check the total money
    while True:
        try:
            print("Your money: %s$" % total)
            betting_money = float(input("Money to covert to chips: (total bet for this match): "))
            if betting_money > total:
                print("You can't bet above your total")
            elif betting_money <= 0:
                print("You must bet above 0")
            else:
                if betting_money == total:
                    print("All in, good luck! ☺")
                total -= betting_money
                print("_________________\n")
                print("Total money: %s$" % total)
                print("Total chips: %s$" % betting_money)
                print("________________\n")
                break
        except ValueError:
            print("Please only enter integer")
    print("Here are all the bets you can submit: "
          "\n1) Straight-Up Bet: Placed directly on the number. "
          "\n2) Color bet: Placed on the color of the number(red, black, green)  "
          "\n3) Odd or even: Placed on whether the number is odd or even. Note: 0 and 00 are not even/odd."
          "\n4) Group bet: 1 to 12, 13 to 24 25 to 36 .")
    while True:
        print("You can bet up to %s$" % betting_money)
        print('Your bets so far',current_bets)
        while True:
            try:
                betting_kind = int(input("Pick your bet kind: "))
                if betting_kind == 1 or betting_kind == 2 or betting_kind == 3 or betting_kind == 4:
                    break
                else:
                    print("That's not one of the options")
            except ValueError:
                print("Only integers")

        # Straight bet
        if betting_kind == 1 and betting_kind not in betting_list:
            while True:
                first_bet_value = input("You chose straight up bet! "
                    "\nNow, pick a number between 0, 00, and 36 to bet on. ")
                if first_bet_value == '00':
                    break
                else:
                    try:
                        first_bet_value = int(first_bet_value)
                        if 0 <= first_bet_value <= 36:
                            break
                        else:
                            print("This is not between 00 and 36")
                    except ValueError:
                        print("Only enter integers")
            bet1 = True


        # Color bet
        elif betting_kind == 2 and betting_kind not in betting_list:
            while True:
                second_bet_value = input("You chose color bet! \nNow, pick a color. (green, red, or black): ").lower()
                if second_bet_value == 'green' or second_bet_value == 'red' or second_bet_value == 'black':
                    break
                else:
                    print("Only enter green, red or black.")
            bet2 = True
        # odd or even bet
        elif betting_kind == 3 and betting_kind not in betting_list:
            while True:
                third_bet_value = input("You chose odd or even bet! \nNow, pick odd or even: ").lower()
                if third_bet_value == 'odd' or third_bet_value == 'even':
                    break
                else:
                    print("This is not odd/even bet. Only enter odd or even.")
            if third_bet_value == 'odd' or third_bet_value == 'even':
                bet3 = True


        elif betting_kind == 4 and betting_kind not in betting_list:
            while True:
                try:
                    fourth_bet_value = int(input("You chose group bet! \n Pick either: 1) 1-12 2) 13-24 3) 25 to 36 "))
                    if fourth_bet_value == 1 or fourth_bet_value == 2 or fourth_bet_value == 3:
                        break
                    else:
                        print("This is not one of the options, you must only enter 1, 2, or 3")
                except ValueError:
                    print("Only enter integers")
            bet4 = True
        if betting_kind not in betting_list:
            betting_list.append(betting_kind)
            while True:
                try:
                    money_for_bet = int(input("How much chips would you like to bet: "))
                    if money_for_bet > betting_money:
                        print("You can't bet more than the chips you have")
                    else:
                        break
                except ValueError:
                    print("only integer")
            betting_money -= money_for_bet
            current_bets[betting_kind] = money_for_bet

            if betting_money > 0:
                keep_going = input("Do you want to place another bet(yes/no): ")
                if keep_going == "yes":
                    pass
                elif keep_going == "no":
                    if betting_money > 0:
                        sure = input("If you continue your chips will be lost, are you sure you would like to proceed? ")
                        if sure == 'yes':
                            break
                        else:
                            pass
            else:
                print("Alright, that's all your money!")
                break
        else:
            print('You can not bet twice on the same type!')
            print("Your bets:", current_bets)
            pass
    if bet1 or bet2 or bet3 or bet4:
        print("Time to start the roulette!")
        roulette = ['00', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        red_colors = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black_colors = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        green_colors = [0, '00']
        for i in range(50):
            range_time = 0.05
            a = random.choice(roulette)
            sys.stdout.write(str(a) + ' ')
            sys.stdout.flush()
            time.sleep(range_time)
            range_time += 0.01
        print("\n_____________________")
        print("\nFinal number: %s" % a)
        # Checking whether the color is black, red, or green
        if a in black_colors:
            print("Color: black")
            color = 'black'
        elif a in red_colors:
            print("Color: red")
            color = 'red'
        elif a in green_colors:
            print("Color: green ")
            color = 'green'
        if a != 0 and a != '00':
            if a % 2 == 0:
                print("Odd-even: Even")
                odd_even = 'even'
            else:
                print("Odd-even: Odd ")
                odd_even = 'odd'
            if 1 <= int(a) <= 12:
                print("Group: 1-12")
                group_bet = 1
            elif 13 <= int(a) <= 24:
                print("Group: 13-24")
                group_bet = 2
            elif 25 <= int(a) <= 36:
                print("Group: 25- 36")
                group_bet = 3
        else:
            odd_even = "not available"
            group_bet = "not available"
        print("_____________________")
        if bet1:
            money = current_bets[1]
            if first_bet_value == a:
                print("Straight bet: Win")
                new_bet_one = money * 4
                print("Pay: %s * 4 = %s " % (money, new_bet_one))
                total += new_bet_one
            elif first_bet_value != a:
                print("Straight bet: Lose")
                print("Pay: 0")
                new_bet_one = 0
            current_bets[1] = new_bet_one
        # This is if rather than elif because I want all of those statements to run if the bet is on
        if bet2:
            money = current_bets[2]
            if second_bet_value == color:
                print("Color bet: Win")
                new_bet_two = money * 2
                print("Pay: %s * 2 = %s " % (money, new_bet_two))
                total += new_bet_two
                print("Total: %s$" % total)
            elif second_bet_value != color:
                print("Color bet: Lose")
                new_bet_two = 0
                print("Pay: 0")
            current_bets[2] = new_bet_two
        if bet3:
            money = current_bets[3]
            if third_bet_value == odd_even:
                print("Odd-even bet: Win")
                new_bet_three = money * 2
                print("Pay: %s * 2 = %s" % (money, new_bet_three))
                total += new_bet_three
                print("Total: %s" % total)
            else:
                print("Odd_even bet: Lose")
                new_bet_three = 0
                print("Pay: 0")
            current_bets[3] = new_bet_three
        if bet4:
            money = current_bets[4]
            if fourth_bet_value == group_bet:
                print("Group bet: Win")
                new_bet_four = money * 3
                print("Pay: %s * 3 = %s" % (money, new_bet_four))
                total += new_bet_four
                print("Total: %s$" % total)
            else:
                print("Group bet: Lose")
                new_bet_four = 0
                print("Pay: 0")
            current_bets[4] = new_bet_four
    print("Your final total: %s$" % total)
    graph.append(total)

# logo
print("Created by:")
print(
    Bcolors.red + "     ___  ___       _  \n    /   |/   |&    | | \n   / /|   /| |&    | | \n  / / |__/ | |& _  | | "
                  "\n / /       | |&| |_| | \n/_/ike     |_|&\_____/ake ")

# Asking the user whether they would like to read the instructions
print(Bcolors.NOTHING + '\n-------------------------------------------------------------------------')
i = input('Would you like to see the instructions before starting the game? ').lower()
if i == 'yes':  # if yes, instructions will appear
    while True:
        print('Instructions:')
        print('-----------------------------------')
        print('Chose one of the games to view...')
        print(' 1) Blackjack')
        print(' 2) Hot Slot Machine')
        print(' 3) Dices')
        print(' 4) Slot Machine')
        print(' 5) Roulette')
        print(' 6) Game Play')
        instruct = int(input('---------------------------------- \n'))
        if instruct == 1:
            print('Blackjack:')
            print('-------------------------------------------------------------------------------------')
            print(
                'In Blackjack the player is dealt 2 cards.\nHe uses those cards to make a hand up to 21.'
                '\nIf the player gets over 21 he loses!\nHe can chose to pick up more or stay!'
                '\nIf he stays he then compares with the dealers hand!\nWhoever is closest to 21 wins!')
            print('-------------------------------------------------------------------------------------')
        elif instruct == 2:
            print('Hot Slot Machine:')
            print('-------------------------------------------------------------------------------------')
            print(
                'In Flaming Hot Slot the computer randomizes 8 signs.\nFor every 3 signs in the same row, '
                'the user gains a point. \nAce equals to every sign \nThe more signs, the more points!'
                '\nThe more points, the bigger the win.\nIf you win, you have an '
                'option to go double by guessing red or black.\nHowever, if you lose the double you '
                'will lose everything.')
            print('-------------------------------------------------------------------------------------')
        elif instruct == 3:
            print('Dices:')
            print('-------------------------------------------------------------------------------------')
            print(
                'In Dices the user and dealer roll three times.\nWhoever has the highest per roll gets a point.'
                '\nIf the user gets 2 points out of 3 he wins!\nIf they tie, the user gets no money!'
                '\nIf the dealer wins the user loses all his money!')
            print('-------------------------------------------------------------------------------------')
        elif instruct == 4:
            print('Slot Machine:')
            print('-------------------------------------------------------------------------------------')
            print(
                'In slot machine, the user pulls a leaver.'
                '\nThe machine will then output 3 symbols, 1 at a time.'
                '\nIf all three match, the user wins double his bet!'
                '\nIf two match the user wins half his bet!'
                '\nIf there are no matches the user loses his bet and the house get it!')
            print('-------------------------------------------------------------------------------------')
        elif instruct == 5:
            print('Roulette:')
            print('-------------------------------------------------------------------------------------')
            print(
                'In roulette the user has a chance to bet on positions on the board.'
                '\nThey can bet on color, number, odd or even, and sequence (1-12).'
                '\nIf the ball on the roulette wheel lands on the position then the user wins!'
                '\nYou are not allowed to re-bet.'
                '\nIf it does not the user loses!')
            print('-------------------------------------------------------------------------------------')
        elif instruct == 6:
            print('Game Play:')
            print('-------------------------------------------------------------------------------------')
            print(
                'The game will ask you whether you want to sign up, in or delete an account.'
                '\nInputs must be typed as requested by the game! If there is no instructions on'
                '\nwhat to input, usually you must input "yes" or "no"!'
                '\nWhen signing up, makes sure to only user @gmail.com on the email section'
                '\nWe will send you emails!'
                '\nWe suggest reading the other game instructions to get an understanding on how'
                '\neach game works!')
            print('-------------------------------------------------------------------------------------')
        continue1 = input('\nWould you like to see other instructions? ')
        if continue1 == 'yes':
            pass
        else:
            print('Ok, have fun!')
            break
else:  # the program will start
    print('Ok have fun!')
print('-------------------------------------------------------------------------')

# Asking the user whether they want to sign in or sign up
sign_up = input(
    Bcolors.NOTHING + "Welcome! Would you like to sign up or sign in or delete account? (U/I/D) ").lower().lstrip()

# if the user wants to delete account
if sign_up == 'd':
    sign_in_user_name = input("Enter your username: ")
    if os.path.exists(sign_in_user_name + '.txt'):  # if username exists
        inFile = open(sign_in_user_name + '.txt', "r")
        w = inFile.readlines()
        # making w a list that I read from text file
        w = w[0].split('\n') + w[1].split('\n') + w[2].split('\n')
        for i in range(3):
            w.remove('')
        # This code will make sure the password is the same
        while True:
            sign_in_user_password = input("Enter your password: ")
            if sign_in_user_password != w[1]:
                print("That's wrong, try again\n")
                pass
            else:
                break
        inFile.close()
        email_delete()
        outFile = open(sign_in_user_name + '.txt', "w")
        outFile.close()
        os.remove(sign_in_user_name + '.txt')
        if os.path.exists(sign_in_user_name + 'graph.txt'):
            os.remove(sign_in_user_name + 'graph.txt')
        else:
            pass
        print('Account was deleted!')
    else:
        print('This account does not exist!')

# If the user wants to sign up the code takes input from the user and creates text file with that
elif sign_up == "u":
    while True:
        # Taking input
        file = 0
        new_user_name = input("Enter username: ")
        if os.path.exists(new_user_name + ".txt") == True:
            print('That username is taken! Start again!')
            pass
        else:
            new_user_password = input("Enter password: ")
            new_user_mail = input("Enter email(only gmail): ")
            if '@gmail.com' in new_user_mail:
                outFile = open(new_user_name + '.txt', "w")
                # writing the input
                outFile.write(new_user_name + '\n')
                outFile.write(new_user_password + '\n')
                outFile.write(new_user_mail + '\n')
                outFile.write("1000")
                print("Your registration is now complete. Run the program again and sign in!")
                email_sign_up()
                outFile.close()
                break
            else:
                while '@gmail.com' not in new_user_mail:
                    new_user_mail = input('Invalid email address! Try again! ')
                outFile = open(new_user_name + '.txt', "w")
                # writing the input
                outFile.write(new_user_name + '\n')
                outFile.write(new_user_password + '\n')
                outFile.write(new_user_mail + '\n')
                outFile.write("1000")
                print("Your registration is now complete. Run the program again and sign in!")
                email_sign_up()
                outFile.close()
                break

# if the user wants to sign in they enter their username and password and the program will compare
elif sign_up == "i":
    sign_in_user_name = input("Enter your username: ")
    if os.path.exists(sign_in_user_name + '.txt'):  # if username exists
        inFile = open(sign_in_user_name + '.txt', "r")
        w = inFile.readlines()
        # making w a list that I read from text file
        w = w[0].split('\n') + w[1].split('\n') + w[2].split('\n') + w[3].split('\n')
        count = w.count('')
        for i in range(int(count)):
            w.remove('')
        # This code will make sure the password is the same
        sign_in_user_password = input("Enter your password: ")
        if sign_in_user_password != w[1]:
            print("That's wrong, try again")
            while True:
                sign_in_user_password = input("Enter your password: ")
                if sign_in_user_password != w[1]:
                    print("That's wrong, try again")
                    pass
                else:
                    break

        # the start of the game if the password match
        if sign_in_user_password == w[1]:
            name = fancy_words = ["W", "e", "l", "c", "o", "m", "e", " " "t", "o", " " "t", "h", "e" + Bcolors.red,
                                  "\n _____       ___   _____   _   __   _   _____  "
                                  "\n/  ___|     /   | /  ___/ | | |  \ | | /  _  \ "
                                  "\n| |        / /| | | |___  | | |   \| | | | | | "
                                  "\n| |       / / | | \___  \ | | | |\   | | | | | "
                                  "\n| |___   / /  | |  ___| | | | | | \  | | |_| | "
                                  "\n\_____| /_/   |_| /_____/ |_| |_|  \_| \_____/ " + Bcolors.NOTHING]
            for char in name:
                print(char, end="")
                sys.stdout.flush()  # this flushes the buffer
                time.sleep(.1)
            total = float(w[3])  # total of user from text file (starting is $1000)
            print('\n \n---------------------------')
            print('| ' + str(sign_in_user_name) + "\'s balance: $%s" % total + ' |')  # printing balance of user
            print('---------------------------')
            graph.append(total)
            inFile.close()
            again = "no"
            other_game = 'yes'

            # And here is how we'll make the games happen
            while True:
                if again == "no" or other_game == 'yes':
                    while True:
                        try:
                            games = int(input(
                                "\nHere are some of the games we are offering: \n 1) Blackjack \n 2) Hot Slot Machine "
                                "\n 3) Dices \n 4) Roulette \n 5) Slot Machine \nPick one out of these! \n"))
                        except ValueError:
                            print("Only enter integers")
                        if 0 < games < 6:
                            break
                        else:
                            print("This is not one of the games!")

                # Blackjack
                if games == 1:
                    blackjack()

                # Flaming hot slot machine
                elif games == 2:
                    flaming_hot_slot()

                # Dices
                elif games == 3:
                    dices()

                # Roulette
                elif games == 4:
                    roulette()

                # Slot machine
                elif games == 5:
                    slot_machine()

                # after the user finishes a game
                if total > 0:
                    inFile = open(sign_in_user_name + '.txt', "w")
                    inFile.write(w[0] + '\n' + w[1] + '\n' + w[2] + '\n' + str(total))
                    inFile.close()
                    print('\n-------------------------------------')
                    again = input("Would you like to play again?(yes/no) ")
                    print('-------------------------------------')

                    # if they chose to play again
                    if again == "yes":
                        print("Good luck!")
                        other_game='no'

                    # if they don't
                    else:
                        print('-------------------------------------')
                        other_game = input("Would you like to try other game?(yes/no) ")
                        print('-------------------------------------\n')

                        # if they chose to not play any other games (done with the program)
                        if other_game == "no":
                            print("Your final total: $%s" % total)
                            if os.path.exists('scores.txt'):
                                inFile = open('scores.txt', 'r')
                                all_scores = inFile.readlines()
                                inFile.close()
                                new_list = []
                                fits = []
                                place = 0
                                for i in range(len(all_scores)):
                                    a = all_scores[i].strip('\n')
                                    new_list.append(float(a))
                                new_list.sort()
                                new_list.append(total)
                                new_list.sort()
                                # Now I'll do couple steps to find the user's rank in the list
                                list_length = len(new_list)
                                index = new_list.index(total)
                                rank = list_length - index

                                print("Your rank: %s" % rank)
                                outFile = open('scores.txt', 'w')
                                for b in range(len(new_list)):
                                    outFile.write(str(new_list[-b - 1]) + '\n')
                                outFile.close()
                                inFile = open('withnames.txt', 'r')
                                textFileList = inFile.readlines()
                                inFile.close()
                                outFile = open("withnames.txt", 'w')
                                textFileList.insert(rank - 1, str(total) + ' ' + sign_in_user_name + '\n')
                                for o in range(len(textFileList)):
                                    outFile.write(textFileList[o])
                                outFile.close()
                                if len(textFileList) > 5:
                                    print("TOP FIVE\n-----------------------")
                                    time.sleep(1)
                                    for rank in range(5):
                                        print(str(rank + 1) + '. ' + textFileList[rank])
                                        time.sleep(0.2)

                            else:
                                outFile = open('scores.txt', 'w')
                                outFile.write(str(total))
                                print("Your rank: 1")
                                outFile.close()
                                outFile = open('withnames.txt', 'w')
                                outFile.write(str(total) + ' ' + sign_in_user_name + '\n')
                            if os.path.exists(sign_in_user_name + "graph.txt") == False:
                                outFile = open(sign_in_user_name + "graph.txt", 'a')
                                outFile.write(sign_in_user_name + '\'s progress:\n')
                            else:
                                outFile = open(sign_in_user_name + "graph.txt", 'a')
                            for i in range(len(graph)):
                                outFile.write(str(graph[i]) + '\n')
                            outFile.close()
                            email_progress()
                            break

                # if the user loses all his money
                else:
                    print("You lost all your money. We're officially kicking you out. ")
                    kicked_out = True
                    email_delete()
                    os.remove(sign_in_user_name + '.txt')
                    break
                if kicked_out:
                    break
    else:  # if there is no such account
        print('There is no such account! Please start again and sign up!')

else:  # if the user inputs invalid character (input is not u, d or i)
    print('Invalid input! Start again!')
