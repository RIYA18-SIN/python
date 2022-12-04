def remove_char(s1,s2):
    dict = {ord(s2) : None}
    print(s1.translate(dict))

s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 
