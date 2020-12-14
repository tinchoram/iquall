import re
from collections import Counter

###Functions###
def create_dictionary(letras):
    """ Return dictionary from class Counter
        Param letras: string to convert
    """
    ###Paso todos a minuscula
    letras = letras.lower() 
    ###Capturo simbolos (letras/numeros) utilizando Regex
    letras = re.findall('[a-z1-9]', letras)
    ###Uso collections para crear un diccionario y contar las letras
    letras_dict = Counter(letras)
    
    return letras_dict

def create_diff_dictionarys(dictTarget, dictData):
    """ Return dictionary whit diff between: dictData - dictTarget
        Param dictTarget: Counter dict
        Param dictData: Counter dict
    """
    dict_diff = {}
    ###Recorro el dict target y comparo con dictdata
    for k in dictTarget.keys():
        dict_diff[k] = dictData[k] - dictTarget[k]
    
    return dict_diff

###MAIN###
if __name__ == "__main__":
    ###Leo carta a escribir 
    target = open("Data/target/carta.txt", "r")
    datatarget = target.read()
    target.close()

    ###Leo articulo
    article= open("Data/in/articulo.txt", "r")
    dataarticle = article.read()
    article.close()

    ###convierto a diccionarios la informacion
    dictTarget = create_dictionary(datatarget)
    dictData = create_dictionary(dataarticle)
    
    ###Comparo los diccionarios
    dict_diff = create_diff_dictionarys(dictTarget, dictData)

    ### Muestro los resultados
    print('---RESULTADO---')
    print('Para la carta ingresada: ')
    for key,value in dict_diff.items():
        if value < 0:
            print(f'XXX - Faltan {abs(value)} letras: {key} ')
        elif value==0:
            print(f'OK - Numero exacto letras: {key} ')
        else:
            print(f'OK - Sobran {value} letras: {key} ')