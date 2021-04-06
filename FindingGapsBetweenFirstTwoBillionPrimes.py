import traceback
import time
# TODO While I am storing all of the gaps into a txt file, it may be faster just to recalculate all of the gaps
#  WITHOUT writing anything to files. That way, I already have a dictionary fully filled up. Or, maybe it will be
#  faster to just read all of the gaps in from the file

# WITH outputting everything to files
# Program run time for first file only: 37.54 seconds
# Program run time for first two files only: 80.83 seconds first time, 73.91 seconds second time
# Program run times for ALL 200 files (Ran in CMD line not IDE): 7262.08 seconds
# (minus about 250 seconds when I paused the program on accident during file 162)

# WITHOUT outputting everything to files, so just counting gap occurrences and storing them in the dictionary
# Program run time for first file only: 14.38 seconds
# Program run time for first two files only: 27.13 seconds
# Program run times for ALL 200 files:


start_time = time.time()

currentFileNum = 1
onNewLine = False
currentPrime = 0
nextPrime = 0
gap = 0
gapsInPrimes = open("gapsInPrimes.txt", "w")
gapsInPrimes.write("Gap | Current | Next\n")
occurrencesOfGaps = open("occurrencesOfGaps.txt", "w")
numOccurrencesOfGaps = {}
try:
    for currentFileNum in range(1, 201):
        currentFile = open("2T_part" + str(currentFileNum) + ".txt")
        print("Starting new file: 2T_part" + str(currentFileNum) + ".text")
        print("------------------------------")
        newFile = True
        for line in currentFile:
            primes = line.split()
            for i in range(10):
                if i+1 > 9:
                    # If i+1 is greater than 9, then the next prime (i+1) will be on the next line or next file. Thus,
                    # we should save the current primes[i], which is the last prime on the current line or current file,
                    # so that we can can compare it to the nextPrime on the next line or next file.
                    currentPrime = primes[i]
                    onNewLine = True
                    # break, so that we go back to previous loop and go to new line (or previous previous loop and a new
                    # line in a new file)
                    break

                # If we are on a new line (or new file) then primes[i] will be the nextPrime to compare to,
                # with our previous prime being saved from the last line or file
                if onNewLine:
                    # print("first comparison newLine, onNewLine = True")
                    nextPrime = primes[i]
                    gap = int(nextPrime) - int(currentPrime)
                    gapsInPrimes.write(str(gap) + "\t" + str(currentPrime) + "\t" + str(nextPrime) + "\n")

                    if gap in numOccurrencesOfGaps:
                        numOccurrencesOfGaps[gap] += 1
                    else:
                        numOccurrencesOfGaps[gap] = 1

                    if newFile:
                        print("First comparison in new file")
                        print("currentPrime: ", currentPrime)
                        print("nextPrime:", nextPrime)
                        print("gap:", gap)
                        print("------------------------------")

                    currentPrime = nextPrime
                    nextPrime = primes[i+1]
                    gap = int(nextPrime) - int(currentPrime)
                    gapsInPrimes.write(str(gap) + "\t" + str(currentPrime) + "\t" + str(nextPrime) + "\n")

                    if gap in numOccurrencesOfGaps:
                        numOccurrencesOfGaps[gap] += 1
                    else:
                        numOccurrencesOfGaps[gap] = 1

                    onNewLine = False

                    if newFile:
                        print("Second comparison in new file")
                        print("currentPrime: ", currentPrime)
                        print("nextPrime:", nextPrime)
                        print("gap:", gap)
                        print("------------------------------")

                    continue

                currentPrime = primes[i]
                nextPrime = primes[i+1]

                gap = int(nextPrime) - int(currentPrime)
                gapsInPrimes.write(str(gap) + "\t" + str(currentPrime) + "\t" + str(nextPrime) + "\n")

                if gap in numOccurrencesOfGaps:
                    numOccurrencesOfGaps[gap] += 1
                else:
                    numOccurrencesOfGaps[gap] = 1

            newFile = False

        occurrencesOfGaps.write(
            "---------------Gap Frequency in First " + str(10000000 * currentFileNum) + " Primes (or " + str(currentFileNum) + " number of files) ---------------\n")
        occurrencesOfGaps.write("Gap | Occurred\n")

        for key, value in numOccurrencesOfGaps.items():
            occurrencesOfGaps.write(str(key) + "\t" + str(value) + "\n")
        print(
            "Current run time after completing " + str(currentFileNum) + " number of files: " + "--- %s seconds ---" % (
                        time.time() - start_time))
        print()

    gapsInPrimes.write("---------------Gap Frequency for Entire Program---------------\n")
    gapsInPrimes.write("Gap | Occurred\n")
    for key, value in numOccurrencesOfGaps.items():
        gapsInPrimes.write(str(key) + "\t" + str(value) + "\n")

except Exception as e:
    print("An error occurred in file number", currentFileNum, "\nOn line", line, "\nOn currentPrime", currentPrime, "\nOn nextPrime", nextPrime)
    print(e)
    traceback.print_exc()

print()
print("Program has finished without errors! (Excluding possible logical errors lol)")
print("--- %s seconds ---" % (time.time() - start_time))
print("Gaps (and primes for those gaps) and frequency of gaps can be found in gapsInPrimes.txt")
print("Gap frequencies for each file (AKA every 10 million primes) can be found in occurrencesOfGaps.txt")
currentFile.close()
gapsInPrimes.close()
occurrencesOfGaps.close()

