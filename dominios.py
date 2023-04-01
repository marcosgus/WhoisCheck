import whois
import datetime

# Leer el archivo con los dominios a verificar
with open('whois.txt', 'r') as f:
    dominios = f.read().splitlines()

# Iterar por cada dominio
for dominio in dominios:
    # Obtener información del dominio con whois
    info = whois.whois(dominio)

    # Verificar si el dominio está expirado
    if isinstance(info.expiration_date, list):
        expiracion = info.expiration_date[0]
    else:
        expiracion = info.expiration_date
    if expiracion is None:
        print(f"El dominio {dominio} no tiene información de expiración.")
    elif expiracion < datetime.datetime.now():
        print(f"El dominio {dominio} ha expirado.")
    else:
        print(f"El dominio {dominio} expira el {expiracion}.")
