Phone =(input("Phone: "))
dic = {"1": " One ",
       "2": " Two ",
       "3": " Three ",
       "4": " Four ",
       "5": " Five ",
       "6": " Six ",
       "7": " Seven ",
       "8": " Eight ",
       "9": " Nine ",
       "10": " Ten ",
       "0": " Zero ",
       }
output = ""
for ch in Phone:
    output += dic.get(ch, "!")
print(output)