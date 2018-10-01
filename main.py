##########################
# Tristan Pétur Andersen #
# 28 Ágúst 2018          #
# Æfingaverkefni 2       #
##########################

import os
from os import system

def main():
    os.system('cls')
    lidur = int(input('Sláðu in númer á lið: '))
    
    if lidur == 1:
        print('-' * 20)
        lidur1()
        input()
    elif lidur == 2:
        print('-' * 20)
        lidur2()
        input()
    elif lidur == 3:
        print('-' * 20)
        lidur3()
        input()
    elif lidur == 4:
        print('-' * 20)
        lidur4()
        input()
    elif lidur == 5:
        print('-' * 20)
        lidur5()
        input()
    main()

def lidur1():
    numer1 = input('Sláðu inn tölu: ')
    numer2 = input('Sláðu inn aðra tölu: ')
    
    if numer1 > numer2:
        print('Fyrsta talan ' + str(numer1) + " er stærri en " + str(numer2))
        
    elif numer1 < numer2:
        print('Önnur talan ' + str(numer2) + " er stærri en " + str(numer1))
        
    elif numer1 == numer2:
        print('Tölurnar eru jafn stórar')
    
def lidur2():
    manadaTexti = "Númerið á munuðinum er "
    
    manudur = input('Sláðu inn mánuð (t.d: "janúar"): ')

    manudur = manudur.lower()
    
    if manudur == "janúar":
        print("\n", manadaTexti, "01")
    elif manudur == "febrúar":
        print("\n", manadaTexti, "02")
    elif manudur == "mars":
        print("\n", manadaTexti, "03")
    elif manudur == "apríl":
        print("\n", manadaTexti, "04")
    elif manudur == "maí":
        print("\n", manadaTexti, "05")
    elif manudur == "júní":
        print("\n", manadaTexti, "06")
    elif manudur == "júlí":
        print("\n", manadaTexti, "07")
    elif manudur == "ágúst":
        print("\n", manadaTexti, "08")
    elif manudur == "september":
        print("\n", manadaTexti, "09")
    elif manudur == "október":
        print("\n", manadaTexti, "10")
    elif manudur == "nóvember":
        print("\n", manadaTexti, "11")
    elif manudur == "desember":
        print("\n", manadaTexti, "12")
    else:
        print("Ég þekki ekki þennan mánuð.")
        
def lidur3():
    aldur = int(input('Sláðu inn aldurinn þinn: '))
    
    if aldur < 7:
        print('Nú, svo þú ferð að byrja í skóla')
        
    elif aldur >= 7 and aldur <= 15:
        spyrMennt = input('Ætlarðu í menntaskóla? (J/N): ')
        spyrMennt = spyrMennt.lower()
        
        if spyrMennt == "J":
            print('Gangi þér vel!')
        elif spyrMennt == "N":
            print('Oof... ok.')
            
    elif aldur >= 16 and aldur <= 105:
        print('Gangi þér vel í framtíðinni!')
        
    elif aldur > 105:
        print('Annað hvort ertu Gandalf eða þú sláðir inn vitlaust')
    
def lidur4():
    milliTala = int(input('Veldu tölu á milli 0 og 25: '))
    
    if milliTala > 0 and milliTala < 25:
        milliTala = milliTala * 1.7
    
        print(milliTala, " er nýja talan þín!")
        
    else:
        print('Rangur innsláttur')
        
def lidur5():
    villBrandara = input('Viltu heyra brandara? (J/N): ')
    villBrandara = villBrandara.lower()
    
    if villBrandara == "j":
        print('self != </> brandara')
        
    elif villBrandara == "n":
        print('Allt í lagi, kannski seinna')
main()