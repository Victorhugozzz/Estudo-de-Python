import datetime 
def main():
    year = datetime.datetime.now().year
    age = year - date
    if age < 18:
       return print(f"Você tem {age} anos: VOTO PROIBIDO")
    elif age >= 18 and age < 65:
       return print(f"Você tem {age} anos: VOTO OBRIGATÓRIO")
    else:
       return print(f"Você tem {age} anos: VOTO OPICIONAL")

date = int(input("Digite o ano do seu nascimento: "))
main()
