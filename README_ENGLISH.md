![image_Alt](https://github.com/juanvilla05/Ecercise_W3_Inventory/blob/2aac04b11fa4ccc804dab7a555324b7199a78e4e/NA_SEP._29.jpg)
# 📦 Store Inventory Management Program in Python 🐍

## 🎯 Objective

To develop a program in Python that allows for the efficient management of a store's product inventory, applying functions with parameters, lambda functions, and data structures such as lists, tuples, and dictionaries.

## ✨ Program Features

This program has been developed for a store's team to improve their digital inventory management. It allows for the following operations to be performed interactively:

* **➕ Add products:** Allows the user to enter the name, price, and quantity of new products, which are dynamically added to the inventory.
* **🔍 Consult products:** Allows searching for a product by its name and obtaining details such as its price and the available quantity. If the product is not found, the user is notified.
* **✏️ Update prices:** Allows selecting an existing product and updating its price in the inventory.
* **🗑️ Delete products:** Allows for the safe removal of products from the inventory.
* **💰 Calculate total inventory value:** Calculates and displays the total value of all products in the inventory using a lambda function to facilitate the calculation.

## 📊 Data Structure

The inventory is stored using a Python dictionary, where:

* The **🔑 key** is the **product name** (string).
* The **Value value** associated with each product name is a **tuple** containing the **💲 price** (float) and the **🔢 available quantity** (integer).

Example of the inventory structure:

```python
inventory = {
    "apple": (1.0, 50),
    "milk": (3.5, 20),
    "bread": (0.75, 100)
}
