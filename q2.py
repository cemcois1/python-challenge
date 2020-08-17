
text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
def fonk(text):
   
    for i in range(len(text)):
        if(text[i]!=" "):
            if(chr(ord( text[i])+2)=="{"):
                print("a",end="")
            elif (chr(ord( text[i])+2)=="."):
                
                print(".",end="")
               
            elif (chr(ord( text[i])+2)=="z"):
                
                print("b",end="")
            elif (chr(ord( text[i])+2)=="w"):
                
                print("y",end="")
            else:
                print(chr(ord( text[i])+2),end="")
                
        else:
            print(" ",end="")

    
    
fonk("map")
