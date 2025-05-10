![image_Alt][https://github.com/juanvilla05/Ecercise_W3_Inventory/blob/2aac04b11fa4ccc804dab7a555324b7199a78e4e/NA_SEP._29.jpg]
# 📦 Programa de Gestión de Inventario de Tienda en Python 🐍

## 🎯 Objetivo

Desarrollar un programa en Python que permita gestionar de manera eficiente el inventario de productos de una tienda, aplicando funciones con parámetros, funciones lambda, y estructuras de datos como listas, tuplas y diccionarios.

## ✨ Características del Programa

Este programa ha sido desarrollado para el equipo de una tienda con el fin de mejorar la gestión de su inventario digital. Permite realizar las siguientes operaciones de manera interactiva:

* **➕ Añadir productos:** Permite al usuario ingresar el nombre, precio y cantidad de nuevos productos, los cuales se añaden dinámicamente al inventario.
* **🔍 Consultar productos:** Permite buscar un producto por su nombre y obtener detalles como su precio y la cantidad disponible. Si el producto no se encuentra, se notifica al usuario.
* **✏️ Actualizar precios:** Permite seleccionar un producto existente y actualizar su precio en el inventario.
* **🗑️ Eliminar productos:** Permite eliminar productos del inventario de forma segura.
* **💰 Calcular el valor total del inventario:** Calcula y muestra el valor total de todos los productos en el inventario utilizando una función lambda para facilitar el cálculo.

## 📊 Estructura de Datos

El inventario se almacena utilizando un diccionario de Python, donde:

* La **🔑 clave** es el **nombre del producto** (string).
* El **Value valor** asociado a cada nombre de producto es una **tuple tupla** que contiene el **💲 precio** (float) y la **🔢 cantidad disponible** (integer).

Ejemplo de la estructura del inventario:

```python
inventario = {
    "manzana": (1.0, 50),
    "leche": (3.5, 20),
    "pan": (0.75, 100)
}
