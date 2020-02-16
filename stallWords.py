
def getStall(text):
    text = text.lower()
    te = list(text.split())
    uh = 0
    um = 0
    kinda = 0
    like = 0
    hate = 0
    fuck = 0
    bitch = 0
    shit = 0
    damn = 0
    dammit = 0
    perfectionist = 0
    sure = 0
    stuff = 0
    fired = 0
    counter = 0

    for i in te:
        if i == "um":
            um += 1
        if i == "kinda":
            kinda += 1
        if i == "like":
            like += 1
        if i == "fuck":
            fuck += 1
        if i == "bitch":
            bitch += 1
        if i == "damn":
            damn += 1
        if i == "shit":
            shit += 1
        if i == "dammit":
            dammit += 1
        if i == "perfectionist":
            perfectionist += 1
        if i == "sure":
            sure += 1
        if i == "fired":
            fired += 1
        if i == "uh":
            uh += 1
        counter += 1
    mylist = [um, kinda, like, hate, fuck, bitch, shit, damn, dammit, perfectionist, sure, stuff, fired]
    return mylist
