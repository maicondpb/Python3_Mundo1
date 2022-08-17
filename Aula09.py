#Fatiamento

frase = 'Curso em Video Python'
print(frase[9]) = V

# Cada caractece da frase é um número para o Python, nesse caso acima vai de 0 a 20.

print(frase[9:13]) = Vide
print(frase[9:21]) = Video Python
print(frase[9:21:2]) = Vdo Pto
print(frase[:5]) = Curso
print(frase[15:]) = Python
print(frase[9::3]) = VePh

# Análise

len(frase) = Comprimento da frase (21 caracteres)
frase.count('o') = 3, vai contar quantas vezes tem a letra 'o' na string
frase.count('o',0,13) = 2, vai contar até o 12 e só tem '0' 2x até o 12.
frase.find('deo') = 11, vai apontar aonde começou
frase.find('Android') = -1, significa que não existe, não foi encontrado
'Curso' in frase


# Transformação

frase.replace('Python', 'Android') = vai substituir o Python por Android, ficaria Curso em Video Android
frase.upper() = o que já for maiúscula ele mantém e o que estava em minúscula ele transforma pra maiúscula
frase.lower() = o que já for minúscula ele mantém e o que estava em maíuscula ele transforma pra minúscula
frase.capitalize() = vai jogar todos os caracteres para minúscula e só a primeira letra vai jogar pra maiúscula
frase.title() = vai jogar todos os primeiros caracteres de cada palavra para maiúsculas

frase = ('   Aprenda Python  ')
frase.strip() = vai remover todos os espaços inúteis do início e do fim da frase
frase.rstrip() = vai remover todos os espaços inúteis da direita (os últimos da frase somente)
frase.lstrip() = vai remover todos os espaços inúteis da esquerda (os primeiros da frase somente)

frase.split() = vai pegar cada espaço entre as palavras e criar uma divisão, cada palavra tem sua recontagem daí


# Junção

'-'.join(frase) = Curso-em-Video-Python


