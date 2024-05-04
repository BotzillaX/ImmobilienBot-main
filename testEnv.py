



prompt = """**Betreff: Bewerbung für die Wohnung in der Kopenhagener Str. 42, 10437 Berlin**

Sehr geehrter Herr Guder,

mein Name ist Lara Brunner, ich bin 23 Jahre alt und derzeit wohnhaft in Berlin. Mit großem Interesse habe ich Ihr Mietangebot für die Etagenwohnung in der Kopenhagener Str. 42 in Prenzlauer Berg entdeckt und möchte mich hiermit als Mieterin bewerben.

Die Wohnung entspricht mit ihrer Größe von 63,3 m² und zwei Zimmern genau meinem Bedarf. Besonders angetan bin ich von der Möglichkeit, einen Balkon sowie einen Keller zu nutzen, was in Berlin nicht selbstverständlich ist. Die Angabe der Kaltmiete von 694,21 € und einer Warmmiete von 1.000,21 € passt ebenfalls gut in mein Budget.

Ich arbeite als [Ihre Berufsbezeichnung einfügen], was mir ein stabiles Einkommen sichert. Da die Wohnung ab dem 01.06.2024 bezugsfrei ist, würde dieser Termin ideal zu meinem Umzugsplan passen. 

Ich bin eine ruhige und verantwortungsbewusste Mieterin, die großen Wert auf ein gepflegtes Wohnambiente legt. Mein aktueller Vermieter kann Ihnen bestätigen, dass ich stets pünktlich die Miete zahle und mich umsichtig um die Wohnung kümmere.

Die Möglichkeit, Haustiere nach Vereinbarung halten zu können, ist ebenfalls ein Pluspunkt, da ich überlege, in Zukunft vielleicht ein kleines Haustier anzuschaffen.

Ich würde mich sehr freuen, wenn Sie mir die Gelegenheit geben könnten, die Wohnung persönlich zu besichtigen und Sie von meiner Zuverlässigkeit und Ernsthaftigkeit als Mieterin überzeugen zu können.

Für weitere Informationen oder zur Vereinbarung eines Besichtigungstermins stehe ich Ihnen gerne zur Verfügung. Ich freue mich auf Ihre Rückmeldung.

Mit freundlichen Grüßen,

Lara Brunner"""


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
    