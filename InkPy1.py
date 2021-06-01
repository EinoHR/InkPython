import re
import time

inkfile = open("ShopTest.ink")
inkfiletext = inkfile.read()
lines = inkfile.readlines()


# print(inkfiletext)

# with open("ShopTest.ink") as i:
#     for line in i:
#         print(line)
#         time.sleep(0.1)

#Finds knots
def findknot(knot):
    line_number = 0
    knotline = -1

    with open("ShopTest.ink") as i:
        for line in i:
            line_number += 1
            if "=="+knot+"==" in line:
                knotline = line_number
                return(knotline)

def playknot(knotline):
    with open("ShopTest.ink") as i:
        ilines = i.readlines()
        print(ilines[knotline])

        choiceline = knotline

        while ilines[choiceline] != '\n':
            choiceline += 1
            print(ilines[choiceline])

        if ilines[knotline].startswith('+' or '*'):
            if re.match(r'(.)(?P<text>.*)\[(?P<previewtext>.*)\](?P<fulltext>.*)', ilines[knotline+1]):
                option = re.match(r'(.)(?P<text>.*)\[(?P<previewtext>.*)\](?P<fulltext>.*)', ilines[knotline+1])
                print(option.group("previewtext"))
            elif re.match(r'(.)(?P<text>.*)(?P<fulltext>.*)', ilines[knotline+1]):
                option = re.match(r'(.)(?P<text>.*)(?P<fulltext>.*)', ilines[knotline+1])
                print(option.group("text"))

        input()




with open("ShopTest.ink") as i:
    for line in i:
        # print(line)

        # Parses variables
        if re.match(r'VAR (?P<varname>.*) = "(?P<var>.*)"', line):
            var = re.match(r'VAR (?P<varname>.*) = "(?P<var>.*)"', line)
            var.group("varname")
            globals()[var.group("varname")] = var.group("var")

            # print(var.group("varname") + " = " + var.group("var"))

        elif re.match(r'VAR (?P<varname>.*) = (?P<var>.*)', line):
            var = re.match(r'VAR (?P<varname>.*) = (?P<var>.*)', line)
            var.group("var")
            globals()[var.group("varname")] = float(var.group("var"))

            # print(var.group("varname") + " = " + var.group("var"))

        #Find diverts
        if re.match(r'-> DONE', line):
            print("End of story")

        elif re.match(r'->(\w)', line):
            divert = re.match(r'->(?P<goto>\w*)', line)
            goto = divert.group("goto")

            knotline = findknot(goto)
            playknot(knotline)
            # print(knotline)
        elif re.match(r'-> (\w)', line):
            divert = re.match(r'-> (?P<goto>\w*)', line)
            goto = divert.group("goto")

            knotline = findknot(goto)
            playknot(knotline)
            # print(knotline)