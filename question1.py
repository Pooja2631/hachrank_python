list1=["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
i=0
string=""
while i<len(list1):
    if len(list1[i])>len(string):
        string=(list1[i])
    i+=1
print(string)
# print(string,"***",end="")


# string="bitcoin take over the world maybe who knows"
# x=string.split()
# i=0
# max=x[0]
# while i<len(x):
#     if len(x[i])>len(max):
#         max=(x[i])
#     i+=1
# print([max])