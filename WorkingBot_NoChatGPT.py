import pyautogui as py
import time
import clipboard
import cv2
import keyboard
import os
import json
import sys
import random
from Send_Notification import send_pushover_message

#https://myaccount.google.com/data-and-privacy?utm_source=OGB&utm_medium=app
#1. Reset, wenn es Probleme geben sollte (für jeden loop setzen wir "count" ein bis 50 und wenn nicht gefunden wird, soll ein Reset durchgeführt werden.(zurück zu main und scroll nach unten nicht vergessen))
#act as an apartment seeker, you are interested in all apartments, your name is Lara Brunner, you are 23 years old, you live in Berlin, you write your cover letters only in german, your cover letter always starts with "Sehr geehrte/geehrter/geehrtes", your cover letters are random, write depending on the following information:




api_token = "aribvoi9i4crzz42ydamjehvfzzn7j" #für pushnachrichten
user_key = "utb76t214ojqeq7fxt2oiwxwbjbu3a" #für pushnachrichten
message = 'Capcha on Screen' #Text der auf dem Handy ausgespuckt wird


#für Troubleshooting

#noch für oder nicht für premium machen.
#https://www.immobilienscout24.de/expose/149619965?referrer=RESULT_LIST_LISTING%2CTOTAL_RENT&searchId=6a6ae48a-3eaa-3240-af94-677252c77f34&searchType=drawn_area#/
link = "https://www.immobilienscout24.de/Suche/shape/wohnung-mieten?shape=cXFnX0lrX19vQWZ5Q2NQdWJDY0U7ZWVyX0lzY19vQXpiQWl4SHhoQF9dcHRCbHtCfm9BamRFfHRAbkFmfkV9ZEZ6eER1YlN5eUtpZk97ZkdjYVZnc0BxcEFldUFxR2FoQXZ2QGFoQXJsQ31uRm55Q2d6QXh9Q3FnRWZtUnBnRXZ0TGB1QXdYdU5zc0ZgTHZYamVBcH5HdWhAbGJGemBAbGJGYn5DYF0.&numberofrooms=-2.0&price=-850.0&livingspace=30.0-&exclusioncriteria=projectlisting,swapflat&pricetype=calculatedtotalrent&sorting=2"
clipboard.copy(link)
Legende = {
    "averageTimerForLoop":0.1,
    "averageTimeGeneral":0.2,
    "copyInformation":0.6
}






######################################################################################################################################################################







filePath_pictures = os.path.dirname(os.path.realpath(sys.argv[0]))+"\\"

def MouseMover():
    beenden()
    py.moveTo(3, 3)
        
def beenden():
    if keyboard.is_pressed("ctrl+alt+shift"):
        exit()

