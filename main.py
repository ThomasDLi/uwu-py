ipt = input("chose file to translate from uwu into python\nFILE HAS TO END IN .UWUPY\nyou do not need to write .uwupy after the filename\n\n")

something = open(f"{ipt}.uwupy", "r")

lines = something.readlines()

something.close()

outfilename = input("what should the output .py file name be?\n")

out = open(f"{outfilename}.py", "a")

for x in lines:
    replaced = x.replace("dwef", "def")
    replaced = replaced.replace("cwass", "class")
    replaced = replaced.replace("__nwame__", "__name__")
    replaced = replaced.replace("retwern", "return")
    replaced = replaced.replace("pwint", "print")
    replaced = replaced.replace("intpwut", "input")
    replaced = replaced.replace("fwor", "for")
    replaced = replaced.replace("die", "quit")
    replaced = replaced.replace("wen", "when")
    replaced = replaced.replace("waile", "while")
    replaced = replaced.replace("tru", "True")
    replaced = replaced.replace("no!", "False")
    replaced = replaced.replace("pls", "try")
    replaced = replaced.replace("but...", "except")
    replaced = replaced.replace("welcome", "import")

    out.write(replaced)
