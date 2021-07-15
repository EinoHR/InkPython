import InkPy as ink

inkjsonpath = "./ShopTest.json"

print(ink.init(inkjsonpath))

while ink.CanContinue == True or ink.NeedsChoice == True:
    if ink.CanContinue == True:
        print(ink.Continue(inkjsonpath))

    if ink.NeedsChoice == True: 
        choiceindex = 1
        print("Choose one")
        for choice in ink.choices:
            print(str(choiceindex)+": "+choice)
            choiceindex += 1
        chosen = int(input())-1
        print() 
        print(ink.Choose(inkjsonpath, chosen))

    # print(ink.CanContinue)
    # print(ink.NeedsChoice)
