'''
    Packet Fragmentation Calculator
'''

inputValue = int(input())
fullPackets = 0
totalBytes =0
inputValue = inputValue -20
while inputValue > 1480:
	inputValue -=1480
	totalBytes +=1480
	fullPackets += 1
	if inputValue < 1480:
		break
totalBytes = totalBytes + inputValue + (fullPackets+1) * 20
print(totalBytes)
print (fullPackets)
print (fullPackets+1)
