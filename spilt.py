senteace='My name is Sana'
def spilt():
   spilt_value= []
   tmp=""
   for c in senteace:
      if c==' ':
        spilt_value.append(tmp)
        tmp=''
      else:
        tmp += c
   if tmp:
    spilt_value.append(tmp)
    print(spilt_value)
spilt()
