
from random import randint
from pizza_personalizada import PizzaPersonalizada 
from pizza_personalizada import ConcretePizzaPersonalizada
from director import Director
import csv
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Pedido:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.numero_pedido = None
        self.pizzas = [] # lista de objetos PizzaPersonalizada

    def asignar_numero_pedido(self):
        '''asignar numero de pedido con el formato 3 letras y 3 numeros'''
        num_pedido = letras[randint(0,25)] + letras[randint(0,25)] + letras[randint(0,25)] + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        self.numero_pedido = num_pedido

    def agregar_pizza(self, pizza: PizzaPersonalizada):
        self.pizzas.append(pizza)

    def mostrar_resumen(self):
        print(f"Pedido para: {self.nombre}")
        print(f"Número de Pedido: {self.numero_pedido}")
        print("Pizzas en el pedido:")
        for pizza in self.pizzas:
            pizza.list_parts()
            print()



def generar_pedido():
    nombre_cliente = input("Introduce tu nombre: ")
    pedido = Pedido(nombre_cliente)
    pedido.asignar_numero_pedido()
    num_pedido = pedido.numero_pedido

    print("Bienvenido a la pizzería, " + nombre_cliente + ".")
    print("Tu número de pedido es: " + num_pedido)

    
    director = Director()
    builder = ConcretePizzaPersonalizada() #tipo de pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    
    num_pizzas = int(input("¿Cuántas pizzas quieres? "))
    for _ in range(num_pizzas):
        hacer_pizza(pedido, director, builder)
        print()

    print("Tu pedido es:")
    #leer_pizzas_por_numero_de_pedido(num_pedido)
    pizzas_solicitadas = leer_pizzas_por_numero_de_pedido(num_pedido)
    for pizza in pizzas_solicitadas:
        print(pizza)

    
def hacer_pizza(pedido, director, builder):
    '''Funcion que crea una pizza personalizada, la agrega al pedido y la guarda en un diccionario de pedidos'''
    
    director.build_pizza()
    pizza_personalizada = builder.pizza  # es un objeto PizzaPersonalizada
    lista_ingredientes = pizza_personalizada.get_parts()
    pedido.agregar_pizza(lista_ingredientes) # agregamos la pizza al pedido (en forma de lista de ingredientes)
    #pizza_personalizada.list_parts()  # imprime la lista de ingredientes
    
    # GUARDAR DATOS PIZZA
    guardar_datos_csv(pedido)

    builder.reset() #reseteamos  builder para que no se acumulen los datos


def guardar_datos_csv(pedido):
    with open('pedidos.csv', mode='a', newline='') as file:
        fieldnames = ['Número de Pedido', 'Masa', 'Salsa Base', 'Ingredientes', 'Cocción', 'Presentación', 'Maridaje', 'Extra']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        lista_pizzas=pedido.pizzas
        for pizza in pedido.pizzas:
            writer.writerow({
                'Número de Pedido': pedido.numero_pedido,
                'Masa': pizza[0],
                'Salsa Base': pizza[1],
                'Ingredientes': pizza[2],
                'Cocción': pizza[3],
                'Presentación': pizza[4],
                'Maridaje': pizza[5],
                'Extra': pizza[6]
            })

def leer_pizzas_por_numero_de_pedido(numero_pedido, nombre_archivo='pedidos.csv'):
    try:
        pizzas_solicitadas = []

        with open(nombre_archivo, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Número de Pedido'] == numero_pedido:
                    pizza = {
                        'Masa': row['Masa'],
                        'Salsa Base': row['Salsa Base'],
                        'Ingredientes': row['Ingredientes'],
                        'Cocción': row['Cocción'],
                        'Presentación': row['Presentación'],
                        'Maridaje': row['Maridaje'],
                        'Extra': row['Extra']
                    }
                    pizzas_solicitadas.append(pizza)

        return pizzas_solicitadas

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return []



def funcion_main():
    print('Bienvenido a la pizzería')
    generar_pedido()
    print('Gracias por venir a la pizzería, vuelva pronto')
     
