import re
import string

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

        lastknotline = knotline-1

        while ilines[lastknotline] != '\n':
            if not lastknotline == None:
                lastknotline += 1
                # print(lastknotline)
                # print(ilines[lastknotline])

        totalknotlines = lastknotline-knotline-1

        optionnumber = 0
        for lineiter in range(totalknotlines):
            lineiter = lineiter+knotline
            # print(ilines[lineiter])

            # Finds textlines
            if not ilines[lineiter].startswith(("+","*","-","~")):
                # Replaces variables with the variable contents
                if re.search(r'{(?P<varname>\w+)}', ilines[lineiter]):
                    varline = re.search(r'{(?P<varname>\w+)}', ilines[lineiter])
                    varcontent = globals()[varline.group("varname")]
                    var = "{"+str(varline.group("varname"))+"}"
                    patched_line = ilines[lineiter].replace(var, varcontent)
                    print(patched_line)
                else:
                    print(ilines[lineiter])

            # Finds choicelines
            elif ilines[lineiter].startswith('+' or '*'):
            
                # print(ilines[lineiter])

                # Finds choicelines
                if re.match(r'([+]|[*])(?P<text>.*)\[(?P<previewtext>.*)\](?P<fulltext>.*)', ilines[lineiter]):
                    option = re.match(r'(.)(?P<text>.*)\[(?P<previewtext>.*)\](?P<fulltext>.*)', ilines[lineiter])
                    optionnumber += 1
                    goto = None #TODO this should be fixed to be non-specific to the testing .ink file, comment line to see error.
                    
                    for divertiter in range(totalknotlines):
                        divertiter = divertiter+knotline+1
                        # print(ilines[divertiter])
                        if ilines[divertiter].startswith('-'):
                            if re.match(r'-> DONE', ilines[divertiter]):
                                goto = None

                            elif re.match(r'->(\w)', ilines[divertiter]):
                                divert = re.match(r'->(?P<goto>\w*)', ilines[divertiter])
                                goto = divert.group("goto")


                                # knotline = findknot(goto)
                                # playknot(knotline)
                                # print("Found")
                            elif re.match(r'-> (\w)', ilines[divertiter]):
                                divert = re.match(r'-> (?P<goto>\w*)', ilines[divertiter])
                                goto = divert.group("goto")

                                # knotline = findknot(goto)
                                # playknot(knotline)
                                # print("Found")
                            
                            else:
                                # print("Not found")
                                goto = None
                    

                    


                    globals()["option"+str(optionnumber)] = goto
                    globals()["optionprevtext"+str(optionnumber)] = option.group("text") + option.group("previewtext")
                    globals()["optionfulltext"+str(optionnumber)] = option.group ("text") + option.group("fulltext")

                    # Replaces variables with the variable contents 
                    if re.search(r'{(?P<varname>\w+)}', globals()["optionprevtext"+str(optionnumber)]):
                        # print("Found in prev")
                        varline = re.search(r'{(?P<varname>\w+)}', globals()["optionprevtext"+str(optionnumber)])
                        varcontent = globals()[varline.group("varname")]
                        var = "{"+str(varline.group("varname"))+"}"
                        globals()["optionprevtext"+str(optionnumber)] = globals()["optionprevtext"+str(optionnumber)].replace(var, varcontent)

                    if re.search(r'{(?P<varname>\w+)}', globals()["optionfulltext"+str(optionnumber)]):
                        # print("Found in full")
                        varline = re.search(r'{(?P<varname>\w+)}', globals()["optionfulltext"+str(optionnumber)])
                        varcontent = str(globals()[varline.group("varname")])
                        var = "{"+str(varline.group("varname"))+"}"
                        globals()["optionfulltext"+str(optionnumber)] = globals()["optionfulltext"+str(optionnumber)].replace(var, varcontent)

                    print(str(optionnumber) + ": " + globals()["optionprevtext"+str(optionnumber)])
                    # print(globals()["option"+str(optionnumber)]) 
                elif re.match(r'([+]|[*])(?P<text>.*)', ilines[lineiter]):
                
                    option = re.match(r'(.)(?P<text>.*)', ilines[lineiter])
                    optionnumber += 1
                    # print(str(optionnumber) + ": " + option.group("text"))

                    for divertiter in range(totalknotlines):
                        divertiter = divertiter+knotline+1
                        # print(ilines[divertiter])
                        if ilines[divertiter].startswith('-'):
                            if re.match(r'-> DONE', ilines[divertiter]):
                                goto = None

                            elif re.match(r'->(\w)', ilines[divertiter]):
                                divert = re.match(r'->(?P<goto>\w*)', ilines[divertiter])
                                goto = divert.group("goto")


                                # knotline = findknot(goto)
                                # playknot(knotline)
                                # print("Found")
                            elif re.match(r'-> (\w)', ilines[divertiter]):
                                divert = re.match(r'-> (?P<goto>\w*)', ilines[divertiter])
                                goto = divert.group("goto")

                                # knotline = findknot(goto)
                                # playknot(knotline)
                                # print("Found")
                            
                            else:
                                # print("Not found")
                                goto = None

                    globals()["option"+str(optionnumber)] = goto
                    globals()["optionfulltext"+str(optionnumber)] = option.group("text")
                    globals()["optionprevtext"+str(optionnumber)] = option.group("text") 

                    # Replaces variables with the variable contents 
                    if re.search(r'{(?P<varname>\w+)}', globals()["optionfulltext"+str(optionnumber)]):
                        # print("Found in text")
                        varline = re.search(r'{(?P<varname>\w+)}', globals()["optionfulltext"+str(optionnumber)])
                        varcontent = str(globals()[varline.group("varname")])
                        var = "{"+str(varline.group("varname"))+"}"
                        globals()["optionfulltext"+str(optionnumber)] = globals()["optionfulltext"+str(optionnumber)].replace(var, varcontent)

                    print(str(optionnumber) + ": " + globals()["optionprevtext"+str(optionnumber)])


            # Changes variables (Cannot do math) TODO
            elif ilines[lineiter].startswith('~'):
                if re.match(r'~ (?P<varname>\w+) = (?P<varnewstate>\w+)', ilines[lineiter]):
                    varchangeline = re.match(r'~ (?P<varname>\w+) = (?P<varnewstate>\w+)', ilines[lineiter])
                    varname = varchangeline.group("varname")
                    varnewstate = varchangeline.group("varnewstate")
                    globals()[varname] = varnewstate
            # Handles lone diverts (Not working) TODO
            # elif ilines[lineiter].startswith('-'):
            #     if re.match(r'-> DONE', ilines[lineiter]):
            #         print("End of story")
            #         return
            #     elif re.match(r'->(\w)', ilines[lineiter]):
            #         divert = re.match(r'->(?P<goto>\w*)', ilines[lineiter])
            #         goto = divert.group("goto")

            #         knotline = findknot(goto)
            #         playknot(knotline)
            #     elif re.match(r'-> (\w)', ilines[lineiter+1]):
            #         divert = re.match(r'-> (?P<goto>\w*)', ilines[lineiter])
            #         goto = divert.group("goto")
            #         knotline = findknot(goto)
            #         playknot(knotline)

        print("---")
        chosenoption = input("Press the number of your choice and hit enter. \n")
        # print(globals()["option"+str(chosenoption)])
        if globals()["option"+str(chosenoption)] != None:
            chosenknot = findknot(globals()["option"+str(chosenoption)])
        else:
            print("---")
            print("End of story")
            return
        print("---")
        print(globals()["optionfulltext"+str(chosenoption)])
        playknot(chosenknot)

def startink():
    with open(inkfilepath) as i:
        for line in i:
            # print(line)

            # Deals with variables at the start
            if re.match(r'VAR (?P<varname>.*) = "(?P<var>.*)"', line):
                var = re.match(r'VAR (?P<varname>.*) = "(?P<var>.*)"', line)
                var.group("varname")
                globals()[var.group("varname")] = var.group("var")

                # print(var.group("varname") + " = " + var.group("var"))

            elif re.match(r'VAR (?P<varname>.*) = (?P<var>.*)', line):
                var = re.match(r'VAR (?P<varname>.*) = (?P<var>.*)', line)
                var.group("var")
                globals()[var.group("varname")] = var.group("var")

                # print(var.group("varname") + " = " + var.group("var"))

            # Deals with diverts at the start
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


            elif line != '\n':
                print(line)


startink()