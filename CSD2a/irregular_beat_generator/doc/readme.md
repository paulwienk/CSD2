# Paul's Beat Generator

Een beat generator op basis van een gegeven time signature. 
De gebruiker geeft een numerator en denominator als input en op basis daarvan wordt een aantal ticks gegenereerd en het aantal kicks verdeeld.

Bij bijvoorbeeld time signature 4/4 wordt deze sequence gegenereerd:

[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]

- De kick komt 100% op de 1
- De snare komt 20% op de 0
- De hihat komt 66% op de 1 of 0

De UI leidt je door het programma heen met de nodige instructies:

- type 'ts' to set a new time signature (numerator and denominator)
- type 'bpm' to set a new BPM
- type 'exit' or 'quit' to quit the generator
- type 'midi' to save the beat as a MIDI file

Bij command 'midi' wordt gevraagd aan de gebruiker of de laatst gegenereerde sequence moet worden opgeslagen.
Deze file wordt vervolgens met naam 'sequence' toegevoegd aan de src map.
