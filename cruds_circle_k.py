import flet as ft
import mysql.connector

def conectar_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="KEYRILOPEZ97$",
            database="circlek",
            auth_plugin='mysql_native_password'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar con la base de datos: {err}")
        return None

def main(page: ft.Page):
    page.title = "Circle-K"
    page.window_width = 900
    page.window_height = 700
    page.scroll = ft.ScrollMode.AUTO

    db = conectar_db()
    if db is None:
        page.add(ft.Text("Error al conectar con la base de datos", color="red"))
        return
    cursor = db.cursor()

    def mostrar_alerta(msg):
        page.snack_bar = ft.SnackBar(ft.Text(msg), bgcolor=ft.colors.RED_300)
        page.snack_bar.open = True
        page.update()

    encabezado = ft.Row([
    ft.Text("Circle-K", size=30, weight="bold", color=ft.colors.RED),
    ft.Image(src="logo_tiendita.png", width=60, height=60),
])

    # ---------------- Vista Artículos -------------------
    def vista_articulos():
        txt_id = ft.TextField(label="ID Artículo")
        txt_nom = ft.TextField(label="Nombre")
        txt_desc = ft.TextField(label="Descripción")
        txt_precio = ft.TextField(label="Precio")
        txt_stock = ft.TextField(label="Stock")
        txt_cat = ft.TextField(label="Categoría")
        txt_fecha = ft.TextField(label="Fecha caducidad (YYYY-MM-DD)")

        tabla = ft.DataTable(columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Descripción")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Stock")),
            ft.DataColumn(ft.Text("Categoría")),
            ft.DataColumn(ft.Text("Caducidad")),
        ], rows=[])

        def cargar():
            cursor.execute("SELECT * FROM articulos")
            tabla.rows.clear()
            for fila in cursor.fetchall():
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(fila[0]))),
                    ft.DataCell(ft.Text(fila[1])),
                    ft.DataCell(ft.Text(fila[2])),
                    ft.DataCell(ft.Text(str(fila[3]))),
                    ft.DataCell(ft.Text(str(fila[4]))),
                    ft.DataCell(ft.Text(fila[5])),
                    ft.DataCell(ft.Text(str(fila[6]))),
                ]))
            page.update()

        def crear(e):
            cursor.execute("INSERT INTO articulos (nombre, descripcion, precio, stock, categoria, fecha_caducidad) VALUES (%s,%s,%s,%s,%s,%s)", (
                txt_nom.value, txt_desc.value, float(txt_precio.value),
                int(txt_stock.value), txt_cat.value, txt_fecha.value))
            db.commit()
            mostrar_alerta("Artículo creado")
            cargar()

        def actualizar(e):
            cursor.execute("UPDATE articulos SET nombre=%s, descripcion=%s, precio=%s, stock=%s, categoria=%s, fecha_caducidad=%s WHERE id_articulo=%s", (
                txt_nom.value, txt_desc.value, float(txt_precio.value),
                int(txt_stock.value), txt_cat.value, txt_fecha.value, int(txt_id.value)))
            db.commit()
            mostrar_alerta("Artículo actualizado")
            cargar()

        def eliminar(e):
            cursor.execute("DELETE FROM articulos WHERE id_articulo=%s", (int(txt_id.value),))
            db.commit()
            mostrar_alerta("Artículo eliminado")
            cargar()

        cargar()

        return ft.Column([
            ft.Text("Artículos", size=22, weight="bold"),
            txt_id, txt_nom, txt_desc, txt_precio, txt_stock, txt_cat, txt_fecha,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=crear),
                ft.ElevatedButton("Actualizar", on_click=actualizar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Cargar", on_click=lambda e: cargar()),
            ]),
            tabla
        ])

    # ---------------- Vista Clientes -------------------
    def vista_clientes():
        txt_id = ft.TextField(label="ID Cliente")
        txt_nom = ft.TextField(label="Nombre")
        txt_tel = ft.TextField(label="Teléfono")
        txt_correo = ft.TextField(label="Correo")
        txt_dir = ft.TextField(label="Dirección")

        tabla = ft.DataTable(columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Correo")),
            ft.DataColumn(ft.Text("Dirección")),
            ft.DataColumn(ft.Text("Registro")),
        ], rows=[])

        def cargar():
            cursor.execute("SELECT * FROM clientes")
            tabla.rows.clear()
            for fila in cursor.fetchall():
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(fila[0]))),
                    ft.DataCell(ft.Text(fila[1])),
                    ft.DataCell(ft.Text(fila[2])),
                    ft.DataCell(ft.Text(fila[3])),
                    ft.DataCell(ft.Text(fila[4])),
                    ft.DataCell(ft.Text(str(fila[5]))),
                ]))
            page.update()

        def crear(e):
            cursor.execute("INSERT INTO clientes (nombre, telefono, correo, direccion) VALUES (%s, %s, %s, %s)", (
                txt_nom.value, txt_tel.value, txt_correo.value, txt_dir.value))
            db.commit()
            mostrar_alerta("Cliente creado")
            cargar()

        def actualizar(e):
            cursor.execute("UPDATE clientes SET nombre=%s, telefono=%s, correo=%s, direccion=%s WHERE id_cliente=%s", (
                txt_nom.value, txt_tel.value, txt_correo.value, txt_dir.value, int(txt_id.value)))
            db.commit()
            mostrar_alerta("Cliente actualizado")
            cargar()

        def eliminar(e):
            cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (int(txt_id.value),))
            db.commit()
            mostrar_alerta("Cliente eliminado")
            cargar()

        cargar()

        return ft.Column([
            ft.Text("Clientes", size=22, weight="bold"),
            txt_id, txt_nom, txt_tel, txt_correo, txt_dir,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=crear),
                ft.ElevatedButton("Actualizar", on_click=actualizar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Cargar", on_click=lambda e: cargar()),
            ]),
            tabla
        ])

    # ---------------- Vista Empleados -------------------
    def vista_empleados():
        txt_id = ft.TextField(label="ID Empleado")
        txt_nom = ft.TextField(label="Nombre")
        txt_puesto = ft.TextField(label="Puesto")
        txt_salario = ft.TextField(label="Salario")
        txt_fecha = ft.TextField(label="Fecha Contratación (YYYY-MM-DD)")
        txt_turno = ft.Dropdown(label="Turno", options=[
            ft.dropdown.Option("Matutino"),
            ft.dropdown.Option("Vespertino"),
            ft.dropdown.Option("Nocturno"),
        ])

        tabla = ft.DataTable(columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Puesto")),
            ft.DataColumn(ft.Text("Salario")),
            ft.DataColumn(ft.Text("Contratación")),
            ft.DataColumn(ft.Text("Turno")),
        ], rows=[])

        def cargar():
            cursor.execute("SELECT * FROM empleados")
            tabla.rows.clear()
            for fila in cursor.fetchall():
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(fila[0]))),
                    ft.DataCell(ft.Text(fila[1])),
                    ft.DataCell(ft.Text(fila[2])),
                    ft.DataCell(ft.Text(str(fila[3]))),
                    ft.DataCell(ft.Text(str(fila[4]))),
                    ft.DataCell(ft.Text(fila[5])),
                ]))
            page.update()

        def crear(e):
            cursor.execute("INSERT INTO empleados (nombre, puesto, salario, fecha_contratacion, turno) VALUES (%s, %s, %s, %s, %s)", (
                txt_nom.value, txt_puesto.value, float(txt_salario.value),
                txt_fecha.value, txt_turno.value))
            db.commit()
            mostrar_alerta("Empleado creado")
            cargar()

        def actualizar(e):
            cursor.execute("UPDATE empleados SET nombre=%s, puesto=%s, salario=%s, fecha_contratacion=%s, turno=%s WHERE id_empleado=%s", (
                txt_nom.value, txt_puesto.value, float(txt_salario.value),
                txt_fecha.value, txt_turno.value, int(txt_id.value)))
            db.commit()
            mostrar_alerta("Empleado actualizado")
            cargar()

        def eliminar(e):
            cursor.execute("DELETE FROM empleados WHERE id_empleado=%s", (int(txt_id.value),))
            db.commit()
            mostrar_alerta("Empleado eliminado")
            cargar()

        cargar()

        return ft.Column([
            ft.Text("Empleados", size=22, weight="bold"),
            txt_id, txt_nom, txt_puesto, txt_salario, txt_fecha, txt_turno,
            ft.Row([
                ft.ElevatedButton("Crear", on_click=crear),
                ft.ElevatedButton("Actualizar", on_click=actualizar),
                ft.ElevatedButton("Eliminar", on_click=eliminar),
                ft.ElevatedButton("Cargar", on_click=lambda e: cargar()),
            ]),
            tabla
        ])

    # ---------------- Tabs -------------------
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Artículos", icon=ft.icons.SHOPPING_CART, content=vista_articulos()),
            ft.Tab(text="Clientes", icon=ft.icons.PERSON, content=vista_clientes()),
            ft.Tab(text="Empleados", icon=ft.icons.BUSINESS_CENTER, content=vista_empleados()),
        ]
    )

    page.add(encabezado, ft.Divider(), tabs)

ft.app(target=main)
