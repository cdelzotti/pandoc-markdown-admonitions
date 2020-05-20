import sys

def latexAdmonition(text):
    """
    Convert every Markdown Extended Admonitions from text into latex tcolorbox boxes
    Parameters
    ----------
    text : Text that must be tranformed (list)

    Return
    ------
    String : text with Markdown Extended admonitions remplaced by latex tcolorbox boxes
    """
    # For each line
    i = 0
    while i < len(text):
        # If the line is ong enough to contain an Admonition
        if len(text[i]) > 3:
            # If the line start with "!!!"
            if  "!!!" in text[i]:
                # It's an admonition ! Now find the end !
                # Find the starting pattern
                statingPattern = text[i].split("!")[0] + " "
                j = i + 1
                foundEnd = False
                while not foundEnd and j < len(text):
                    if len(text[j]) < len(statingPattern):
                        foundEnd = True
                    elif text[j][0:len(statingPattern)] == statingPattern:
                        j += 1
                    else:
                        foundEnd = True
                # End found !
                # Get box title
                title = ""
                parsedHeader = text[i].strip().split(" ")
                for k in range(2, len(parsedHeader)):
                    title += parsedHeader[k] + " "
                # Change text
                ## Define title
                text[i] = "\\begin{tcolorbox}[title=%s,colframe=%s]\n" % (title, parsedHeader[1].upper())
                ## Define end block
                text.insert(j, "\\end{tcolorbox}\n")
                i = j
        i += 1
    return text
                
if len(sys.argv) != 3:
    print("Wrong number of parameters ! Expected `python admonition.py FILE_IN FILE_OUT`")
else:
    # Open file to read
    fh = open(sys.argv[1], "r")
    text = fh.readlines()
    fh.close
    # Convert
    convertedText = latexAdmonition(text)
    # Open file to write
    fh = open(sys.argv[2], "w+")
    for line in convertedText:
        fh.write(line)
    fh.close()
