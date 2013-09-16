#Joshua Bloch
#2/28/13
#stringIntersect

def stringIntersect(stringUpper1, stringUpper2):
    outputString=''
    string1=stringUpper1.lower()
    string2=stringUpper2.lower()
    for ch in string1:
        if ch in string2:
            if ch not in outputString:
                outputString=outputString+ch
    print outputString
