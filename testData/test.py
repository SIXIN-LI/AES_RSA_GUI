from Main import *

app = Application()
messages = app.read_files()
#print(messages)
for i in range(3):
    m = messages[i][0]
    #print(m)
    #processed is a list of truncated messages converted into numbers
    nLength = len(str(88889999000))
    processed = preprocess(m, nLength)
    print(processed)
    break