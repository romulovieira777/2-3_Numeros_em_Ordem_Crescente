primeiro = int(input())
segundo = int(input())
terceiro = int(input())

if (segundo > terceiro):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if (primeiro > segundo):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if (segundo > terceiro):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro)
print(segundo)
print(terceiro)  
