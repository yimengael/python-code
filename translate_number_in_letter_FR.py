###
## This function lets you count the number
## of digits in a number en base 10
###
def count_nb_digits(number):
    nb = 0
    res = number
    while int(res/10)!=0:
        res = int(res/10)
        nb = nb+1
    nb = nb+1
    return nb

###
## this function give your the translation in letter
## of a number that have one digit in french
###
def one_digit_to_letter(number):
    nombre = int(number)
    return {
        0:'zero',
        1:'un',
        2:'deux',
        3:'trois',
        4:'quatre',
        5:'cinq',
        6:'six',
        7:'sept',
        8:'huit',
        9:'neuf'
    }[nombre]


###
## function that returns Multiple of ten in letter
###
def multiple_ten_to_letter(number):
    nombre = int(number)
    return {
        10:'dix',
        20:'vingt',
        30:'trente',
        40:'quarante',
        50:'cinquante',
        60:'soixante',
        70:'soixante-dix',
        80:'quatre-vingt',
        90:'quatre-vingt-dix'
    }[nombre]

###
## this function give your the translation in letter
## of a number that have two digits in french
###
def two_digits_to_letter(number):
    nombre = int(number)
    dizaine = int(nombre/10)
    reste = int(nombre%10)
    strNumberTranslate = None

    if dizaine == 1:
        if reste == 0:
            strNumberTranslate = multiple_ten_to_letter(10)
        elif reste == 1:
            strNumberTranslate = 'onze'
        elif reste == 2:
            strNumberTranslate = 'douze'
        elif reste == 3:
            strNumberTranslate = 'treize'
        elif reste == 4:
            strNumberTranslate = 'quatorze'
        elif reste == 5:
            strNumberTranslate = 'quinze'
        elif reste == 6:
            strNumberTranslate = 'seize'
        elif reste == 7:
            strNumberTranslate = multiple_ten_to_letter(dizaine*10) + "-" + one_digit_to_letter(reste)
        elif reste == 8:
            strNumberTranslate = multiple_ten_to_letter(dizaine*10) + "-" + one_digit_to_letter(reste)
        elif reste == 9:
            strNumberTranslate = multiple_ten_to_letter(dizaine*10) + "-" + one_digit_to_letter(reste)
    elif dizaine == 2:
        pass


    return strNumberTranslate


nombre = 17;
#nbConverted = convert_number_to_letter(nombre)
print(two_digits_to_letter(nombre));
