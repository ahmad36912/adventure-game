from time import sleep
score = 100
print("score: " + str(score))
sleep(2)
print("you are in formula e race and have two choices: ")
sleep(2)
print("1: to have VIP but no budget for snacks 2: have regular but snacks")
sleep(2)
first_choosing = input("1: VIP 2: budget")
def VIP():
    scor = score
    sleep(2)
    print("you sit in the VIP but you are hungry")
    sleep(2)
    print("2 hours left for the race")
    sleep(2)
    print("1: go and bring snacks 2: stay here in order to watch training")
    sleep(2)
    second_VIP_choosing = input("go to home to bring snacks?")
    sleep(2)
    if second_VIP_choosing == str("1"):
        sleep(2)
        print("you eat your snacks but the place is crowded and 30 minutes until the race starts")
        scor = scor - 5
        sleep(2)
        print("score: " + str(scor))
    if second_VIP_choosing == str("2"):
        sleep(2)
        print("you are watching training but no snacks")
def budget():
    sco = score
    print("score: " + str(sco))
    sleep(2)
    print("you eat your snacks but you don't have legroom")
    sleep(2)
    print("2 hours left for the race")
    sleep(2)
    print("1: go and have a pillow 2: stay here in order to keep your chair")
    sleep(2)
    second_budget_choosing = input("go and bring a pillow?")
    sleep(2)
    if second_budget_choosing == str("1"):
        sleep(2)
        print("you now have a pillow but someone took your chair")
        sleep(2)
        print("you have two choices: ")
        sleep(2)
        third_budget_choosing = input("1: to fight with the man to set quickly 2: to talk to service but wait")
        if third_budget_choosing == 1:
            sco = sco - 15
            print("score: " + str(sco))
            sleep(2)
            print("you sit after a fight but the adiminstration wanted you because of the fight")
            sleep(2)
            fourth_budget_choosing = input("1: to have and argument because it's your chair and watch what is left from the race 2: to go there but don't watch the race")

    if second_budget_choosing == str("2"):
        sleep(2)
        print("you are watching the training but no legroom")


if first_choosing != str("1") and first_choosing != str("2"):
    print("please choose one to complete the game")
    sleep(2)
    print("you are in formula e race and have two choices: ")
    sleep(2)
    print("1-to have VIP but no budget for snacks 2-have regular but snacks")
    sleep(2)
    first_choosing = input("1: VIP 2: budget")


if first_choosing == str("1"):
    VIP()


if first_choosing == str("2"):
    budget()


