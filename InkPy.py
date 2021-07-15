import json

def init(inkjsonpath):
    inkjsonfile = open(inkjsonpath, "r", encoding="utf-8-sig")
    inkjson = json.loads(inkjsonfile.read())
    inkroot = inkjson["root"]
    global ContinueTo
    global CanContinue
    global choices
    global NeedsChoice
    global currentKnot

    storyvars(inkjsonpath)

    global ContinueTo
    global CanContinue
    global choices
    global NeedsChoice
    global currentKnot
    choices = [] 
    returntext = ""
    startsection = inkroot[0]
    for item in startsection:
        if str(item).startswith("^"):
            returntext += item[1 : : ]
        elif str(item).startswith("{"):
            if "->" in item:
                ContinueTo = item["->"]
                CanContinue = True
                NeedsChoice = False
    return(returntext)

def storyvars(inkjsonpath):
    inkjsonfile = open(inkjsonpath, "r", encoding="utf-8-sig")
    inkjson = json.loads(inkjsonfile.read())
    inkroot = inkjson["root"]
    global ContinueTo
    global CanContinue
    global choices
    global NeedsChoice
    global currentKnot

    globaldecl = inkroot[2]["global decl"]
    i = 0
    for item in globaldecl:
        if item == "str":
            tempvar = globaldecl[i+1][1 : : ]
            exec(f"storyvars.{globaldecl[i+3].get('VAR=')}='{str(tempvar)}'")
        elif str(item).isnumeric():
            tempvar = item
            exec(f"storyvars.{globaldecl[i+1].get('VAR=')}='{str(tempvar)}'")
        i += 1


def Continue(inkjsonpath):
    inkjsonfile = open(inkjsonpath, "r", encoding="utf-8-sig")
    inkjson = json.loads(inkjsonfile.read())
    inkroot = inkjson["root"]
    global ContinueTo
    global CanContinue
    global choices
    global NeedsChoice
    global currentKnot

    CanContinue = False
    currentKnot = inkroot[2][ContinueTo][0]
    returntext = ""
    choices = [] # Note sure what's wrong with this
    i = 0
    for item in currentKnot:
        # print(item)
        if str(item).startswith("^"):
            if currentKnot[i-2] != "ev":
                returntext += item[1 : : ]
        elif str(item) == "ev":
            if str(currentKnot[i+1]).startswith("{"):
                if "VAR?" in currentKnot[i+1]:
                    tempvar = ""
                    ldict = {}
                    exec("tempvar = storyvars.{}".format(currentKnot[i+1]['VAR?']),globals(),ldict)
                    tempvar = ldict['tempvar']
                    returntext += str(tempvar)

            elif str(currentKnot[i+1]) == "str":
                choices.append(currentKnot[i+2][1 : : ])
                CanContinue = False
                NeedsChoice = True
        # elif str(currentKnot[i]).startswith("{"): 
        #     if "VAR=" in currentKnot[i]:
        #         tempvar = ""
        #         ldict = {}
        #         TODO dynamically change variable mid script. And generally better variable handling.
        #         tempvar = ldict['tempvar']
        #         exec("{} = tempvar".format(currentKnot[i]['VAR=']),globals(),ldict)
        elif str(item) == "\n":
            returntext += "\n"
        elif str(item).startswith("{"):
            if "->" in item:
                ContinueTo = item["->"]
                CanContinue = True
                NeedsChoice = False

        i += 1
    return(returntext)

def Choose(inkjsonpath, chosen):
    inkjsonfile = open(inkjsonpath, "r", encoding="utf-8-sig")
    inkjson = json.loads(inkjsonfile.read())
    inkroot = inkjson["root"]
    global ContinueTo
    global CanContinue
    global choices
    global NeedsChoice
    global currentKnot

    returntext = ""
    i = 0
    choicedict = currentKnot[-1]
    for item in choicedict.get(f"c-{chosen}"):
        # print(item)
        if str(item).startswith("^"):
            returntext += item[1 : : ]
        elif str(item) == "\n":
            returntext += "\n"
        elif str(item) == "ev":
            if str(choicedict.get(f"c-{chosen}")[i+1]).startswith("{"):
                if "VAR?" in choicedict.get(f"c-{chosen}")[i+1]:
                    tempvar = ""
                    ldict = {}
                    exec("tempvar = storyvars.{}".format(choicedict.get(f"c-{chosen}")[i+1]['VAR?']),globals(),ldict)
                    tempvar = ldict['tempvar']
                    returntext += str(tempvar)
        elif str(item).startswith("{"):
            if "->" in item:
                ContinueTo = item.get("->")
                CanContinue = True
                NeedsChoice = False
        i += 1

    return(returntext)