import re

inkfilepath = "ShopTest.ink"
# inkfiletext = inkfile.read()
# lines = inkfile.readlines()


# print(inkfiletext)

# with open(inkfilepath) as i:
#     for line in i:
#         print(line)
#         time.sleep(0.1)

#Finds knots
def findknot(knot):
    line_number = 0
    knotline = -1

    with open(inkfilepath) as i:
        for line in i:
            line_number += 1
            if "=="+knot+"==" in line:
                knotline = line_number
                return(knotline)

def playknot(knotline):
    with open(inkfilepath) as i:
        ilines = i.readlines()
        print(ilines[knotline])

        # Finds choicelines
        lastchoiceline = knotline

        while ilines[lastchoiceline] != '\n':
            if not lastchoiceline == None:
                lastchoiceline += 1
                # print(lastchoiceline)
                # print(ilines[lastchoiceline])

        totalchoicelines = lastchoiceline-knotline-1

        optionnumber = 0

        for lineiter in range(totalchoicelines):
            # print(ilines[lineiter])
            lineiter = lineiter+knotline
            if ilines[lineiter].startswith('+' or '*'):
                # print(ilines[lineiter]) 
                if re.match(r'([+]|[*])(?P<text>.*)\[(?P<previewtext>.*)\](?P<fulltext>.*)', ilines[lineiter]):
                    option = re.match(r'(.)(?P<text>.*)\[(?P<previewtext>.*)\](?P<fulltext>.*)', ilines[lineiter])
                    optionnumber += 1
                    if re.match(r'-> DONE', ilines[lineiter+1]):
                        print("End of story")
                        return
                    elif re.match(r'->(\w)', ilines[lineiter+1]):
                        divert = re.match(r'->(?P<goto>\w*)', ilines[lineiter+1])
                        goto = divert.group("goto")


                        # knotline = findknot(goto)
                        # playknot(knotline)
                        # # print(knotline)
                    elif re.match(r'-> (\w)', ilines[lineiter+1]):
                        divert = re.match(r'-> (?P<goto>\w*)', ilines[lineiter+1])
                        goto = divert.group("goto")

                        # knotline = findknot(goto)
                        # playknot(knotline)
                        # # print(knotline

                    globals()["option"+str(optionnumber)] = goto
                    globals()["optionprevtext"+str(optionnumber)] = option.group("text") + option.group("previewtext")
                    globals()["optionfulltext"+str(optionnumber)] = option.group ("text") + option.group("fulltext")
                    print(str(optionnumber) + ": " + option.group("previewtext"))
                    # print(globals()["option"+str(optionnumber)]) 
                elif re.match(r'([+]|[*])(?P<text>.*)', ilines[lineiter]):
                    option = re.match(r'(.)(?P<text>.*)', ilines[lineiter])
                    optionnumber += 1
                    print(str(optionnumber) + ": " + option.group("text"))
                    if re.match(r'-> DONE', ilines[lineiter+1]):
                        print("End of story")
                        return
                    elif re.match(r'->(\w)', ilines[lineiter+1]):
                        divert = re.match(r'->(?P<goto>\w*)', ilines[lineiter+1])
                        goto = divert.group("goto")

                        # knotline = findknot(goto)
                        # playknot(knotline)
                        # # print(knotline)
                    elif re.match(r'-> (\w)', ilines[lineiter+1]):
                        divert = re.match(r'-> (?P<goto>\w*)', ilines[lineiter+1])
                        goto = divert.group("goto")
                        # knotline = findknot(goto)
                        # playknot(knotline)
                        # # print(knotline

                    globals()["option"+str(optionnumber)] = goto
                    globals()["optionfulltext"+str(optionnumber)] = option.group ("text")
                    print(str(optionnumber) + ": " + option.group("text"))
        print("---")
        chosenoption = input("Press the number of your choice and hit enter. \n")
        chosenknot = findknot(globals()["option"+str(chosenoption)])
        print("---")
        print(globals()["optionfulltext"+str(chosenoption)])
        playknot(chosenknot)

def startink():
    with open(inkfilepath) as i:
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
            elif re.match(r'-> DONE', line):
                print("End of story")
                return

            elif re.match(r'->(\w)', line):
                divert = re.match(r'->(?P<goto>\w*)', line)
                goto = divert.group("goto")

                knotline = findknot(goto)
                playknot(knotline)
                return
                # print(knotline)
            elif re.match(r'-> (\w)', line):
                divert = re.match(r'-> (?P<goto>\w*)', line)
                goto = divert.group("goto")

                knotline = findknot(goto)
                playknot(knotline)
                return
                # print(knotline)


startink()