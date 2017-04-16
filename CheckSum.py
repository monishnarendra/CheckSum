import sys
import time
import itertools
import threading

def Get_Text(text_original):
    text_copy = text_original
    list1 = ':'.join(hex(ord(x))[0:] for x in text_copy)  # text to hexadecimal conversion
    print("Given input in Hexadecimal format, with :", list1)
    list2 = list1.split(':')
    print("Given input in Hexadecimal format, split ",list2)
    list3 = Remove_0x(list2)
    print("Given input in Hexadecimal format, without 0x = ",list3)
    list4 = [''.join(list3) for list3 in zip(list3[0::2], list3[1::2])]
    print("Given Text in Hexadecimal format ,",list4)
    return list4

def dec_to_hex(number):
    rValue = ""
    hex_bits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while(number):
        rValue = hex_bits[int(number%16)] + rValue
        number = number/16
    return rValue

def hex_to_dec(hex_string):
    hex_dict = {"0" : 0,
                "1" : 1,
                "2" : 2,
                "3" : 3,
                "4" : 4,
                "5" : 5,
                "6" : 6,
                "7" : 7,
                "8" : 8,
                "9" : 9,
                "A" : 10,
                "B" : 11,
                "C" : 12,
                "D" : 13,
                "E" : 14,
                "F" : 15}
    rValue = 0
    multiplier = 1
    str_hex_string = str(hex_string)
    for i in range(len(str_hex_string)):
        rValue = hex_dict[str_hex_string[len(str_hex_string)-1-i]] * multiplier + rValue
        multiplier = multiplier * 16
    return rValue

def Remove_Leading_zero(A):
    A = A.lstrip('0')  # removing leading 0000000
    A = list(A)        # put in list
    return A

def Remove_0x(B):
    C = ' '.join(B).replace('0x', '').split()       # removing 0x from list
    return C

def Reciver(list4,check_sum,list7):
    for i in range(len(list4)):
        list7.append(list4[i])

    list7.append(check_sum)

    print("list 7 = ", list7)
    list7 = Corrupt(list7)
    list7 = Remove_0x(list7)
    list7 = [element.upper() for element in list7]  # capitalization
    print("list7 before addd = ",list7)
    i,result_reciver = 0,0
    while i != len(list7):
        result_reciver = dec_to_hex(hex_to_dec(result_reciver) + hex_to_dec(list7[i]))
        i = i + 1

    print("result Reciver add with zero = ", result_reciver)

    list8 = Remove_Leading_zero(result_reciver)

    if len(list8) > 4:
        a = list8.pop(0)
        print(list8)
        str1 = ''.join(list8)  # converting a list to string
        final_result = dec_to_hex(hex_to_dec(str1) + hex_to_dec(a))

    print("final result with zero = ", final_result)

    list9 = Remove_Leading_zero(final_result)

    print("final result without zero = ", list9)

    complement = hex(int(final_result, 16) ^ 0xFFFF)
    return complement

def Loading():
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rSending ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r    ')

    t = threading.Thread(target=animate)
    t.start()
    #long process here
    time.sleep(1)
    done = True

def Corrupt(D):
    print("Do you wish to currupt the data")
    x = input()
    if x == 'Y' or x == 'y':
        print("1.Bit or 2.Burst Error")
        z = int(input())
        if z == 1:
            print(list7)
            y = int(input("Enter the position you wish to corrupt at"))
            list7[y] = input("Enter the data to be replaced")
            print("list 7 after replaced = ",list7)
            return list7
        elif z == 2:
            w = int(input("Enter the number of Errors you want"))
            print(list7)
            for i in range(w):
                print("Enter the ",i," position you wish to corrupt at")
                y = int(input())
                list7[y] = input("Enter the data to be replaced")
                print("list 7 after replaced = ", list7)
            return list7
    else:
        return list7

list1 = []  # contains original text to hexadecimal values
list2 = []  # contains hexadecimal values without ':'
list3 = []  # contains hexadecimal values without 0x
list4 = []  # contains hexadecimal values merge of 2 elements
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
i,result = 0,0

text_original = input("Enter the text message to be sent")  # contains original values

list4 = Get_Text(text_original)

list4 = [element.upper() for element in list4]  # capitalization

while i != len(list4):
    result = dec_to_hex(hex_to_dec(result) + hex_to_dec(list4[i]))
    i = i + 1

print("Result sum with zero = ",result)

list5 = Remove_Leading_zero(result)

print("Result sum without zero in list = ",list5)

if len(list5) > 4:
    a = list5.pop(0)
    print(list5)
    str1 = ''.join(list5)  # converting a list to string
    result_new = dec_to_hex(hex_to_dec(str1) + hex_to_dec(a))

print("Result(2) new with zero = ",result_new)

list6 = Remove_Leading_zero(result_new)

print("Result(2) new sum without zero in list = ",list6)

check_sum = hex(int(result_new, 16) ^ 0xFFFF)

print("CheckSum =",check_sum)

print("Do you wish to send the Data")
x = input()

if x == 'Y' or x == 'y':
    print("Data Sending...")
    Loading()
    print("Data Has been sent")

    complement = Reciver(list4,check_sum,list7)
elif x == 'N' or x == 'n':
    print("Data has not been sent")
    print("Thank YOU")
    sys.exit()

print("compliment",complement)

if complement == '0x0':
    print("Data has been received")
else:
    print("Error has occured")
