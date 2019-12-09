class mp3_tag():
    def __init__(self, wykonawca, tytul, album, rok):
        self.wykonawca = wykonawca
        self.tytul = tytul
        self.album = album
        self.rok = rok
    def __str__(self):
        out = f"Wykonawca  :{self.wykonawca}\n"
        out += f"Utwór      :{self.tytul}\n"
        out += f"Album      :{self.album}\n"
        out += f"Rok        :{self.rok}\n"
        return f"{out}"
    
tags = []
tags.append(mp3_tag('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018'))
tags.append(mp3_tag('Eminem', 'The Real Slim Shady', 'The Marshall Mathers LP', '2000'))
tags.append(mp3_tag('Baha Men', 'Who let the dogs out ', 'Absolute Music 33', '2000'))
for tag in tags:
    print(tag)
