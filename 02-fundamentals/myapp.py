import physics

print("Světlo urazí vzdálenost 384 400 km (vzdálenost měsíce od země) za: " +
      str(round(physics.casRychlostiSvetla(384400),2)) + "sekund\n")

print("\nZvuk urazí vzdálenost 384 400 km (vzdálenost měsíce od země) za: "+
      str(round(physics.casRychlostiZvuku(348400),2)) + " minut\n")

print("\nPotenciální energie objektu, který váží 10kg ve výšce 5 metrů činí:" +
      str(physics.potencialniEnergie(10, 5)) + " Newtonů\n")

print("\nHmotnost člověka, který na zemi váží 60kg činí:" + str(physics.vahaNaMesici(60)) + " kg\n")
