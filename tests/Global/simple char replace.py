def transl(orig):
    lc = 0
    transl = ""
    l = ""

    for l in orig:
        if l in ["a", "e", "i", "o", "u"]:
            transl = transl+"b"

        elif l in "AEIOU":
            transl = transl + "B"

        else:
            transl = transl+l
        lc += 1
    lc = 0

    return transl 

print(transl(input ("Enter text to translate to Blawgistani: ")))

