import re

fileInput = raw_input('file name: \n')
f = open(fileInput, 'r')


##Extract times and text from file, put in a list as follows:
## [[timeFrom, timeTo],[subLine1, subLine2...]]
result = []
times = []
subs = []
newLine = True
for l in f:
    t = re.findall("([0-9]+:[0-9]+:[0-9]+,[0-9]+)", l)
    s = re.findall("([a-z]+)", l)
    if len(t) > 0:
        times.append(t)
    elif len(s) > 0:
        subs.append(l)
    else:
        if(len(times) > 0):
            times.append(subs)
            result.append(times)
            times = []
            subs = []
##Methond to convert time tag to time in ms
def converToNum(test):
    h = int(test[0:2])
    m = int(test[3:5])
    s = int(test[6:8])
    ms = int(test[9:12])
    msT = ms + s*1000 + m*60*1000 + h*60*60*1000
    return msT
##Method to convert time in ms to a time tag
def converToTime(nIn):
    h, m = divmod(nIn, 60*60*1000)
    m, s = divmod(m, 60*1000)
    s, ms = divmod(s, 1000)
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2) + ',' + str(ms).zfill(3)

##Create timeLine in ms
msTimeLine = []
for i in result:
    couple = []
    couple.append(converToNum(i[0][0]))
    couple.append(converToNum(i[0][1]))
    msTimeLine.append(couple)


print "The firs subtitle that say's: '" + result[0][1][0].rstrip('\n') + "' appears now at: " + result[0][0][0]
y1 = converToNum(raw_input("please give the correct value below \n"))
x1 = converToNum(result[0][0][0])

print "The last subtitle that say's: '" + result[len(result)-1][1][0].rstrip('\n') + "' appears now at: " + result[len(result)-1][0][0]
y2 = converToNum(raw_input("please give the correct value below \n"))
x2 = converToNum(result[len(result)-1][0][0])

m = float((y1 - y2)) / float((x1 - x2))
## y = m*x + b
## -b = m*x -y
## b = -m*x +y

b = -m*x1 + y1

newVals = []

for i in result:
	couple = []
	x11 = converToNum(i[0][0])
	x22 = converToNum(i[0][1])
	y11 = int(x11*m + b)
	y22 = int(x22*m + b)
	couple.append(converToTime(y11))
	couple.append(converToTime(y22))
	newVals.append(couple)
## run through file once again replacing old 00:00:00,000 ===> 00:00:00,000 with the new values, display or save result.

##TEST
print 'Slope :' + str(m) + ', Offsset: ' + str(b)
##for i in range(0, len(result)):
##    outF.write( 'Old: ' + result[i][0][0])
##    outF.write( 'New: ' + newVals[i][0])


outString = ''
valIndex = 0
f = open(fileInput, 'r')
for l in f:
    t = re.findall("([0-9]+:[0-9]+:[0-9]+,[0-9]+)", l)
    if len(t) > 0:
        outString += newVals[valIndex][0] + ' --> ' + newVals[valIndex][1] +'\n'
        valIndex += 1
    else:
        outString += l
outF = open(fileInput+'.out', 'w')
outF.write(outString)


