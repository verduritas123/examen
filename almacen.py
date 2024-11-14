# Datos del almacén
almacen = {
    "Estanteria A": [
        {"nombre": "Manzana", "cantidad": 15, "precio": 2.5},
        {"nombre": "Pera", "cantidad": 10, "precio": 3.0}
    ],
    "Estanteria B": [
        {"nombre": "Banana", "cantidad": 20, "precio": 1.0},
        {"nombre": "Naranja", "cantidad": 5, "precio": 1.5}
    ],
}

# 1. Gestión de Entrada de Productos
def agregar_producto(almacen, nombre, cantidad, precio, estanteria):
    if estanteria not in almacen:
        almacen[estanteria] = []
    for producto in almacen[estanteria]:
        if producto["nombre"] == nombre:
            producto["cantidad"] += cantidad
            producto["precio"] = precio
            return f"Producto {nombre} actualizado en {estanteria}."
    almacen[estanteria].append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    return f"Producto {nombre} agregado en {estanteria}."

# 2. Gestión de Salida de Productos
def retirar_producto(almacen, nombre, cantidad):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    return f"Retirado {cantidad} de {nombre} de {estanteria}."
                else:
                    return f"No hay suficiente cantidad de {nombre} en {estanteria}."
    return f"Producto {nombre} no encontrado en el almacén."

# 3. Verificar Disponibilidad de Productos
def verificar_disponibilidad(almacen, nombre):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre:
                return f"{nombre} está en {estanteria} con cantidad: {producto['cantidad']}."
    return f"Producto {nombre} no encontrado."

# 4. Verificar el Estado del Almacén
def estado_almacen(almacen):
    estado = {}
    for estanteria, productos in almacen.items():
        total_valor = sum(producto["cantidad"] * producto["precio"] for producto in productos)
        total_cantidad = sum(producto["cantidad"] for producto in productos)
        estado[estanteria] = {"total_valor": total_valor, "total_cantidad": total_cantidad}
    return estado

# 5. Transferencia de Productos entre Estanterías
def transferir_producto(almacen, nombre, cantidad, origen, destino):
    if origen in almacen and destino in almacen:
        for producto in almacen[origen]:
            if producto["nombre"] == nombre:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    agregar_producto(almacen, nombre, cantidad, producto["precio"], destino)
                    return f"Transferido {cantidad} de {nombre} de {origen} a {destino}."
                else:
                    return f"No hay suficiente cantidad de {nombre} en {origen}."
    return f"Producto {nombre} no encontrado en {origen} o estantería destino {destino} no existe."

# 6. Optimización del Inventario
def optimizar_inventario(almacen):
    max_valor = 0
    min_productos = float('inf')
    estanteria_max_valor = ""
    estanteria_min_productos = ""
    for estanteria, productos in almacen.items():
        total_valor = sum(producto["cantidad"] * producto["precio"] for producto in productos)
        total_productos = sum(producto["cantidad"] for producto in productos)
        if total_valor > max_valor:
            max_valor = total_valor
            estanteria_max_valor = estanteria
        if total_productos < min_productos:
            min_productos = total_productos
            estanteria_min_productos = estanteria
    return f"Estantería con mayor valor acumulado: {estanteria_max_valor}, Estantería con menos productos: {estanteria_min_productos}."
