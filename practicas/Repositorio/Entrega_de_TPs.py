import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
#print(re.search(patron , texto))
#print(re.match(patron , texto))
#print(re.search(patron, texto).group())
print(re.findall(patron, texto))
print(texto[22:26])


p = "ipsum(.*?)sit"
print(re.findall(p, texto))

print(re.sub(p, "hola", texto))

 
patrones = r"\bipsum\b"
print(re.sub(patrones, "lapsus", texto))
re.sub(patrones, "lapsus", texto)