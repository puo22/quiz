from collections import deque

class EntidadPublica:# hace referencia a una entidad publica.
    def __init__(self):
        self.cola = deque()#se crea una cola vacia 

    def agregar_cliente(self, nombre): #llama a la cola y agrega el nombre del cliente al final de la cola 
        print(f"{nombre} ha llegado.")#muestra el nombre del cliente que llego
        self.cola.append(nombre)

    def atender_cliente(self):
    #Atiende al primer cliente en la cola, una vez realizada esa accion se elimina la cabeza de la cola 
    #es decir sale el cliente de la cola y sigue el siguein en orden de llegada 
        if self.cola:
            cliente = self.cola.popleft() #elimna la caneza de la cola
            print(f"Atendiendo a {cliente}")# si en la cola sigue teniendo clientes continua.
        else:
            print("No hay clientes en espera.")# si ya no ahi clientes muestra el mensaje 

    def mostrar_cola(self):
        print("En espera:", list(self.cola))#muestra la lista de espera de los clientes que aun estan.

# Prueba
entidad = EntidadPublica()

#se agrega los clientes a la cola (lista de espera)
entidad.agregar_cliente("Carlos")
entidad.agregar_cliente("María")
entidad.agregar_cliente("Luis")
entidad.mostrar_cola()

#se atiende al cliente que esta en la cabeza de la cola asi sucesivamente 
entidad.atender_cliente()
entidad.atender_cliente()
entidad.mostrar_cola()

#se agrega un nuevo cliente a la cola y se muestra la lista de espera con los cambios 
entidad.agregar_cliente("Ana")
entidad.mostrar_cola()

entidad.atender_cliente()
entidad.atender_cliente()  # No hay más clientes, se detiene el proceso 