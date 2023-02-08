import netflix

filme1 = netflix.Filme("hitch", 2015, 140, "will smith")
filme1.likes()
filme1.likes()
filme1.likes()
filme1.likes()
filme2 = netflix.Filme("Interestrelar", 2014, 190,"Ana Hotway")
filme2.likes()
filme2.likes()
filme2.likes()
filme2.likes()
filme2.likes()
#  print(filme1)

serie1 = netflix.Serie("lista negra", 2022, 10, "james spader")
serie1.likes()
serie1.likes()
serie1.likes()
serie1.likes()
serie1.likes()
serie2 = netflix.Serie("designated suviver", 2022, 4, "24 horas")
serie2.likes()
serie2.likes()
serie2.likes()
serie2.likes()
serie2.likes()
#  print(serie1)

lista = [filme1, filme2, serie1, serie2]
lista_play = netflix.Playlist("FDS", lista)

for programas in lista_play:
    print(programas)

print(f"O tamanho da lista é {len(lista_play)}")
