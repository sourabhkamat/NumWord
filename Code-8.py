def OTH(number):
    '''This Function Only Returns Ones Tens And Hundred In Word Form'''
    number = int(number)
#     if number == 0:
#         return 'Zero'

    numList = []
    for i in str(number):
        numList.append(i)
        
    num_length = len(numList)

    num_Dict = {0  : '',
                1  : ' One',
                2  : ' Two',
                3  : ' Three',
                4  : ' Four',
                5  : ' Five',
                6  : ' Six',
                7  : ' Seven',
                8  : ' Eight',
                9  : ' Nine',
                10 : ' Ten',
                11 : ' Eleven',
                12 : ' Twelve',
                13 : ' Thirteen',
                14 : ' Fourteen',
                15 : ' Fifteen',
                16 : ' Sixteen',
                17 : ' Seventeen',
                18 : ' Eighteen',
                19 : ' Nineteen',
                20 : ' Twenty',
                30 : ' Thirty',
                40 : ' Fourty',
                50 : ' Fifty',
                60 : ' Sixty',
                70 : ' Seventy',
                80 : ' Eighty',
                90 : ' Ninety',
                100: ' Hundred'}
    num_Word = []
    if num_length == 3:
        
        tens = str() # 11 to 19
        for elements in numList[1:]:
            tens += elements
            
        tens = int(tens)
        
        if 20 >= tens >= 10:
            num_Word.insert(0, num_Dict[tens])
            
        elif len(str(tens)) == 1:
            num_Word.insert(0, num_Dict[tens])
            
        elif 99 >= tens >= 21:
            num_Word.insert(0, num_Dict[int(numList[-1])])
            num_Word.insert(0, num_Dict[int(numList[1]+'0')])
        num_Word.insert(0, num_Dict[100])
        num_Word.insert(0, num_Dict[int(numList[0])])
        


    elif num_length == 2:
        
        tens = str() # 11 to 19
        for elements in numList:
            tens += elements
            
        tens = int(tens)
        
        # once####
        if 20 >= tens >= 10:
            num_Word.insert(0, num_Dict[tens])
            
#         elif len(str(tens)) == 1:
#             num_Word.insert(0, num_Dict[tens])
            
        elif 99 >= tens >= 21:
            num_Word.insert(0, num_Dict[int(numList[-1])])
            num_Word.insert(0, num_Dict[int(numList[0]+'0')])
            
    elif num_length == 1:
        
        tens = str() # 11 to 19
        for elements in numList:
            tens += elements
            
        tens = int(tens)
        
        # once####
        if len(str(tens)) == 1:
            num_Word.insert(0, num_Dict[tens])
            
    return ('').join(num_Word)


#########################################################################################
num    = int(input(' > Enter Number   :   '))
numlen1 = len(str(num))
num0   = num
num    = ("{:,}".format(num)) # "{:,}" is a string format method to saparate thousand.
num    = num.split(',')
print('\n   Orignal Number :  ', (',').join(num))
num.reverse()
numlen = len(num)


num_Dict = {0: '',
            1: ' Thousand',
            2 : ' Million',
            3 : ' Billion',
            4 : ' Trillion',
            5 : ' Quadrillion',
            6 : ' Quintillion'}

numWord = []
print_flag = True

if num0 == 0:
    numWord.insert(0, 'Zero')
if numlen1 <= 19:
    for i in range(numlen):
        numWord.insert(0, OTH(num[i]))
        if int(num[i]) >= 1:
            numWord.insert(1, num_Dict[i]+', ')
else:
    print("\nNote :\n   You\'ve entered a ", numlen1, " digit number.\n   Right now this code is set to calculate only 19 digit number, Which is One Quintillion = 1,000,000,000,000,000,000")
    print_flag = False

a = ('').join(numWord)

if print_flag == True:
    print('\n   Number Name    : ', a)
