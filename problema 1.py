class NavegadorWeb:
    def __init__(self):
        self.historial = [] # arreglo para lamecenar las paginas o guardar las paginas visitadas 
        self.posicion_actual = -1 # el -1 indica que se encuantra la inicio es decir no se ha visitao ninguna pagina 

    def visitar_pagina(self, pagina):
        # Al visitar una nueva página se borra el historial futuro
        self.historial = self.historial[:self.posicion_actual + 1]
        self.historial.append(pagina)
        self.posicion_actual += 1
        print(f"Visitando: {pagina}")
    
    #si no se ha visitado ninguna pagina los metodos de avanzar y retrocedre no se lleva a cabo
    #debe haber más de dos paginas para qque los metodos pueden ejecutarce.
    

    def retrocedre(self):
        if self.posicion_actual > 0:
            self.posicion_actual -= 1 # no puede estar al inicio del historial, el puntero que señala la posicion se mueve una posicio atras.
            print(f"Retrocediendo a: {self.historial[self.posicion_actual]}")
        else:
            print("No puedes retroceder más.")# señal de indica que ya no se puede retroceder mas es decir que llego al inicio del historia 

    def avanzar(self):
        if self.posicion_actual < len(self.historial) - 1:
            self.posicion_actual += 1 #  el puntero que señala la posicion se mueve una posicio adelante y se vuelve la pagina actual .
            print(f"Avanzando a: {self.historial[self.posicion_actual]}")
        else:
            print("No puedes avanzar más.")# señal de indica que ya no se puede avanzar mas es decir que es la ultima pagina visitada. 

    def mostrar_pagina_actual(self): #muestra si ya haz visitado alguna pagina o no 
        if self.posicion_actual != -1:
            print(f"Página actual: {self.historial[self.posicion_actual]}")
        else:
            print("No hay páginas en el historial.")

# Prueba 
navegador = NavegadorWeb() #llama a la clase 
navegador.visitar_pagina("google.com")
navegador.visitar_pagina("youtube.com")
navegador.visitar_pagina("chat.openai.com")

navegador.retroceder()
navegador.retroceder()
navegador.retroceder()  #No puede retroceder más

navegador.avanzar()
navegador.avanzar()
navegador.avanzar()  #No puede avanzar más

navegador.visitar_pagina("github.com")  #Se borra el historial futuro

navegador.mostrar_pagina_actual()
