# Dictionary Containing 'Number Names'
numName = {'0': 'Zero' ,
           '1': 'One'  ,
           '2': 'Two'  ,
           '3': 'Three',
           '4': 'Four' ,
           '5': 'Five' ,
           '6': 'Six'  ,
           '7': 'Seven',
           '8': 'Eight',
           '9': 'Nine' ,
           'Zero' : ''       ,
           'One'  : 'Ten'    ,
           'Two'  : 'Twenty' ,
           'Three': 'Thirty' ,
           'Four' : 'Fourty' ,
           'Five' : 'Fifty'  ,
           'Six'  : 'Sixty'  ,
           'Seven': 'Seventy',
           'Eight': 'Eighty' ,
           'Nine' : 'Ninety' ,
           '100':        'Hundred'     ,
           '1000':       'Thousand'    ,
           '10000':      'Ten Thousand',
           '100000':     'Hundred Thousand',
           '1000000':    'Million'         ,
           '10000000':   'Ten Million'     ,
           '100000000':  'Hundred Million' ,
           '1000000000': 'Billion'}

# User Input In Gigit Here
NumDigit = str(12345)
print(NumDigit)


# Converting NumDigit Into A List In Loop
numList = []

for (_digits) in (NumDigit):
      numList.append(_digits)

# Reversing Number List
numList.reverse()
print(numList)

# NumList Length

numLen = len(numList)

# Converting Digits Into Names

popupdate = 1

for i in range(numLen):
    
    if numList[i] == '0':
        numList.insert(i, numName['0'])
        numList.pop(popupdate)
        popupdate += 1
        
        continue
        
    elif numList[i] == '1':
        numList.insert(i, numName['1'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '2':
        numList.insert(i, numName['2'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '3':
        numList.insert(i, numName['3'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '4':
        numList.insert(i, numName['4'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '5':
        numList.insert(i, numName['5'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '6':
        numList.insert(i, numName['6'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '7':
        numList.insert(i, numName['7'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '8':
        numList.insert(i, numName['8'])
        numList.pop(popupdate)
        popupdate += 1
        continue

    elif numList[i] == '9':
        numList.insert(i, numName['9'])
        numList.pop(popupdate)
        popupdate += 1
        continue
    else:
        print("Seems any error occurred while 'Converting Digits Into Numbers Names' ")
    
print(numList)

# Don't Know What I'm Doing || Update Later
#['1', '2', '3', '4', '5']
#['One', 'Two', 'Three', 'Four', 'Five']


finalNum = list()

loopup = 1

for i in range(numLen):
    
    if i == 0: # Once
        if numList[i] != 'Zero':
            finalNum.append(numList[0])
            continue
            
    elif i == 1 and numList[i] != 'Zero': # Tense
        finalNum.append(numName[numList[i]])
        
    elif i == 2 and numList[i] != 'Zero': # Hundred
        finalNum.append(numList[i] + ' Hundred')
        
    elif i == 3 and numList[i] != 'Zero': # Hundred
        finalNum.append(numName[numList[i]])
        
    elif i == 4 and numList[i] != 'Zero': # Hundred
        finalNum.append(numList[i] + ' Hundred')
        
    
finalNum.reverse()
print(finalNum)
    
#     elif numList[i] == 'Zero':
#          numList.pop(i)
#          loopup += 1
#          continue
        
#     elif numList[i] != 'Zero':
#         numList.insert(numList[i] + masterNum[i])
        
#     print(i)