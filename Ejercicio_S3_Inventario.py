# Aquí creamos un diccionario llamado 'inventario'. Imagina que es como una lista grandota
# donde vamos a guardar todos nuestros productos. Por ahora está vacía.
inventario = {}

# ===== Vamos a crear una función para agregar un nuevo producto al inventario =====
def add_product (inventario):
    # Este 'while True' crea un ciclo que se va a repetir hasta que le digamos que pare.
    while True:
        # Le preguntamos al usuario el nombre del producto que quiere agregar.
        # '.strip()' quita espacios en blanco al principio y al final, y '.lower()' convierte todo a minúsculas
        # para que no haya problemas si escribe "Manzana" o "manzana".
        nombre = input('Ingrese el nombre del producto que desea agragar al inventario:').strip().lower()
        # Aquí revisamos si el nombre solo tiene letras o espacios.
        valido = all(caracter.isalpha() or caracter == ' ' for caracter in nombre)
        print(f'{valido} primero') # Esto es para ver si 'valido' es True o False (verdadero o falso)
        if valido and nombre != '': # Si el nombre es válido (solo letras o espacios) y no está vacío...
            print(f'{valido} segundo') # Otra vez mostramos si es True o False
            break # ...salimos de este ciclo 'while' porque el nombre está bien.
        else:
            print('El nombre del producto debe contener solo letras y espacios.')

    # Intentamos hacer lo siguiente, pero si hay un error lo manejamos después.
    try:
        if nombre in inventario: # Si el nombre del producto ya existe en nuestro inventario...
            print(f'El producto {nombre} ya existe en el inventario, escoge la opción 3 si deseas actualizarlo.')
        else: # Si el producto no existe todavía...
            precio = float(input('Ingrese el precio del producto:')) # Preguntamos el precio (puede tener decimales).
            cantidad = int (input('Ingrese la cantidad del producto que deseas agregar:')) # Preguntamos cuántos vamos a agregar (número entero).
            # Guardamos la información del producto en el inventario. El nombre es la llave,
            # y el valor es otro diccionario con el 'precio' y la 'cantidad'.
            inventario[nombre]={'precio': precio, 'cantidad':cantidad}
            print(f'El producto {nombre} fue agregado exitosamente.')
    # Si el usuario ingresa algo que no es un número para el precio o la cantidad...
    except ValueError:
        print('¡Ups! Ingresaste algo inválido. Por favor, escribe un número para el precio y la cantidad.')

    # Preguntamos si quiere agregar otro producto.
    while True:
        seguir = input ('¿Deseas agregar otro producto? (Si/No):') .strip() .lower()

        if seguir == 'si':
            break # Si dice que sí, salimos de este ciclo para que pregunte el nombre del siguiente producto.
        elif seguir == 'no':
            print('Volviendo al menú principal.')
            return # Si dice que no, volvemos al menú principal.
        else:
            print('Respuesta incorrecta. Por favor, escribe "Si" o "No".')

# ===== Función para buscar un producto en el inventario =====
def consultar_producto (invenrario):
    nombre_product = input('Ingrese el nombre del producto que quieres buscar: ') .strip() .lower()
    if nombre_product in invenrario: # Si el nombre que ingresó el usuario está en nuestro inventario...
        datos_producto = invenrario [nombre_product] # Sacamos toda la información de ese producto.
        precio = datos_producto ['precio'] # Obtenemos el precio.
        cantidad = datos_producto ['cantidad'] # Obtenemos la cantidad.
        print (f'El producto {nombre_product} ya se encuentra en el inventario.')
        print (f'Precio: {precio}')
        print (f'Cantidad disponible: {cantidad}')
    else: # Si el nombre del producto no está en el inventario...
        print (f'El producto {nombre_product} no se encuentra en el inventario.')

# ===== Función para cambiar el precio de un producto =====
def actualizar_precio (inventario):
    nombre_product = input('Ingresa el nombre del producto al que quieres cambiar el precio: ')
    if nombre_product in inventario: # Si el producto existe en el inventario...
       try:
           nuevo_precio_produc = input ('Ingresa el nuevo precio del producto: ')
           nuevo_precio = float (nuevo_precio_produc) # Convertimos lo que escribió el usuario a un número con decimales.
           if nuevo_precio < 0 :
               print ('Por favor, ingresa un precio que sea mayor o igual a cero.')
               return # Volvemos al menú si el precio es negativo.
           inventario[nombre_product]['precio'] = nuevo_precio # Actualizamos el precio en el inventario.
           print(f'{nombre_product} actualizado con éxito.')
       except ValueError: # Si el usuario no escribe un número válido...
           print("¡Ups! Ingresaste algo inválido. Por favor, escribe un número para el precio.")
    else: # Si el producto no existe...
        print(f'El producto {nombre_product} no existe en el inventario.')

# ===== Función para quitar un producto del inventario =====
def eliminar_producto (inventario):
    nombre_product = input('Ingresa el nombre del producto que quieres eliminar: ')
    if nombre_product in inventario: # Si el producto está en el inventario...
        del inventario[nombre_product] # Lo borramos del diccionario.
        print(f'{nombre_product} eliminado con éxito.')
    else: # Si no está...
        print(f'El producto {nombre_product} no existe en el inventario.')

# ===== Función para calcular cuánto valen todos los productos juntos en el inventario =====
def valor_total_inventario (inventario):
    # Creamos una función pequeña (lambda) que toma la información de un producto
    # y multiplica su precio por la cantidad.
    calcular_valor = lambda producto:producto['precio'] * producto['cantidad']
    valor_total = 0 # Empezamos con un valor total de cero.
    # Recorremos todos los productos que están en los valores de nuestro diccionario 'inventario'.
    for producto in inventario.values():
        valor_total += calcular_valor(producto) # Sumamos el valor de cada producto al total.
    # Mostramos el valor total con dos decimales para que se vea como dinero.
    print(f'El valor total del inventario es: ${valor_total:.2f}')

# ===== Función para mostrar el menú de opciones al usuario =====
def mostrar_menu_y_obtener_opcion():
    print("\n===== Menú del Inventario =====")
    print("1. Añadir un producto")
    print("2. Consultar un producto")
    print("3. Actualizar precio de un producto")
    print("4. Eliminar un producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")
    return input("Selecciona una opción (1-6): ") # Le pedimos al usuario que elija una opción.

# ===== Aquí empieza la parte principal del programa =====
def main():
    while True: # Este ciclo se repite hasta que el usuario decida salir.
        opcion = mostrar_menu_y_obtener_opcion() # Mostramos el menú y guardamos la opción que eligió el usuario.

        if opcion == "1": # Si eligió la opción 1...
            add_product(inventario) # ...llamamos a la función para agregar un producto.
        elif opcion == "2": # Si eligió la opción 2...
            consultar_producto(inventario) # ...llamamos a la función para consultar un producto.
        elif opcion == "3": # Si eligió la opción 3...
            actualizar_precio(inventario) # ...llamamos a la función para actualizar el precio.
        elif opcion == "4": # Si eligió la opción 4...
            eliminar_producto(inventario) # ...llamamos a la función para eliminar un producto.
        elif opcion == "5": # Si eligió la opción 5...
            valor_total_inventario(inventario) # ...calculamos el valor total del inventario.
        elif opcion == "6": # Si eligió la opción 6...
            print("¡Hasta luego!")
            break # ...salimos del ciclo y el programa termina.
        else: # Si eligió cualquier otra cosa...
            print("Opción inválida. Por favor, selecciona una opción del menú (1-6).")

# Esta línea hace que la función 'main()' se ejecute cuando corremos el programa.
main ()
