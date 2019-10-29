import os, time, subprocess

if __name__=="__main__":
    f = []
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        f.extend(filenames)
        break

    questions = []
    for file in f:
        if (file[-2:] == "py") and (file[:1] == "q"):
            questions.append(file)

    print("Question\tAdam\t\tJason")
    cur = 1
    for question in questions:
        # Run each and list in one row for both
        start = time.time()
        subprocess.run("python " + question, stdout=subprocess.DEVNULL)
        stop = time.time()
        delta = stop - start
        delta = "{:10.4f}".format(delta)

        if cur == 1:
            text = question[:2]
            text += "\t"
            text += str(delta)
            text += "\t"
            cur += 1
        else:
            text += str(delta)
            print(text)
            text = ""
            cur = 1
