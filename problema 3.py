class TrieNode:
    def __init__(self):
        self.hijos = {}  # Diccionario de letras hijas
        self.es_fin_de_palabra = False  # Marca si es final de una palabra

class Trie:
    def __init__(self):
        self.raiz = TrieNode()  # Raíz del Trie

    def insertar(self, palabra):
        nodo = self.raiz
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = TrieNode()
            nodo = nodo.hijos[letra]
        nodo.es_fin_de_palabra = True

    # Buscar todas las palabras posibles a partir de las letras disponibles
    def buscar_palabras(self, letras):
        resultado = set()
        self._buscar_palabras_rec(self.raiz, "", letras, resultado)
        return resultado

    # Función recursiva auxiliar
    def _buscar_palabras_rec(self, nodo, palabra_actual, letras_disponibles, resultado):
        if nodo.es_fin_de_palabra:
            resultado.add(palabra_actual)

        for i, letra in enumerate(letras_disponibles):
            if letra in nodo.hijos:
                # Usamos la letra y seguimos buscando
                self._buscar_palabras_rec(
                    nodo.hijos[letra],
                    palabra_actual + letra,
                    letras_disponibles[:i] + letras_disponibles[i+1:],  # Eliminamos la letra usada
                    resultado
                )

# Lista de palabras válidas (diccionario)
diccionario = ["gato","gota","toga","ato","tag","to","go","ta","a"]

letras = list("toga")  # Puedes cambiar las letras

# Crear e insertar palabras en el Trie
trie = Trie()
for palabra in diccionario:
    trie.insertar(palabra)

# Buscar palabras que se pueden formar con las letras dadas
palabras_formadas = trie.buscar_palabras(letras)

# Mostrar resultados
print("Palabras posibles formadas con las letras:", letras)
print(palabras_formadas)