def lookingForPixel(name):
    beenden()
    MouseMover()
    print("looking for " + name)
    time.sleep(0.2)
    picture1 = py.screenshot() #region=(1446, 597, 220, 230) minimap location  #start while in game

    picture1.save(os.path.join(filePath_pictures, "whatsapp.jpg"))

    TestJungle = cv2.imread(os.path.join(filePath_pictures, "Bilder\\", name + ".PNG"), cv2.IMREAD_UNCHANGED)
    DesktopTest = cv2.imread(os.path.join(filePath_pictures, "whatsapp.jpg"), cv2.IMREAD_UNCHANGED)

    nesne = cv2.cvtColor(DesktopTest, cv2.COLOR_BGR2GRAY)
    nesne1 = cv2.cvtColor(TestJungle, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(nesne1, nesne, cv2.TM_CCOEFF_NORMED)

    beenden()

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("done looking for " + name)
    return max_loc, max_val


def waitingForRobot(): # sorgt dafür, dass es wartet, bis ich die Captcha gemacht habe (Captcha lösen und dann keyboard.is_pressed erfüllen)
    beenden()
    print("überprüfung nach Robot")
    beenden()
    
    max_val1 = lookingForPixel("Roboter")[1]

    count= 0
    while max_val1 < 0.90 :
        time.sleep(Legende["averageTimerForLoop"]+0.3)
        max_val1 = lookingForPixel("Roboter")[1]
        count += 1
        if count > 5:
            break
    
    
    max_val = lookingForPixel("Roboter")[1]
    beenden()
    
    beenden()
    if max_val < 0.90:
        beenden()
        print("Es wird keinen Captcha benötigt")
        beenden()
        return False
    else:
        print("Es wird Captcha abgefragt")
        send_pushover_message(api_token, user_key, message)
        beenden()
        statusLoop = True
        beenden()
        while statusLoop:
            beenden()
            time.sleep(0.003)
            beenden()
            if keyboard.is_pressed("ctrl+q"):
                beenden()
                statusLoop = False
                beenden()
        aktualisierenDerSeite()
        beenden()
        print("Die Robotüberprüfung ist fertig")
        beenden()
        return True
    
    
script_dir = "C:\\Users\\vboxuser\\Desktop\\BAckup"
# script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))  # deactivated for custom path
dateipfad = os.path.join(script_dir, "Informationen für den Bot", "persönliche Daten.json")
with open(dateipfad, 'r') as json_datei:
    eigeneDaten = json.load(json_datei)
        

if eigeneDaten["haustiere"] == "ja":
    haustiere = True
else:
    haustiere = False
    
    
def randomClicking(max_loc):
    if random.randint(0, 9) == 1:
        py.click(max_loc) 
        beenden()
        x,y=max_loc
        beenden()
        if random.randint(0, 3) == 0:
            py.moveTo(x+(random.randint(0, 1920)),y+(random.randint(0, 1080))) #damit der button zu einem X wird
        elif random.randint(0, 3) == 1:
            py.moveTo(x-(random.randint(0, 1920)),y-(random.randint(0, 1080))) #damit der button zu einem X wird
        elif random.randint(0, 3) == 2:
            py.moveTo(x-(random.randint(0, 1920)),y+(random.randint(0, 1080))) #damit der button zu einem X wird
        elif random.randint(0, 3) == 3:
            py.moveTo(x+(random.randint(0, 1920)),y-(random.randint(0, 1080))) #damit der button zu einem X wird


    else:
        keyboard.press_and_release("strg+f5")
#####################################################################################################################################################################



















    ## 2
def aktualisierenDerSeite(): #aktualisiert JEDE Webseite und schaut, ob diese aktualisiert wurde (sucht nach dem Button, clickt diesen und checkt bis zum Ende)
    print("Die aktuelle Seite wird aktualisiert")
    beenden()
    max_loc, max_val = lookingForPixel("Aktualisieren")
    beenden()
    x, y = max_loc
    beenden()
    while max_val < 0.90: #während es false ist
        beenden()
        max_loc, max_val = lookingForPixel("Aktualisieren") #erneut versuchen
        beenden()
        time.sleep(Legende["averageTimerForLoop"])
        beenden()
    print("Button zum Aktualisieren gefunden!")
    beenden()
    print("Aktualisieren der Seite!")
    beenden()
    randomClicking(max_loc)
    beenden()
    time.sleep(Legende["averageTimeGeneral"]+1.4)
    beenden()
    max_loc, max_val = lookingForPixel("Aktualisieren")
    beenden()
    while max_val < 0.90: #checkt, ob die Seite fertig geladen ist
        beenden()
        max_loc, max_val = lookingForPixel("Aktualisieren")
        beenden()
        time.sleep(Legende["averageTimerForLoop"])
        beenden()
    _ = waitingForRobot()
    beenden()
    time.sleep(1) #um sicher zu gehen, dass die Herzen ihre Farbe annehmen (weil die Seite schlecht programmiert wurde)
    beenden()
    print("Die Seite ist aktualisiert und kann nun genutzt werden")#ende
    beenden()





    ## 3
def scrollingDown(): #scrollt bei der Startseite runter
    beenden()
    print("Es wird nun gescrollt")
    beenden()
    py.moveTo(1920/2, 1080/2)
    beenden()
    py.scroll(-500)
    beenden()
    print("Es wurde gescrollt!")
    beenden()





    ## 4
def checkingForRedHearth():
    beenden()
    print("Bot checkt nach weißem Herz")
    beenden()
    max_loc, max_val = lookingForPixel("oberesHerzWeiss")
    beenden()
    counterHeart = 0
    beenden()
    x, y = max_loc
    beenden()
    while max_val < 0.90:
        beenden()
        max_loc, max_val = lookingForPixel("oberesHerzWeiss")
        beenden()
        time.sleep(Legende["averageTimerForLoop"])   
        beenden()
        counterHeart += 1
        beenden()
        if counterHeart > 3:
            beenden()
            break
    if counterHeart <= 3:
        beenden()
        py.click(x-100, y)
        beenden()
        print("auf das herz geklickt")
        beenden()
    else:
        print("nicht klicken, weil herzen sind rot oder nicht zu sehen")
        beenden()
    print("Bot ist fertig mit dem Checken")
    beenden()
    if counterHeart > 3:
        beenden()
        counterHeart = 0
        beenden()
        return "noHearth"
    else:
        beenden()
        return "withHearth"
    

    
    
    
#Robot, deaktiviert, gemerkt und kein Internet
#internet fehlt noch

    ## 5
def checkingIfExpoIsDeactivated(): # checkt, ob die Immobilie deaktiviert wurde
    beenden()
    print("Es wird nun überprüft, ob das Expo noch existiert oder nicht")
    beenden()
    max_val = lookingForPixel("Aktualisieren")[1]# checken, ob die Seite geladen ist
    beenden()
    while max_val < 0.90: # wenn die Seite noch nicht geladen ist
        beenden()
        max_val = lookingForPixel("Aktualisieren")[1]
        beenden()
        time.sleep(Legende["averageTimerForLoop"])
        beenden()
    max_val = lookingForPixel("ButtonNachricht")[1]
    beenden()
    if max_val < 0.90: # wenn der Nachrichten-Button nicht in Sicht ist
        beenden()
        print("Es könnte sein, dass Captcha abgefragt werden")
        beenden()
        robotOrNot = waitingForRobot()
        beenden()
        if robotOrNot == False:
            beenden()
            keyboard.press_and_release("alt+left")
            beenden()
            time.sleep(2)
            beenden()
            print("es ist deaktiviert")
            beenden()
            return "es ist deaktiviert"
        else:
            print("Überprüfung ob es noch existiert oder nicht ist beendet")
            beenden()
            pass
    else: # wenn der Nachrichten-Button zu sehen ist
        print("Überprüfung ob es noch existiert oder nicht ist beendet")
        beenden()
        pass
        
        
    
    
    
    
    
    
    ## 6
def checkingForPremium():
    beenden()
    max_loc, max_val = lookingForPixel("ButtonNachricht")# checken, ob der Button da ist
    beenden()
    x, y = max_loc
    beenden()
    while max_val < 0.90:
        beenden()
        max_loc, max_val = lookingForPixel("ButtonNachricht")# checken, ob die Seite geladen ist
        beenden()
        time.sleep(Legende["averageTimerForLoop"])
        beenden()
    py.click(x+5, y+3)
    beenden()
    time.sleep(2)
    beenden()
    max_loc, max_val = lookingForPixel("ForPlus")# checken, ob der Button da ist
    beenden()
    if max_val > 0.90: # wenn es nur für plus member ist, dann skippen
        time.sleep(Legende["averageTimeGeneral"])
        beenden()
        keyboard.press_and_release("alt+left")
        beenden()
        time.sleep(2)
        max_loc, max_val = lookingForPixel("merken")
        beenden()
        x, y = max_loc
        py.click(x+4, y+4)
        time.sleep(1)
        keyboard.press_and_release("alt+left")
        beenden()
        return "premium"
    else:
        time.sleep(Legende["averageTimeGeneral"])
        max_loc, max_val = lookingForPixel("schliessen")
        beenden()
        py.click(max_loc)
        time.sleep(Legende["averageTimeGeneral"]+0.7)
        print("somit wird die Bewerbung für die Immobilie fortgesetzt")
        
        
    
def doubleCheckHearth():
    print("doppelte überprüfung, ob ich mich schon darauf beworben habe oder nicht")
    if lookingForPixel("gemerkt")[1] < 0.90:
        print("auf diese Wohnung wurde sich wirklich noch nciht beworben")
        return True
    else:
        print("auf diese Wohnung wurde sich schon beworben")
        return False
        
    
    
    
    
    ## 7    
def checkingIfPictureOrNot():
    print("eine Überpfüfung noch um zu schauen, ob ein Bild der Immobilie vorhanden ist.")
    max_loc, max_val = lookingForPixel("KeinBild")# checken, ob ein Bild da ist, oder nicht
    if max_val > 0.90: # wenn kein Bild vorhanden ist, dann soll "merken" angeklickt werden und somit wird die Immobilie ignoriert
        beenden()
        max_loc, max_val = lookingForPixel("merken")# checken, ob ein Bild da ist, oder nicht
        time.sleep(Legende["averageTimeGeneral"])
        py.click(max_loc)
        for i in range(4):    
            beenden()
            time.sleep(Legende["averageTimeGeneral"])
        keyboard.press_and_release("alt+left")
        time.sleep(Legende["averageTimeGeneral"])
        beenden()
        print("leider ist kein Bild vorhanden, die Bewerbung muss abgebrochen werden!")
        return "kein Bild"
    else:
        pass # weil ein Bild vorhanden ist, kann die Bewerbung fortgesetzt werden
        

    
    
    
    ## 8
def takingNameOFthePerson():
    print("Entnimmt der Expo den Namen des Vermieters/Anbieter") # beachte, dass selten kein Name angegeben ist
    max_loc, max_val = lookingForPixel("ButtonNachricht")# checken, ob der Button da ist
    x, y = max_loc
    beenden()
    while max_val < 0.90:
        max_loc, max_val = lookingForPixel("ButtonNachricht")# checken, ob die Seite geladen ist
        time.sleep(Legende["averageTimerForLoop"])
    py.moveTo(x+350, y-78) 
    time.sleep(Legende["averageTimeGeneral"])
    beenden()
    for i in range(3):
        py.click()
    time.sleep(Legende["averageTimeGeneral"]) 
    keyboard.press_and_release("ctrl+c")
    beenden()
    time.sleep(Legende["copyInformation"])
    print("Entnahme des Vermieters ist beendet")
    return clipboard.paste()
        
        
        
        

    ## 9
def takingAdresse():
    print("extrahierung der Adresse wird nun ausgeführt")
    time.sleep(Legende["averageTimeGeneral"])
    py.moveTo(1920/2, 1080/2)
    beenden()
    py.scroll(-700)
    max_loc= lookingForPixel("Pin")[0]# checken, ob der Button da ist
    x, y = max_loc
    beenden()
    for i in range(3):
        py.click(x+120, y)
    keyboard.press_and_release("ctrl+c")
    time.sleep(Legende["copyInformation"])
    ersteAdresse = clipboard.paste()
    for i in range(3):
        py.click(x+340, y)
    keyboard.press_and_release("ctrl+c")
    beenden()
    time.sleep(Legende["copyInformation"])
    zweiteAdresse = clipboard.paste()
    beenden()
    dieVollständigeAdresse = ersteAdresse+" "+zweiteAdresse
    print("Die Adresse wurde erfolgreich extrahiert!\n\n\n\n\n\n\n\n")
    return dieVollständigeAdresse
    
    
    
    
    
    
    ## 10
def Wohnungsinfo(): # Extrahierung der Datung über die Wohnung
    print("nun extrahieren wird die letzten Informationen der Wohnung")
    max_loc= lookingForPixel("kaltmiete")[0]# checken, ob der Button da ist
    beenden()
    x, y = max_loc
    py.moveTo(x, y-70)
    time.sleep(Legende["averageTimeGeneral"])
    beenden()
    py.mouseDown()
    time.sleep(Legende["averageTimeGeneral"])
    py.dragTo(x-10, y+299, 0.5)
    time.sleep(Legende["averageTimeGeneral"])
    py.mouseUp
    time.sleep(Legende["averageTimeGeneral"])
    beenden()
    keyboard.press_and_release("ctrl+c")
    beenden()
    time.sleep(Legende["copyInformation"])
    Nebeninformation = clipboard.paste()
    print("Die letzten Informationen der Wohnung wurden extrahiert")
    return Nebeninformation




    
    ## 11
def wechselDesBrowsers():
    keyboard.press_and_release("ctrl+tab")
    beenden()
    
    
    
    
    
    
    ## 12
def zusammensetzungDerNachricht(Name, Adresse):
    print("Alle Informationen werden nun zusammengefügt und im selben Schritt zum Ergebnis analysiert")
    try:
        print(Adresse[len(Adresse)-3])
        if Adresse[len(Adresse)-3] == ".":
            print(len(Adresse)-65)
            newAdress = ""
            for i in range(len(Adresse)-70):
                print(newAdress)
                newAdress += Adresse[i]
            Adresse = newAdress
        else:
            pass
    except:
        print(TypeError)
    bewerbung = f"""Sehr geehrte Damen und Herren,

mit großem Interesse habe ich Ihr Angebot für die Mietwohnung in der {Adresse} gelesen. Aufgrund meiner persönlichen und beruflichen Situation bin ich auf der Suche nach einer neuen Wohnung und bin davon überzeugt, dass Ihr Objekt meinen Vorstellungen entspricht.

Mein Name ist {eigeneDaten["name"]} und ich bin {eigeneDaten["alter"]} Jahre alt. Ich arbeite als {eigeneDaten["beruf"]} bei {eigeneDaten["arbeitgeberOderSchule"]} und habe ein stabiles Einkommen. Der Umzug in Ihre Wohnung würde es mir ermöglichen, näher an meinem Arbeitsplatz zu sein und gleichzeitig in einem angenehmen Umfeld zu leben.

Zuverlässigkeit, Sauberkeit und ein respektvoller Umgang mit dem Mietobjekt sind für mich selbstverständlich. Ich bin Nichtraucher und habe keine Haustiere. Zudem verfüge ich über eine positive Schufa-Auskunft und kann bei Bedarf auch Referenzen vorlegen.
Die Lage Ihrer Wohnung ist für mich äußerst attraktiv, da sie sich in einer ruhigen und dennoch gut angebundenen Gegend befindet. Die Beschreibung der Ausstattung entspricht genau meinen Bedürfnissen, und ich bin sicher, dass ich mich in dieser Umgebung schnell wohl fühlen würde.

Gerne stehe ich für weitere Fragen zur Verfügung und würde mich sehr darüber freuen, die Wohnung persönlich zu besichtigen. Ich bin flexibel bezüglich eines Besichtigungstermins und stehe für Rückfragen jederzeit zur Verfügung.

Mit freundlichen Grüßen,
{eigeneDaten["name"]}
{eigeneDaten["telefon"]}
{eigeneDaten["email"]}"""
    time.sleep(Legende["averageTimeGeneral"])
    clipboard.copy(bewerbung)
    time.sleep(0.5)






    ## 13
def ExtraktionAusGPT():
    print("Die fertigen Daten werden extrahiert aus GPT")
    max_loc, max_val = lookingForPixel("writing")
    beenden()
    while max_val > 0.90:
        max_loc, max_val = lookingForPixel("writing")
        beenden()
        time.sleep(Legende["averageTimerForLoop"])
    time.sleep(Legende["averageTimeGeneral"]+0.2)
    max_loc, max_val = lookingForPixel("copy")
    while max_val < 0.90:
        max_loc, max_val = lookingForPixel("copy")
        beenden()
        time.sleep(Legende["averageTimerForLoop"])
    time.sleep(1)
    for i in range(2):    
        py.click(max_loc[0]+2, max_loc[1]+2)
    max_loc, max_val = lookingForPixel("loeschen")
    x, y = max_loc
    time.sleep(Legende["averageTimeGeneral"])
    py.click(x, y)
    print("Die Extrahierung sollte erfolgreich gewesen sein!")
    beenden()
       
       
       
       

    ## 14
def nachrichtSchreiben():
    print("TAB wird nun gewechselt und Nachricht wird geschrieben")
    #keyboard.press_and_release("ctrl+tab")
    time.sleep(Legende["averageTimeGeneral"])
    max_loc, max_val = lookingForPixel("ButtonNachricht")
    while max_val < 0.90:
        max_loc, max_val = lookingForPixel("ButtonNachricht")
        time.sleep(Legende["averageTimerForLoop"])
        beenden()
    py.click(max_loc)
    max_loc, max_val = lookingForPixel("IhreNachricht")
    while max_val < 0.90:
        max_loc, max_val = lookingForPixel("IhreNachricht")
        time.sleep(Legende["averageTimerForLoop"])
        beenden()
    time.sleep(Legende["averageTimeGeneral"]+0.8)
    max_loc, max_val = lookingForPixel("IhreNachricht")
    x, y = max_loc
    py.click(x-15, y-15)
    time.sleep(Legende["averageTimeGeneral"])
    keyboard.press_and_release("ctrl+a")
    beenden()
    keyboard.press_and_release("ctrl+v")
    print("TAB wechseln und Nachricht schreiben ist fertig")
    py.moveTo(x+100, y+100)
    
        
    
        
    ## 15
def abschickenDerNachricht(haustiere):
    print("abschicken der nachricht und bescheid geben, dass wir haustiere besitzen oder keine haustiere")
    max_loc, max_val = lookingForPixel("absender")
    max_loc1 = lookingForPixel("runter")[0]
    beenden()
    x1, y1 = max_loc1    
    while max_val < 0.90:
        for i in range(20):
            py.click(x1+2, y1+2)
            beenden()
        time.sleep(0.1)
        max_val = lookingForPixel("absender")[1]
    if haustiere == False:
        max_loc, max_val = lookingForPixel("haustiere")
        if max_val >0.90:
            x, y=max_loc
            py.click(x+15, y+15)
            time.sleep(Legende["averageTimeGeneral"]+0.1)
            for i in range(2): #um mit nein zu antworten
                keyboard.press_and_release("down")
                time.sleep(Legende["averageTimeGeneral"]+0.1)
            keyboard.press_and_release("enter")
    else:
        max_loc, max_val = lookingForPixel("haustiere")
        if max_val >0.90:
            x, y=max_loc
            py.click(x+15, y+15)
            time.sleep(Legende["averageTimeGeneral"]+0.1)
            for i in range(1): #um mit ja zu antworten
                keyboard.press_and_release("down")
                time.sleep(Legende["averageTimeGeneral"]+0.1)
            keyboard.press_and_release("enter")
    time.sleep(0.2)
    max_loc, max_val = lookingForPixel("absender")
    # py.click(max_loc)
    # max_loc, max_val = lookingForPixel("abgesendet")
    # while max_val < 0.90:
    #     max_loc, max_val = lookingForPixel("abgesendet")
    #     time.sleep(Legende["averageTimerForLoop"])
        #Deactivated for testing
    
    
    
    




















    
    
## 1
print("start")
def Main():
    while True:
        time.sleep(0.001)
        if keyboard.is_pressed("q"): #for troubleshooting
            print("hi")
            ScrollingOnce = 0
            while True:
                time.sleep(1)   #wartet 0.08 Sekunden
                aktualisierenDerSeite() ## 2
                time.sleep(Legende["averageTimeGeneral"])
                if ScrollingOnce == 0:
                    scrollingDown() ## 3
                    beenden()
                    ScrollingOnce+=1
                time.sleep(Legende["averageTimeGeneral"])
                statusHearth = checkingForRedHearth() ## 4
                if statusHearth == "noHearth":
                    print("no Hearth")
                    continue
                else:
                    time.sleep(Legende["averageTimeGeneral"])
                    beenden()
                    aktuellerStatus = checkingIfExpoIsDeactivated() ## 5
                    if aktuellerStatus == "es ist deaktiviert":
                        continue # wenn die Wohnung Sekunden nach der Veröffentlichung deaktiviert wurde, soll der Loop wieder neu beginnen
                    else:
                        print("Die Immobilie ist nicht deaktiviert")
                    if eigeneDaten["premium"] == "no": # falls man kein Premium besitzen sollte, werden durch diese Line alle Premiumanzeigen ignoriert
                        print("person hat kein premium")
                        status = checkingForPremium() ## 6
                        if status == "premium":
                            beenden()
                            continue
                    else:
                        print("person hat premium")
                        
                    hearth = doubleCheckHearth()
                    if hearth == False:
                        keyboard.press_and_release("alt+left")
                        continue
                    else:
                        time.sleep(Legende["averageTimeGeneral"])
                        aktuellerStatus1 = checkingIfPictureOrNot() ## 7
                        if aktuellerStatus1 == "kein Bild":
                            continue # wenn kein Bild der Immobilie vorhanden ist, dann soll diese ignoriert werden
                        else:
                            print("Die Immobilie ist mit einem Bild vorhanden")
                        time.sleep(Legende["averageTimeGeneral"])
                        informationenÜberWohnung = {
                            "Name des Vermieters":"Name des Vermieters: "+takingNameOFthePerson(), ## 8
                            "Standort der Wohnung":""+takingAdresse(), ## 9
                             ## 10 
                            }
                        #wechselDesBrowsers() ## 11
                        time.sleep(Legende["averageTimeGeneral"])
                        zusammensetzungDerNachricht(informationenÜberWohnung["Name des Vermieters"], informationenÜberWohnung["Standort der Wohnung"]) ## 12
                        time.sleep(Legende["averageTimeGeneral"])
                        beenden()
                        #ExtraktionAusGPT() ## 13
                        time.sleep(Legende["averageTimeGeneral"])
                        nachrichtSchreiben() ## 14
                        beenden()
                        time.sleep(Legende["averageTimeGeneral"])
                        abschickenDerNachricht(haustiere) ## 15
                        
                        #last step
                        keyboard.press_and_release("alt+left")
                        time.sleep(Legende["averageTimeGeneral"])
                        max_loc, max_val = lookingForPixel("Aktualisieren")
                        while max_val < 0.90:
                            max_loc, max_val = lookingForPixel("Aktualisieren")
                            time.sleep(0.1)
                        time.sleep(random.uniform(5.323, 11.45563))
                        #end and now from beginning
                    
                    



if __name__ == "__main__":
    Main()







