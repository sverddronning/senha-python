
#gerador de senhas seguras

import random
import string


#comprimento de senha

comprimento_senha = int(input("Quantos caracteres você deseja que sua senha possua?  "))


#tipos de caracteres

letra_maiuscula = input("Sua senha deve conter letras maiúsculas? (S/N)")
letra_minuscula = input("Sua senha deve conter letras minúsculas? (S/N)")
numeros = input("Sua senha deve conter números? (S/N)")
carac_especiais = input("Sua senha deve conter caracteres especiais? (S/N)")


# Validação da senha segura

if letra_maiuscula != 's' or letra_minuscula != 's' or numeros != 's' or carac_especiais != 's':

    print("Sua senha não é segura. Recomendamos optar por uma senha com todas as opções acima sendo 'S'.")
else:
    # Gere a senha
    caracteres_permitidos = ''
    if letra_maiuscula == 's':
        caracteres_permitidos += string.ascii_uppercase
    if letra_minuscula == 's':
        caracteres_permitidos += string.ascii_lowercase
    if numeros == 's':
        caracteres_permitidos += string.digits
    if carac_especiais == 's':
        caracteres_permitidos += string.punctuation

    if len(caracteres_permitidos) == 0:
        print("Não há caracteres permitidos para criar a senha.")
    else:
        senha_gerada = ''.join(random.choice(caracteres_permitidos) for _ in range(comprimento_senha))
        print("Sua senha gerada é: " + senha_gerada)
