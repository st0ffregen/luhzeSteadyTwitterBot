#!/usr/bin/env python
# -*- coding: utf-8 -*-

tweetArray = [
"https://www.luhze.de/unterstuetzen/ - Jetzt die Journalist*innen von morgen unterstützen: Ehemalige luhze-Redakteur*innen arbeiten heute für bekannte Medien wie FAZ, Mitteldeutsche Zeitung, MDR und taz.",
"https://www.luhze.de/unterstuetzen/ - Kräutertee: Unser Abo für Neugierige. Unterstütze uns mit 3€ pro Monat und erhalte als Dankeschön unseren Newsletter mit Hintergrundinfos und Geschichten aus der Redaktion.",
"https://www.luhze.de/unterstuetzen/ - Kräutertee: Unser Abo für Ungeduldige. Unterstütze uns mit 3€ pro Monat und erhalte das PDF der Ausgabe zwei Tage vor dem offiziellen Erscheinungstermin.",
"https://www.luhze.de/unterstuetzen/ - Kaffee: Unser Abo für Faule. Unterstütze uns mit 5€ pro Monat und luhze kommt zu dir nach Hause! (nur innerhalb Leipzigs)",
"https://www.luhze.de/unterstuetzen/ - Smoothie: Unser Abo für Mitteilsame. Unterstütze uns mit 10 € pro Monat und erhalte eine kostenlose Kleinstanzeige.",
"https://www.luhze.de/unterstuetzen/ - Nie wieder Angst vor geistigem Vitaminmangel! Mit dem Smoothie-Abo bekommst du unseren Newsletter, das PDF unserer Zeitung vorab, und wenn du in Leipzig wohnst, auch die Printausgabe in den Briefkasten.",
"https://www.luhze.de/unterstuetzen/ - Über unser Crowdfunding kannst du unabhängigen Journalismus mit nur wenigen Klicks und Euros unterstützen. Dafür bekommst du z.B. Einblicke in unseren Redaktionsalltag (Kräutertee-Abo) oder eine kostenlose Kleinstanzeige (Smoothie-Abo).",
"https://www.luhze.de/unterstuetzen/ - Bei luhze arbeiten alle ehrenamtlich. Aber auch wir müssen die Miete für unser Büro und vor allem Druckkosten für die Print-Ausgabe zahlen. Unterstütze uns deshalb jetzt!",
"https://www.luhze.de/unterstuetzen/ - luhze - Das steht für Leipzigs unabhängige Hochschulzeitung. Diese Unabhängigkeit verdanken wir auch unseren Unterstützer*innen. Dankeschön!",
"https://www.luhze.de/unterstuetzen/ - Du magst keine festen Strukturen? Du weißt ganz genau, wie viel wir dir wert sind, keinen Cent mehr oder weniger? Dann überweise uns einfach so einen Betrag, am liebsten regelmäßig.",
"https://www.luhze.de/unterstuetzen/ - Alternativ zum Steady-Abo könnt ihr auch per Dauerauftrag einen festen Betrag auf unser Konto überweisen. So kommt mehr von eurem Geld bei uns an. Und wenn ihr spenden@luhze.de Bescheid sagt, schicken wir euch auch dann alle Steady-Vorteile zu.",
"https://www.luhze.de/unterstuetzen/ - Schon für den Preis eines veganen Gerichts in der Mensa könnt ihr unabhängigen jungen Journalismus für Studierende, Hochschulangehörige und alle anderen Leipziger*innen unterstützen.",
"https://www.luhze.de/unterstuetzen/ - Nur wegen der Menschen, die uns per Crowdfunding oder mit Spenden unterstützen, können wir auch in Corona-Zeiten regelmäßig in Print erscheinen. Vielen Dank dafür!"
"https://www.luhze.de/unterstuetzen/  - Du liest gerne luhze - Leipzigs unabhängige Hochschulzeitung und trinkst dabei Kräutertee? Dann unterstütze uns mit 3 Euro pro Monat über unser Crowdfunding.",
"https://www.luhze.de/unterstuetzen/  - Du liest gerne luhze - Leipzigs unabhängige Hochschulzeitung und trinkst dabei Kaffee? Dann unterstütze uns mit 5 Euro pro Monat über unser Crowdfunding.", 
"https://www.luhze.de/unterstuetzen/  - Du liest gerne luhze - Leipzigs unabhängige Hochschulzeitung und trinkst dabei einen Smoothie? Dann unterstütze uns mit 10 Euro pro Monat über unser Crowdfunding.", 
"https://www.luhze.de/unterstuetzen/  - Kräutertee, Kaffee und Smoothies haben auf den ersten Blick nicht viel gemeinsam. Auf den zweiten unterstützen sie luhze bei ihrer Arbeit: unabhängigen Hochschuljournalismus von Studierenden für Studierende kostenlos zu produzieren.",
"Nie wieder Angst vor geistiger Dehydration! Unterstütze luhze mit einem Kräutertee-, Kaffee- oder Smoothie-Abo. https://www.luhze.de/unterstuetzen/ ",
"https://www.luhze.de/unterstuetzen/  - Du willst hinter die Kulissen schauen und wissen, was in der Redaktion passiert? Dann unterstütze uns mit 3€ pro Monat und erhalte als Dankeschön unseren Newsletter.",
"https://www.luhze.de/unterstuetzen/  - Du kannst es nicht erwarten, die neue luhze-Ausgabe zu lesen? Dann unterstütze uns mit 3€ pro Monat und erhalte das PDF der Ausgabe zwei Tage vor dem offiziellen Erscheinungstermin.",
"https://www.luhze.de/unterstuetzen/  - Du willst luhze in deinem Briefkasten? Dann unterstütze uns mit 5€ pro Monat und nutze unseren exklusiven Verteilservice. (nur innerhalb Leipzigs)",
"https://www.luhze.de/unterstuetzen/  - Ohne Kaffee würde kaum jemand von uns die langen Nächte von Endredaktion und Recherchen überstehen. Mit dem gleichnamigen Paket sorgst du dafür, dass luhze weiterhin so sorgfältig arbeiten kann, wie wir es über 20 Jahren tun.", 
"https://www.luhze.de/unterstuetzen/ - Mit dem Smoothie-Abo gibst du uns einen Vitaminboost! Deine Unterstützung hilft uns dabei, luhze weiterzuentwickeln – ob mit Seminarwochenenden, noch mehr langfristigen Recherchen oder mutigen Veränderungen in der Zeitung.", 
"https://www.luhze.de/unterstuetzen/ - Mit dem Kräutertee-Paket hältst du uns am Laufen – so wie es kannenweise Kräutertee während Redaktionssitzungen tun.", 
"https://www.luhze.de/unterstuetzen - Wir machen Zeitung - seit fast 20 Jahren. Unterstütze mit deiner Spende unabhängigen Hochschuljournalismus!",
"https://www.luhze.de/unterstuetzen/ - luhze ist das einzige unabhängige Medium in Leipzig, das über Hochschulpolitik und die Belange Studierender berichtet. Das heißt aber leider nicht, dass wir ohne finanzielle Unterstützung auskommen.", 
"https://www.luhze.de/unterstuetzen/ - Damit wir weiterhin kritisch auf die Leipziger Hochschulen blicken und über die Interessen der Studierenden schreiben können, brauchen wir eure Unterstützung.", 
"https://www.luhze.de/unterstuetzen/ - Hinter luhze steht ein Team, das neben dem Studium ehrenamtlich alle Aufgaben übernimmt, die für die Produktion einer Zeitung notwendig sind – bis auf den eigentlichen Druck. Um diesen weiterhin gewährleisten zu können, brauchen wir eure Unterstützung.", 
"https://www.luhze.de/unterstuetzen/ - Waschmaschine gesucht, Bett zu verschenken - oder ein Heiratsantrag in der Zeitung? Unterstütze uns mit 10€ pro Monat und du kannst kostenlose Kleinstanzeigen schalten.",
"Noch auf der Suche nach einem tollen Geburtstagsgeschenk? Wir hätten da eine Idee: https://www.luhze.de/unterstuetzen/"
]
