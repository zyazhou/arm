# import json
#
# f = open('./files/led.txt', 'wb+')
# d=1
# data = json.dumps((d)).encode('utf8')
# f.write(data)
# f.close()
#
#
# f = open('./files/led.txt', 'r')
# print(f.read())
# f.close()
#
#
# f = open('./files/led.txt', 'wb+')
# d=2222
# data = json.dumps((d)).encode('utf8')
# f.write(data)
# f.close()
#
#
# f = open('./files/led.txt', 'r')
# print(f.read())
# f.close()

str='ABC'
rest=str[0:1]+str[2:3]
print(rest)

for i in range(3,0,-1):
    print(i)