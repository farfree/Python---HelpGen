# coding=UTF-8

import htmlfiles as hf

helpKey = []
caseKey = {}
caseTitle = {}
jshelp = set()

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_toend( s, first):
    try:
        start = s.index( first ) + len( first )
        return s[start:]
    except ValueError:
        return ""

#search keys in all htmls file
def findKey ():
    for files in hf.htmlfiles:
        file = open(hf.HTMLPATH + files, 'r', encoding='UTF-8')
        while True:
            line = file.readline()
            if not line: break
            if "ColTop" in line or "TableTop" in line:
                #print (line)
                #remove all space
                line = "".join(line.split());
                cnt = line.count(',')

                if cnt == 2:
                    line = find_between(line, '),\'', '\')');
                else:
                    line = find_between(line, '),\'', '\',');

                helpKey.append(line)
        file.close()

    for a in helpKey:
        print ('\"' + a + '\"')

#Search all cases in ng_help.js and compare with keys found for me
def findCase():
    file = open('ng_help.js', 'r', encoding='UTF-8')
    while True:
        line = file.readline()
        if not line: break
        if "case" in line:
            #print (line)
            key = find_between(line, '"', '"')
            if key in hf.helpKey:
                caseKey[key] = [file.readline().strip(), file.readline().strip()]
                #print ('"{0}": ["{1}", "{2}"],'.format(key, caseKey[key][0], caseKey[key][1]))
    file.close()

#generate new format of case and langH() for title and shows
def genCase():
    for key in caseKey:
        langKey = find_between(caseKey[key][0], '_', '_')
        if 0 == len(langKey):
            langKey = find_between(caseKey[key][0], '_', '.')
        langString = find_between(caseKey[key][1], '"', '"')
        caseTitle[key] = langString;
        caseKey[key][0] = caseKey[key][0].replace('.html', '.js')
        caseKey[key][1] = 'strTitle = langH("{0}", "top{1}");'.format(langKey, key)
        jshelp.add(find_between(caseKey[key][0], '"', '#'))
        #case "policyClassConfigInfo":
        #strHelp = "help_diffserv.js#policy_clss_info";
        #strTitle = langH('qos','topDiffPolicy');
        #topCoS:"CLASS OF SERVICE (CoS) HELP",
        #break;
        print ("case \"{0}\":".format(key))
        print ("  " + caseKey[key][0])
        print ("  " + caseKey[key][1])
        print ("  break;")

def getSecondTitle():
    for key in caseKey:
        langKey = find_between(caseKey[key][0], '_', '_')
        if '#' in langKey:
            langKey = find_between(caseKey[key][0], '_', '.')
        langString = find_between(caseKey[key][1], '"', '"')

        helpfile = find_between(caseKey[key][0], '"', '#').replace('js', 'html')
        searchkey = find_between(caseKey[key][0], '#', '"')
        #print (searchkey)
        file = open(hf.HELPPATH + helpfile)
        while True:
            line = file.readline()
            if not line: break
            if searchkey in line:
                msg = find_between(line, "a>", "</h2>")
                #print ('  tit{0}:"{1}"'.format(key, msg))
                #print ("langH('{0}':'{1})".format(langKey, msg))
                caseKey[key].append("tit"+key)
                #print (key + " ----- " + caseKey[key][2])
                break;
        file.close()

def genCaseToHelpTitle():
    file = open('ng_help.js', 'r', encoding='UTF-8')
    while True:
        line = file.readline()
        if not line: break
        if "case" in line:
            key = find_between(line, '"', '"')
            if key in hf.helpKey:
                helpfile = find_between(file.readline().strip(), '"', '#')
                title = find_between(file.readline().strip(), '= ', ';')
                #caseKey[key] = [helpfile, title]
                js = open(hf.HELPPATH+helpfile, 'a', encoding='UTF-8')
                js.write("\n/* Help for {0} */\n".format(key));
                js.write("HELP_HR() +\n");
                js.write("HELP_H2('{0}', langH('fuck','{1}')) +\n".format(key, caseKey[key][2]));
                js.write("\n\n")
                js.close()
    file.close()

def genEOF():
    for files in hf.jshelp:
        js = open(hf.HELPPATH + files, 'a')
        js.write("HELP_END()\n")
        js.close()

#findKey()
#findCase()
#getSecondTitle()
#genCase()
#genCaseToHelpTitle()
#genEOF()


paradata = []
navidata = []
seldata = []
configdata = []
nonconfigdata = []
buttondata = []
langKey = "aclwizard"
sectionKey = ""

def supressKey (key):
    skey = "".join(key.split(" "))
    skey = "".join(skey.split("&"))
    skey = "".join(skey.split("="))
    skey = "".join(skey.split("/"))
    skey = "".join(skey.split("("))
    skey = "".join(skey.split(")"))
    skey = "".join(skey.split(":"))
    skey = "".join(skey.split("\""))
    skey = "".join(skey.split("-"))
    skey = sectionKey + skey
    return skey;

def getFullStr (file, line, end):
    while end not in line:
        line = "".join(line.split("\n"))
        line += " " + file.readline().strip()
    return line

