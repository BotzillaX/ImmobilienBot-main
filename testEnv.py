



prompt = "BetreFf: ich bin der coolste. sehr geehrter herr müller, sie sind auch cool!"



result = ""

for i in range(7):
    result += prompt[i]
    
if result.lower() == "betreff":
    result = ""
    count = 0
    counter = 0
    for char in prompt:
        counter += 1
        if char == " ":################
            count = 1
            print("hi")
            print(result)
        else:
            count = 0
            
        if count == 0:#################
            result+=char
        elif count == 1:
            if result.lower() == "sehr":
                break
            else:
                result = ""
            result = ""
    print(counter)
    prompt = prompt[counter-5::]
    
    print(prompt)
        