# importing libraries
import warnings
import numpy as np
import matplotlib.pyplot as plt
import random
warnings.simplefilter(action='ignore', category=FutureWarning)

def CreateGraph(toPlot, ymax, procedure, totalTrackTime):
    x = np.array(toPlot)
    y = np.arange(ymax + 1)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.ylim(ymax + 1, 0)
    plt.xlim(0, 99)
    plt.title(procedure)
    plt.xlabel("Track")
    plt.ylabel("Step")
    plt.plot(x, y, color="green")
    procedureString = 'The procedure will be'
    plt.text(0, ymax + 2, procedureString, ha='left')
    for i in x:
        plt.text(0, ymax + 2.5, x, ha='left')
    plt.text(99, ymax + 2, 'The total track time is', ha='right')
    plt.text(99, ymax + 2.5, str(totalTrackTime), ha='right')
    plt.plot(x, y, 'go')
    plt.xticks(x)
    plt.yticks(y)
    plt.rc('axes', axisbelow=True)
    plt.show()


def FirstComeFirstServe(trackvalues):
    totalTrackTime = 0
    for i in range(1, len(trackvalues)):
        totalTrackTime = totalTrackTime + abs(trackvalues[i] - trackvalues[i - 1])
    return trackvalues, totalTrackTime


def ShortestSeekTimeFirst(originalvalues, head):
    originalQueue = originalvalues
    sortedQueue = originalQueue.copy()
    sortedQueue.sort()
    SSTFProcedure = [head]
    toCheck = head
    while len(sortedQueue) > 1:
        if toCheck != max(sortedQueue):
            if toCheck == min(sortedQueue):
                sortedQueue.pop(0)
                toCheck = sortedQueue[0]
                SSTFProcedure.append(toCheck)

            elif (toCheck - sortedQueue[sortedQueue.index(toCheck) - 1]) \
                    == (sortedQueue[sortedQueue.index(toCheck) + 1] - toCheck):

                if originalQueue.index(sortedQueue[sortedQueue.index(toCheck) - 1]) \
                        < originalQueue.index(sortedQueue[sortedQueue.index(toCheck) + 1]):
                    valueToGo = sortedQueue[sortedQueue.index(toCheck) - 1]
                    sortedQueue.pop(sortedQueue.index(toCheck))
                    indexToCheck = originalQueue.index(valueToGo)
                    toCheck = originalQueue[indexToCheck]
                    SSTFProcedure.append(toCheck)

                elif originalQueue.index(sortedQueue[sortedQueue.index(toCheck) - 1]) \
                        > originalQueue.index(sortedQueue[sortedQueue.index(toCheck) + 1]):
                    currentIndex = sortedQueue.index(toCheck)
                    sortedQueue.pop(currentIndex)
                    valueToGo = sortedQueue[currentIndex]
                    indexToCheck = originalQueue.index(valueToGo)
                    toCheck = originalQueue[indexToCheck]
                    SSTFProcedure.append(toCheck)

            elif (toCheck - sortedQueue[sortedQueue.index(toCheck) - 1]) \
                    < (sortedQueue[sortedQueue.index(toCheck) + 1] - toCheck):
                currentIndex = sortedQueue.index(toCheck)
                sortedQueue.pop(sortedQueue.index(toCheck))
                toCheck = sortedQueue[currentIndex - 1]
                SSTFProcedure.append(toCheck)

            elif (toCheck - sortedQueue[sortedQueue.index(toCheck) - 1]) \
                    > (sortedQueue[sortedQueue.index(toCheck) + 1] - toCheck):
                currentIndex = sortedQueue.index(toCheck)
                sortedQueue.pop(sortedQueue.index(toCheck))
                toCheck = sortedQueue[currentIndex]
                SSTFProcedure.append(toCheck)

        elif toCheck == max(sortedQueue):
            sortedQueue.pop()
            toCheck = sortedQueue[-1]
            SSTFProcedure.append(toCheck)

    totalTrackTime = 0
    for i in range(1, len(SSTFProcedure)):
        totalTrackTime = totalTrackTime + abs(SSTFProcedure[i] - SSTFProcedure[i - 1])

    return SSTFProcedure, totalTrackTime


def Scan(trackvalues, currenttrack, scanDirection):
    scanQueue = trackvalues.copy()
    scanQueue.sort()
    scanProcedure = [currenttrack]
    toCheck = currenttrack
    if scanDirection == 0:
        if not (0 in scanQueue):
            scanQueue.insert(0, 0)
    elif scanDirection == 99:
        if not (99 in scanQueue):
            scanQueue.append(99)

    while len(scanQueue) > 1:
        if (scanDirection == 0) and (toCheck != 0):
            currentIndex = scanQueue.index(toCheck)
            scanQueue.pop(scanQueue.index(toCheck))
            toCheck = scanQueue[currentIndex - 1]
            scanProcedure.append(toCheck)
            scanDirection = 0
        elif (scanDirection == 0) and (toCheck == 0):
            scanQueue.pop(scanQueue.index(toCheck))
            toCheck = scanQueue[0]
            scanProcedure.append(toCheck)
            scanDirection = 99
        elif (scanDirection == 99) and (toCheck != 99):
            currentIndex = scanQueue.index(toCheck)
            scanQueue.pop(scanQueue.index(toCheck))
            toCheck = scanQueue[currentIndex]
            scanProcedure.append(toCheck)
            scanDirection = 99
        elif (scanDirection == 99) and (toCheck == 99):
            scanQueue.pop(scanQueue.index(toCheck))
            toCheck = scanQueue[-1]
            scanProcedure.append(toCheck)
            scanDirection = 0

    totalTrackTime = 0
    for i in range(1, len(scanProcedure)):
        totalTrackTime = totalTrackTime + abs(scanProcedure[i] - scanProcedure[i - 1])

    return scanProcedure, totalTrackTime


