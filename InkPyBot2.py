import InkPy

# Not yet a discord bot, just testing using the InkPy module using this.

inkfilepath = "ShopTest.ink"

InkPy.startink(inkfilepath)

print(InkPy.currenttext)

while InkPy.storycancontinue:
    lasttext = InkPy.currenttext
    continuefunc = InkPy.Continue(inkfilepath)
    if InkPy.currenttext != lasttext:
        print(InkPy.currenttext)

while True:
    if InkPy.storyneedschoice == True:
        print("Test")
        for i in range(InkPy.numofoptions):
            print(i)
            print(InkPy.globals()["optionfulltext"+str(i)])
        # InkPy.chosenoption = 1