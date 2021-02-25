def verifica(texto, letra):
    return texto.count(letra)

texto = str(input("Informe um texto qualquer: ")).lower()
letra = str(input("Informe um letra qualquer: ")).lower()

print(f"A letra {letra} aparece  {verifica(texto,letra)} vezes no texto \n\n")

