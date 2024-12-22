import random, math
# Your code here

def chat ():
    cowerkers =  ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee  = cowerkers[math.floor(random.random() * 4)]
    print(f"Chatting with {chatee} ...")
    print("Done")


def getWater ():
    print("Getting water ...")
    print("That was refreshing")


def useSocialMedia ():
    socialMedia = ["Facebook", "Twitter", "Youtube", "Reddit"]
    choice = socialMedia[math.floor(random.random() * 4)]
    print(f"Using {choice} ...")
    print("Done")

