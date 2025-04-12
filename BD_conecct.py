import flet as ft

def main(page: ft.Page):
    page.title = "CIRCLE-K"
    page.window_width = 800
    page.window_height = 600

    titulo = ft.Text("CATALOGO DE ARTICULOS", size=25, weight="bold")
    
    # Campos para artículos
    titulo_articulos = ft.Text("Artículos", size=20, weight="bold")
    txt_id_articulo = ft.TextField(label="ID Artículo", filled=True, fill_color=ft.colors.AMBER_100)
    txt_nombre_articulo = ft.TextField(label="Nombre", filled=True, fill_color=ft.colors.AMBER_100)
    txt_descripcion_articulo = ft.TextField(label="Descripción", filled=True, fill_color=ft.colors.AMBER_100)
    txt_precio_articulo = ft.TextField(label="Precio", filled=True, fill_color=ft.colors.AMBER_100)
    txt_categoria_articulo = ft.TextField(label="Categoría", filled=True, fill_color=ft.colors.AMBER_100)

    # Campos para clientes
    titulo_clientes = ft.Text("Clientes", size=20, weight="bold")
    txt_id_cliente = ft.TextField(label="ID Cliente", filled=True, fill_color=ft.colors.LIGHT_BLUE_100)
    txt_nombre_cliente = ft.TextField(label="Nombre", filled=True, fill_color=ft.colors.LIGHT_BLUE_100)
    txt_telefono_cliente = ft.TextField(label="Teléfono", filled=True, fill_color=ft.colors.LIGHT_BLUE_100)
    txt_correo_cliente = ft.TextField(label="Correo", filled=True, fill_color=ft.colors.LIGHT_BLUE_100)
    txt_direccion_cliente = ft.TextField(label="Dirección", filled=True, fill_color=ft.colors.LIGHT_BLUE_100)

    # Campos para empleados
    titulo_empleados = ft.Text("Empleados", size=20, weight="bold")
    txt_id_empleado = ft.TextField(label="ID Empleado", filled=True, fill_color=ft.colors.PURPLE_100)
    txt_nombre_empleado = ft.TextField(label="Nombre", filled=True, fill_color=ft.colors.PURPLE_100)
    txt_puesto_empleado = ft.TextField(label="Puesto", filled=True, fill_color=ft.colors.PURPLE_100)
    txt_salario_empleado = ft.TextField(label="Salario", filled=True, fill_color=ft.colors.PURPLE_100)
    txt_turno_empleado = ft.TextField(label="Turno", filled=True, fill_color=ft.colors.PURPLE_100)

    # Tabla para mostrar datos
    tabla_datos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Detalle")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("Ejemplo")),
                    ft.DataCell(ft.Text("Datos de muestra")),
                ]
            ),
        ]
    )

    # Botones CRUD
    def on_crear_click(e):
        # Aquí iría la lógica para crear registros
        print("Botón Crear presionado")
        
    def on_leer_click(e):
        # Aquí iría la lógica para leer registros
        print("Botón Leer presionado")
        
    def on_actualizar_click(e):
        # Aquí iría la lógica para actualizar registros
        print("Botón Actualizar presionado")
        
    def on_eliminar_click(e):
        # Aquí iría la lógica para eliminar registros
        print("Botón Eliminar presionado")

    botones_crud = ft.Row([
        ft.ElevatedButton("Crear", on_click=on_crear_click, bgcolor=ft.colors.GREEN),
        ft.ElevatedButton("Leer", on_click=on_leer_click, bgcolor=ft.colors.BLUE),
        ft.ElevatedButton("Actualizar", on_click=on_actualizar_click, bgcolor=ft.colors.ORANGE),
        ft.ElevatedButton("Eliminar", on_click=on_eliminar_click, bgcolor=ft.colors.RED),
    ])

    # Pestañas para las diferentes entidades
    pestanas = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Artículos",
                icon=ft.icons.SHOPPING_CART,
                content=ft.Container(
                    content=ft.Column([
                        titulo_articulos,
                        txt_id_articulo,
                        txt_nombre_articulo,
                        txt_descripcion_articulo,
                        txt_precio_articulo,
                        txt_categoria_articulo,
                        botones_crud,
                        ft.Container(height=20),  # Espacio
                        tabla_datos,
                    ], 
                    scroll=ft.ScrollMode.AUTO,
                    spacing=15),
                    padding=20,
                )
            ),
            ft.Tab(
                text="Clientes",
                icon=ft.icons.PERSON,
                content=ft.Container(
                    content=ft.Column([
                        titulo_clientes,
                        txt_id_cliente,
                        txt_nombre_cliente,
                        txt_telefono_cliente,
                        txt_correo_cliente,
                        txt_direccion_cliente,
                        botones_crud,
                        ft.Container(height=20),  # Espacio
                        tabla_datos,
                    ], 
                    scroll=ft.ScrollMode.AUTO,
                    spacing=15),
                    padding=20,
                )
            ),
            ft.Tab(
                text="Empleados",
                icon=ft.icons.BADGE,
                content=ft.Container(
                    content=ft.Column([
                        titulo_empleados,
                        txt_id_empleado,
                        txt_nombre_empleado,
                        txt_puesto_empleado,
                        txt_salario_empleado,
                        txt_turno_empleado,
                        botones_crud,
                        ft.Container(height=20),  # Espacio
                        tabla_datos,
                    ], 
                    scroll=ft.ScrollMode.AUTO,
                    spacing=15),
                    padding=20,
                )
            ),
        ],
        expand=1,
    )

    barra_superior = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.STORE, color=ft.colors.RED, size=30),
            ft.Text("CIRCLE-K", size=22, weight="bold", color=ft.colors.RED),
        ]),
        padding=10,
        bgcolor=ft.colors.BLACK12,
        border_radius=10,
    )
    
    page.add(
        ft.Column([
            barra_superior,
            titulo,
            pestanas,
        ])
    )

ft.app(target=main)