def cScan(trackvalues, currenttrack, initialCScanDirection):
    cScanQueue = trackvalues.copy()
    cScanQueue.sort()
    cScanProcedure = [currenttrack]
    toCheck = currenttrack

    if not (0 in cScanQueue):
        cScanQueue.insert(0, 0)

    if not (99 in cScanQueue):
        cScanQueue.append(99)

    if initialCScanDirection == 0:
        cScanDirection = 0
        while len(cScanQueue) > 1:
            if (cScanDirection == 0) and (toCheck != 0):
                currentIndex = cScanQueue.index(toCheck)
                cScanQueue.pop(cScanQueue.index(toCheck))
                toCheck = cScanQueue[currentIndex - 1]
                cScanProcedure.append(toCheck)
                cScanDirection = 0
            elif (cScanDirection == 0) and (toCheck == 0):
                cScanQueue.pop(cScanQueue.index(toCheck))
                toCheck = cScanQueue[-1]
                cScanProcedure.append(toCheck)
                cScanDirection = 99
            elif cScanDirection == 99:
                currentIndex = cScanQueue.index(toCheck)
                cScanQueue.pop(cScanQueue.index(toCheck))
                toCheck = cScanQueue[currentIndex - 1]
                cScanProcedure.append(toCheck)
                cScanDirection = 99

    elif initialCScanDirection == 99:
        cScanDirection = 99
        while len(cScanQueue) > 1:
            if (cScanDirection == 99) and (toCheck != 99):
                currentIndex = cScanQueue.index(toCheck)
                cScanQueue.pop(cScanQueue.index(toCheck))
                toCheck = cScanQueue[currentIndex]
                cScanProcedure.append(toCheck)
                cScanDirection = 99
            elif (cScanDirection == 99) and (toCheck == 99):
                cScanQueue.pop(cScanQueue.index(toCheck))
                toCheck = cScanQueue[0]
                cScanProcedure.append(toCheck)
                cScanDirection = 0
            if cScanDirection == 0:
                currentIndex = cScanQueue.index(toCheck)
                cScanQueue.pop(cScanQueue.index(toCheck))
                toCheck = cScanQueue[currentIndex]
                cScanProcedure.append(toCheck)
                cScanDirection = 0

    totalTrackTime = 0
    for i in range(1, len(cScanProcedure)):
        totalTrackTime = totalTrackTime + abs(cScanProcedure[i] - cScanProcedure[i - 1])

    return cScanProcedure, totalTrackTime


def Look(trackvalues, currenttrack, scanDirection):
    lookQueue = trackvalues.copy()
    lookQueue.sort()
    lookProcedure = [currenttrack]
    toCheck = currenttrack

    while len(lookQueue) > 1:
        if (scanDirection == 0) and (toCheck != lookQueue[0]):
            currentIndex = lookQueue.index(toCheck)
            lookQueue.pop(lookQueue.index(toCheck))
            toCheck = lookQueue[currentIndex - 1]
            lookProcedure.append(toCheck)
            scanDirection = 0
        elif (scanDirection == 0) and (toCheck == lookQueue[0]):
            lookQueue.pop(lookQueue.index(toCheck))
            toCheck = lookQueue[0]
            lookProcedure.append(toCheck)
            scanDirection = 99
        elif (scanDirection == 99) and (toCheck != lookQueue[-1]):
            currentIndex = lookQueue.index(toCheck)
            lookQueue.pop(lookQueue.index(toCheck))
            toCheck = lookQueue[currentIndex]
            lookProcedure.append(toCheck)
            scanDirection = 99
        elif (scanDirection == 99) and (toCheck == lookQueue[-1]):
            lookQueue.pop(lookQueue.index(toCheck))
            toCheck = lookQueue[-1]
            lookProcedure.append(toCheck)
            scanDirection = 0

    totalTrackTime = 0
    for i in range(1, len(lookProcedure)):
        totalTrackTime = totalTrackTime + abs(lookProcedure[i] - lookProcedure[i - 1])

    return lookProcedure, totalTrackTime


