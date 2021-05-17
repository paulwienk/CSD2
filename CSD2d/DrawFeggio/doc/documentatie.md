# Documentatie prototype

### MoSCoW

MUST
- Mogelijkheid om te tekenen en kleuren aan te passen
- User interaction: geluid genereren wanneer er wordt getekend
- Verandering van de sound op basis van de kleuren in de tekening en de positie hiervan


SHOULD
- Mogelijkheid om de kleuren en dikte van de lijn aan te passen
- Verschillende functies van de lijnen: vervagen, bewegen etc



COULD
- Achtergrond animaties 
- Tekenen met spiegelbeeld en andere symmetrie


WOULD/WON'T
- mic input: tekenen met je stem



### Systeem diagram
![alt text](https://github.com/paulwienk/CSD2/blob/master/CSD2d/DrawFeggio/doc/drawfeggio_systemdiagram.png?raw=true)

Voor dit prototype zijn 6 frequenties gekoppeld aan 6 kleuren. De gebruiker begint in een leeg 
canvas en heeft dan de keuze tussen de 6 kleuren en de dikte van de lijn. Tijdens het tekenen 
kun je opnieuw deze keuze blijven maken. Daarnaast zijn er 2 andere functies, namelijk het wissen 
van getekende lijnen en het hele canvas in één keer leegmaken. 



### Audio flow diagram
![alt text](https://github.com/paulwienk/CSD2/blob/master/CSD2d/DrawFeggio/doc/drawfeggio_audioflowdiagram.png?raw=true)

Bij dit voorbeeld van een audio flow diagram behandelen we 1 van de in totaal 6 oscillatoren.
De oscillator krijgt een frequentie en een waveform type mee. Deze oscillator blijt uit zichzelf
continu klinken. Vervolgens loopt deze door een effect chain, waar de verschillende effecten 
worden toegevoegd. Om ervoor te zorgen dat hij niet meer continu loopt, wordt de oscillator
gekoppeld aan een ADSR. De twee gekozen effecten voor het prototype zijn een autoFilter en 
een autoPanner, die beide een frequentie meekrijgen waarop ze werken. Vervolgens wordt dit signaal
doorgestuurd naar de master en 'klaargezet'. Dit betekent dat hij nog niet zal klinken totdat,
in dit geval, de triggerAttackRelease wordt aangeroepen. Deze krijgt een bepaalde lengte mee 
voor hoelang hij moet klinken. 


Bij het tekenen met een bepaalde kleur, klinkt de bijbehorende frequentie:
- zwart = 396 hz
- blauw = 417 hz
- rood = 528 hz
- groen = 639 hz
- geel = 741 hz
- wit = 852 hz

De duur van de oscillator (lengthADSR in de bovenstaande afbeelding) hangt af van
hoelang je deze kleur vasthoudt, dus met andere woorden de tijd tussen het indrukken van de 
muis en het loslaten daarvan. Deze tijd wordt daarbij ook beïnvloedt door de x en y coördinaten 
waar je je muis loslaat in het canvas. 

### Uitwerking toekomst
Het prototype is een goede basis en biedt veel perspectief. Zo kunnen er heel veel effecten
worden toegevoegd waarvan de parameters door verschillende tekenactiviteiten kunnen worden
aangestuurd. Ook wat betreft de lijnen is er veel mogelijk, namelijk het laten wegvagen of 
het laten bewegen van de lijnen tijdens het tekenen. Ook is er wellicht de mogelijkheid om 
tijdens het tekenen ineens een 'mirrorfunctie' te activeren, die jouw tekeningen spiegelt 
aan verschillende kanten.

### Bronvermelding

- JavaScript / P5js 
- P5js documentatie (https://p5js.org/)
- CSDOSC (https://github.com/csdhku/csdosc)
- Tone.js (https://tonejs.github.io/)
