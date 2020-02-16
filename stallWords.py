def getStall(text):
    text = text.lower()
    te = list(text.split())

    uh = 0
    um = 0
    kinda = 0
    like = 0
    sure = 0
    stuff = 0
    counter = 0
    for i in te:
        if i == "um":
            um += 1
        if i == "kinda":
            kinda += 1
        if i == "like":
            like += 1
        if i == "sure":
            sure += 1
        if i == "uh":
            uh += 1
        counter += 1
    mylist = [um, kinda, like, sure, stuff, uh]
    return mylist