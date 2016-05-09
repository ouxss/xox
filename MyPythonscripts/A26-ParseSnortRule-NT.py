import sys


def parseContent(content):
	escape = False
        listContent = []
        try:
            listContent += content
        except TypeError:
            pdb.set_trace()
        toggle = False
        parsedContent = ""
        if content == "||":
            return False, ''
        while listContent:
            char = listContent.pop(0)
            if char == "|" and not toggle and not escape:
                toggle = True
            elif char == "|" and toggle and not escape:
                toggle = False
                if listContent == []:
                    break
                char = listContent.pop(0)
            if toggle == True:
                if char == ' ' or char == '|':
                    continue
                else:
                    c1 = char
                try:
                    c2 = listContent.pop(0)
                except IndexError:
                    print "cannort parse content, probably a space at the \
                            end or at the beginning"
                    return False
                byteChar = c1 + c2
                try:
                    byte = byteChar.decode("hex")
                except TypeError:
                    print "cannot parse content, bytes should be sperated by \
                    space"
                    return False
                parsedContent = parsedContent + byte
            if toggle == False:
		if char =='\\' and not escape:
			escape=True
		else:	
                	parsedContent = parsedContent + char
			escape=False
        return True, parsedContent

print parseContent(sys.argv[1])[1]
