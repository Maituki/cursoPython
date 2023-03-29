def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    if a==0 or b==0:
        return 0
    else:
        return a*b

def dividir(a,b):
    if b>0:
        return a/b
    else:
        print("No se puede dividir un nº entre 0")

def msg():
    print("Me he despertado")

def msg_medio():
    print("LLevo unos segundos despierta")

def msg_final():
    print("Tiempo variado")

if __name__=='__main__':
    print(sumar(2,5))