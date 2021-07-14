import json

inkjsonpath = open('./ShopTest.json', "r", encoding="utf-8-sig")
inkjson = json.loads(inkjsonpath.read())

inkroot = inkjson["root"]

def storyvars():
    globaldecl = inkroot[2]["global decl"]
    i = 0
    for item in globaldecl:
        if item == "str":
            tempvar = globaldecl[i+1][1 : : ]
            exec("storyvars."+globaldecl[i+3].get("VAR=") +"="+ '"'+tempvar+'"')
        elif str(item).isnumeric():
            tempvar = item
            exec("storyvars."+globaldecl[i+1].get("VAR=") +"="+str(tempvar))

        i += 1

storyvars()
print(storyvars.playername)