def cLook(trackvalues, currenttrack, initialCLookDirection):
    cLookQueue = trackvalues.copy()
    cLookQueue.sort()
    cLookProcedure = [currenttrack]
    toCheck = currenttrack

    if initialCLookDirection == 0:
        cLookDirection = 0
        while len(cLookQueue) > 1:
            if (cLookDirection == 0) and (toCheck != cLookQueue[0]):
                currentIndex = cLookQueue.index(toCheck)
                cLookQueue.pop(cLookQueue.index(toCheck))
                toCheck = cLookQueue[currentIndex - 1]
                cLookProcedure.append(toCheck)
                cLookDirection = 0
            elif (cLookDirection == 0) and (toCheck == cLookQueue[0]):
                cLookQueue.pop(cLookQueue.index(toCheck))
                toCheck = cLookQueue[-1]
                cLookProcedure.append(toCheck)
                cLookDirection = 99
            elif cLookDirection == 99:
                currentIndex = cLookQueue.index(toCheck)
                cLookQueue.pop(cLookQueue.index(toCheck))
                toCheck = cLookQueue[currentIndex - 1]
                cLookProcedure.append(toCheck)
                cLookDirection = 99

    elif initialCLookDirection == 99:
        cLookDirection = 99
        while len(cLookQueue) > 1:
            if (cLookDirection == 99) and (toCheck != cLookQueue[-1]):
                currentIndex = cLookQueue.index(toCheck)
                cLookQueue.pop(cLookQueue.index(toCheck))
                toCheck = cLookQueue[currentIndex]
                cLookProcedure.append(toCheck)
                cLookDirection = 99
            elif (cLookDirection == 99) and (toCheck == cLookQueue[-1]):
                cLookQueue.pop(cLookQueue.index(toCheck))
                toCheck = cLookQueue[0]
                cLookProcedure.append(toCheck)
                cLookDirection = 0
            if cLookDirection == 0:
                currentIndex = cLookQueue.index(toCheck)
                cLookQueue.pop(cLookQueue.index(toCheck))
                toCheck = cLookQueue[currentIndex]
                cLookProcedure.append(toCheck)
                cLookDirection = 0

    totalTrackTime = 0
    for i in range(1, len(cLookProcedure)):
        totalTrackTime = totalTrackTime + abs(cLookProcedure[i] - cLookProcedure[i - 1])

    return cLookProcedure, totalTrackTime


# Driver starts here
amountOfTracks = 0
currentTrack = -1
direction = 1
algorithmChoice = 0

while (amountOfTracks < 10) or (amountOfTracks > 20):
    print("NOTE: NUMBER OF TRACKS MUST ONLY BE BETWEEN 10-20")
    amountOfTracks = int(input("Please enter the number of tracks to service: "))

while (currentTrack < 0) or (currentTrack > 99):
    print("NOTE: THE VALUE OF THE CURRENT HEAD MUST ONLY BE BETWEEN 0-99")
    currentTrack = int(input("Please enter the current position of the head: "))

trackValues = [currentTrack]

while (direction != 0) and (direction != 99):
    direction = int(input("Direction Towards (0 or 99): "))

counter = 0
while counter < amountOfTracks:
    number = random.randint(0, 99)
    if not (number in trackValues):
        trackValues.append(number)
        counter = counter + 1

print("Current Queue: ", trackValues)

while (algorithmChoice < 1) or (algorithmChoice > 6):
    print("Choose Algorithm to be used:\n1.First Come First Serve\n2.Shortest Seek Time First\n"
          "3.SCAN Algorithm\n4.CSCAN Algorithm\n5.LOOK Algorithm\n6.CLOOK Algorithm")
    algorithmChoice = int(input("Choice: "))

if algorithmChoice == 1:
    trackProcedure, total = FirstComeFirstServe(trackValues)
    procedureName = "First Come First Serve"
    CreateGraph(trackProcedure, amountOfTracks, procedureName, total)


elif algorithmChoice == 2:
    trackProcedure, total = ShortestSeekTimeFirst(trackValues, currentTrack)
    procedureName = "Shortest Seek Time First"
    CreateGraph(trackProcedure, amountOfTracks, procedureName, total)

elif algorithmChoice == 3:
    trackProcedure, total = Scan(trackValues, currentTrack, direction)
    procedureName = "SCAN Algorithm"
    scanAmountOfTracks = len(trackProcedure) - 1
    CreateGraph(trackProcedure, scanAmountOfTracks, procedureName, total)

elif algorithmChoice == 4:
    trackProcedure, total = cScan(trackValues, currentTrack, direction)
    procedureName = "CSCAN Algorithm"
    cScanAmountOfTracks = len(trackProcedure) - 1
    CreateGraph(trackProcedure, cScanAmountOfTracks, procedureName, total)

elif algorithmChoice == 5:
    trackProcedure, total = Look(trackValues, currentTrack, direction)
    procedureName = "LOOK Algorithm"
    cScanAmountOfTracks = len(trackProcedure) - 1
    CreateGraph(trackProcedure, cScanAmountOfTracks, procedureName, total)

elif algorithmChoice == 6:
    trackProcedure, total = cLook(trackValues, currentTrack, direction)
    procedureName = "CLOOK Algorithm"
    cScanAmountOfTracks = len(trackProcedure) - 1
    CreateGraph(trackProcedure, cScanAmountOfTracks, procedureName, total)
