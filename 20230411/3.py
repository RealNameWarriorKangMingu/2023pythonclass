outStr = ""
inStr = input("문자열 입력 : ")
count = len(inStr)

for k in range(0, count) :
    outStr += inStr[count - (k + 1)]

print("내용을 거꾸로 출력 --> %s" % outStr)

#outStr = ""
#inStr = input("문자열 입력 : ")
#count = len(inStr)

#for k in range(count -1, -1, -1) :
    #outStr += inSstr[k]

#print("내용을 거꾸로 출력 --> %s" % outStr)