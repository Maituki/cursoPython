from common.calculo import *
#si solicitas varias veces q introduzca los numeros
def input_numeros():
    a=float (input("Introduce primer numerando"))
    b=float (input("Introduce segundo numerando"))
    return a,b

#print(dir())


if __name__=='__main__':
    #print("module calculo.py")
    #print(sumar(2,5))
    operacionOK=True
    opcion= input ("Que operación quieres realizar? Sumar(+), Restar(-), Multiplicar(*),Dividir(/)")
    if opcion not in ["+","-","*","/"]:
         print("La operación elegida no existe. Adios!!")
    else:      
        n1,n2= input_numeros()
        if opcion=="+":
            x=sumar(n1,n2)
        elif opcion=="-":
            x=restar(n1,n2)
        elif opcion=="*":
            x=multiplicar(n1,n2)
        else:
            x=dividir(n1,n2)
        print(f" resultado formateado 2 decimales {x:.2f}")
        
        
    
    
    
    