def innerStr(fuck):
    print (fuck)
    while "<b>" in fuck:
        key = find_between(fuck, "<b>", "</b>")
        skey= supressKey(key);
        msg = find_between(fuck, "</b>", "</li>")
        if 0 == len(msg):
            msg = find_toend(fuck, "</I>")
        print ('  txt{0}:"{1}",'.format(skey, key));

        if 0 != len(msg):
            print ('  txt{0}Msg:"{1}",'.format(skey, msg));
            print ("HELP_UL_LI_B_PARAM(langH('{0}', 'txt{1}'), langH('{0}', 'txt{2}Msg')) +".format(langKey, skey, skey))
        else:
            print ("HELP_LI_I_B(langH('{0}', 'txt{1}')) +".format(langKey, skey))
        if "</li>" in fuck:
            s = fuck.index("</li>") + len("</li>")
            fuck = fuck[s:]
        else:
            break

def processConfigLine (line, paType):
    key = find_between(line, "<li><b>", "</b>")
    skey = supressKey(key)
    msg = find_between(line, "- ", "</li>")
    msg = msg.replace("\"", "'")
    if "<UL>" in msg:
        remain = msg[msg.index("<UL>"):]
        msg = msg[0:msg.index("<UL>")]
        innerStr(remain)
    print ('  txt{0}:"{1}",'.format(skey, key));
    print ('  txt{0}Msg:"{1}",'.format(skey, msg));
    ggg = "HELP_LI_PARAM(langH('{2}','txt{0}'), langH('{2}','txt{1}Msg')) +".format(skey, skey, langKey)
    if 0 == paType:
        configdata.append(ggg)
    elif 1 == paType:
        nonconfigdata.append(ggg)
    elif 2 == paType:
        seldata.append(ggg)
    elif 3 == paType:
        navidata.append(ggg)

def processParaLine (line):
    global paraCnt
    msg = find_between(line, "<p>", "</p>")
    key = "txt{0}ParaMsg".format(sectionKey)
    print ('  {0}:"{1}",'.format(key, msg));
    paradata.append("HELP_P(langH('{0}','{1}')) + ".format(langKey, key))

def processButtonLine (line):
    key = find_between(line, "<b>", "</b>")
    msg = find_between(line, "- ", "</li>")
    if "Apply" == key:
        buttondata.append("HELP_UL_LI_BTN_APPLY() +")
    elif "Cancel" == key:
        buttondata.append("HELP_UL_LI_BTN_CANCEL() +")
    elif "Update" == key:
        print ('  txt{2}{0}Msg:"{1}",'.format(key, msg, sectionKey));
        buttondata.append("HELP_UL_LI_BTN_UPDATE(langH('{0}','txt{1}{2}Msg')) +".format(langKey, sectionKey, key))
    elif "Add" == key:
        print ('  txt{2}{0}Msg:"{1}",'.format(key, msg, sectionKey));
        buttondata.append("HELP_UL_LI_BTN_ADD(langH('{0}','txt{1}{2}Msg')) +".format(langKey, sectionKey, key))
    elif "Delete" == key:
        print ('  txt{2}{0}Msg:"{1}",'.format(key, msg, sectionKey));
        buttondata.append("HELP_UL_LI_BTN_DEL(langH('{0}','txt{1}{2}Msg')) +".format(langKey, sectionKey, key))
    elif "Clear" == key:
        print ('  txt{2}{0}Msg:"{1}",'.format(key, msg, sectionKey));
        buttondata.append("HELP_UL_LI_BTN_CLEAR(langH('{0}','txt{1}{2}Msg')) +".format(langKey, sectionKey, key))

def printCode(data, header):
    print ("")
    if len(data):
        print (header+"(")
        for d in data:
            if d == data[-1]:
                d = d.replace("+", "")
            print ("  " + d)
        print (") + ")

def getHelpString ():
    global sectionKey
    file = open("tmp.txt", 'r')
    isbutton = False
    paType = 0
    for line in file:
        line = line.strip()
        if "<li><b>" in line or "<li> <b>" in line:
            line = getFullStr(file, line, "</li>")
            if isbutton:
                processButtonLine(line)
            else:
                processConfigLine(line, paType)
        elif "<p>" in line:
            line = getFullStr(file, line, "</p>")
            processParaLine(line)
        elif ">Configurable" in line:
            paType = 0
        elif "Non-Configurable" in line:
            paType = 1
        #elif "Selection" in line:
        #    paType = 2
        elif "Navigation" in line:
            paType = 3
        elif "Buttons" in line:
            isbutton = True
        elif "<h2>" in line:
            sectionKey = find_between(line, "name=", ">").replace("_", "")
            sectionKey = sectionKey.replace("\"", "")
    file.close()

    printCode(paradata, "");
    printCode(navidata, "HELP_H3_NAVIGATION");
    printCode(seldata, "HELP_H3_SEL_CRITERIA");
    printCode(configdata, "HELP_H3_CONFIG_DATA");
    printCode(nonconfigdata, "HELP_H3_NONCONFIG_DATA");
    printCode(buttondata, "HELP_H3_CMD_BUTTONS");

getHelpString()
