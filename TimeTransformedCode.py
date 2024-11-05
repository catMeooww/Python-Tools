import datetime
import pyperclip

#Time and Text getters
def getTime():
    time = datetime.datetime.now().time()
    timeStr = str(time).replace(":","").replace(".","")
    return timeStr

alphabet = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "0","1","2","3","4","5","6","7","8","9",
    " ","-","/",",",".","!","?",":",";"
    ]

#Implemented Program
def main():
    print("_______________________________________________")
    print("Welcome to Time Transformed Code decoder:")
    print("1- Encode a text")
    print("2- Decode a text")
    print("3- Cancel")
    option = input("Select: ")
    print("_______________________________________________")
    if option == "1":
        data = encoding(input("Text: "),getTime())
        encoded = data['code']
        time = data['time']

        print("_______________________________________________")
        print("Code:",encoded)
        print("Time:",time)
        print("_______________________________________________")
        print("1-Copy")
        print("2-Save")
        print("3-Exit")

        option = input("Select: ")
        if option == "1":
            pyperclip.copy(f"{encoded}\n___________\n{time}")
        elif option == "2":
            with open("code.txt","w") as file:
                file.write(f"___________\nCode: {encoded}\n___________\nTime: {time}\n___________")

        print("_______________________________________________")

    elif option == "2":
        data = decoding(input("Text: "),input("Time: "))
        decoded = data["text"]

        print("_______________________________________________")
        print("Text:",decoded)
        print("_______________________________________________")
        print("1-Copy")
        print("2-Save")
        print("3-Exit")

        option = input("Select: ")
        if option == "1":
            pyperclip.copy(f"{decoded}")
        elif option == "2":
            with open("code.txt","w") as file:
                file.write(f"___________\nText: {decoded}\n___________")

        print("_______________________________________________")

#Code Functions
def encoding(text,time):
    text = text.removeprefix("[TXT]").lower()
    newtext = ""
    loopTime = 0
    for letter in text:
        loopLetter = 0
        for a in alphabet:
            if a == letter:
                if loopLetter+int(time[loopTime]) > len(alphabet)-1:
                    index = loopLetter+int(time[loopTime])-len(alphabet)
                else:
                    index = loopLetter+int(time[loopTime])
                newtext = newtext + alphabet[index]
            loopLetter += 1
        if loopTime >= len(time)-1:
            loopTime = 0
        else:
            loopTime += 1
    
    return {
        "code":"[TTC]"+newtext,
        "time":time
        }

def decoding(text,time):
    text = text.removeprefix("[TTC]").lower()
    newtext = ""
    loopTime = 0
    for letter in text:
        loopLetter = 0
        for a in alphabet:
            if a == letter:
                if loopLetter-int(time[loopTime]) < 0:
                    index = loopLetter-int(time[loopTime])+len(alphabet)
                else:
                    index = loopLetter-int(time[loopTime])
                newtext = newtext + alphabet[index]
            loopLetter += 1
        if loopTime >= len(time)-1:
            loopTime = 0
        else:
            loopTime += 1

    return {
        "text":"[TXT]"+newtext,
        "time":time
        }


#Use program
if __name__ == "__main__":
    main()