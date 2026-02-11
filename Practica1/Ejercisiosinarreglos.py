Cadena = "Parangaricutimicuaro"

minusculas = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','z'


mayus = 'A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','Y','Z' 

for letras in minusculas:
    minus = Cadena.count(letras)
    if minus != 0:
        print("Esta letra tiene ", letras, minus)

for LETRAS in mayus:
    mayus2 = Cadena.count(LETRAS)
    if mayus2 != 0 :
        print("Esta letra tiene :", LETRAS, mayus2)