### Ontwerp

Een algemene pitch trainer die jou op alle vlakken kan helpen met het trainen van je pitch. Voorbeelden van oefeningen:

- pitch trainer met random pitches die je een bepaalde tijd moet vasthouden
- pitch trainer game met reactietijden (probeer zo snel mogelijk een bepaalde pitch te halen)
- pitch trainer game waarbij je zo lang mogelijk een bepaalde pitch moet vasthouden
- instrument tuner

Al deze oefeningen komen samen in één app waar je kunt kiezen tussen deze oefeningen. Dit alles komt met de nodige visuele en auditieve feedback om de training zo makkelijk mogelijk te maken.
Bij visuele feedback gaat het voornamelijk om feedback die ondersteuning biedt aan jouw training. Bijvoorbeeld een progress bar, noten en bijbehorende octaven die je moet halen, je huidige pitch als een horizontale lijn door het scherm, de mogelijkheid om met buttons bepaalde aspecten te veranderen als de huidige noot, de goal range en het octaaf etc..

### Mapping

- pitch wordt omgezet naar een horizontale lijn die op de y-as beweegt
- pitch verandert van kleur als deze binnen de goal range zit
- pitch wordt omgezet naar een zichtbaar getal
- pitch wordt omgezet naar de ‘pitch history’, waar je kunt zien wat jouw pitch was vóór je huidige pitch in de vorm van een vloeiende lijn

De eerste mapping (pitch wordt omgezet naar een horizontale lijn die op de y-as beweegt) is mijn MVP. Dit is van belang zodat je ook je relevante pitch kan trainen. Zonder deze lijn zou het erg lastig zijn om te weten welke pitch je zingt. In mijn concept is ook de mogelijkheid om de lijn met een button te laten verdwijnen, zodat je deze uitdaging aan kunt gaan om zonder huidige pitch lijn de goal note te halen.
Ook de huidige pitch naar een zichtbaar getal is om deze reden van belang om uit te werken, zodat je op basis daarvan ook kunt oefenen (er van uitgaande dat er ook mensen zijn die pitch trainen op basis van frequentie in hertz ipv noten).

De overige twee mapping mogelijkheden zijn niet van essentieel belang voor de werking van de app. Ze zouden wel iets meer duidelijkheid geven aan het verloop van de oefening, maar zonder zou het weinig verschil moeten uitmaken.

### Reflectie PoC

Ik ben erg tevreden over mijn PoC en het algehele proces. Alles wat er in mijn MoSCoW zat heb ik erin kunnen verwerken, en één van de vooraf bedachte oefeningen heb ik goed uit kunnen werken met alle nodige functionaliteiten en visuals. De implementatie van de pitch detectie was makkelijk te doen en ik ben niet veel andere obstakels tegengekomen tijdens het programmeren. Ik denk dat ik er wel nog meer uit heb kunnen halen als ik er meer tijd in had gestoken.

##### Pluspunten:

- duidelijke interface en visuals
- meerdere buttons voor bepaalde doeleinden, waardoor de oefening goed kan worden uitgevoerd
- voice-over voor blinden en slechtzienden van de huidige noot

##### Minpunten:

- lelijke buttons
- pitch detectie niet altijd even nauwkeurig
- geen limiet op de octaven (kan ver in de min of ver in de plus als je wil)

##### Interessant:

- de pitch history werkt goed en brengt toch iets meer leven in de oefening
- ik heb het coördinatensysteem aangepast in JavaScript zodat coördinaten nu van 0 (onderaan) naar -640 (bovenaan) lopen. Hierdoor moest ik alle frequenties ook negatief maken, wat achteraf gezien misschien anders had gekund
