import flet as ft
from flet import (Colors, FontWeight, Divider, DataColumn, ResponsiveRow, FloatingActionButton,
                  Text, Row, IconButton, Icons)
from model.db_wizard import db, Funcionar

value_controllers = {
    'titulo':['Entrada', 'Saida', 'Ativos'],
    'icon':[ft.icons.ARROW_UPWARD, ft.icons.ARROW_DOWNWARD, ft.icons.PEOPLE],
    'color':[ft.Colors.BLUE, ft.Colors.RED, ft.Colors.BLUE],
    'value':[0,0,0],
}

def home(page: ft.Page, width:int, height :int):

    view = ft.View(
        route='/',
        bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLACK,),
        # bgcolor=ft.colors.BLACK,
        controls=[
            ft.Stack(
                width=width,
                height=height,
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                col={'xs':12},
                                bgcolor=ft.Colors.BLUE,
                                height=height * 0.11,

                            )
                        ]
                    ),
                    ft.Container(
                        padding=ft.padding.only(top=60, left=60, right=60),
                        content= ft.Column(
                            controls=[
                                ft.ResponsiveRow(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        vcontainer(height=height, data=i) for i in range(len(value_controllers['titulo']))
                                    ]
                                ),

                                ft.Container(
                                    bgcolor=ft.Colors.WHITE,
                                    width=width,
                                    height=height * 0.5,
                                    border_radius=10,
                                    padding=10,
                                    content=ft.ResponsiveRow(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.Container(
                                                border_radius=10
                                                ,content=ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            value="Tabela de funcionarios",
                                                            color=Colors.with_opacity(0.4, Colors.BLACK),
                                                            size=20,
                                                            weight=FontWeight.BOLD,
                                                        ),
                                                        Divider(
                                                            height=2,
                                                            thickness=2,
                                                        ),

                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            ),
        ]
    )

    return view

def vcontainer(height:int, data: int):

    container = ft.Container(
        col={'xs': 12, 'md':3}
        ,bgcolor=ft.Colors.WHITE
        ,height=height * 0.19
        ,border_radius=10
        ,padding=ft.padding.only(top=8, left=5, right=5, bottom=5)
        ,content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    value=value_controllers['titulo'][data].upper()
                    ,size=16
                    ,weight=ft.FontWeight.BOLD
                    ,color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK)
                )
                ,ft.Divider(
                    height=1
                    , color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK)
                    , thickness=1
                )
                ,ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ,spacing=20
                    ,controls=[
                        ft.Text(
                            value=f"R$ {value_controllers['value'][data]:.2f}"
                            , color=ft.Colors.with_opacity(0.4, value_controllers['color'][data])
                            , size=18
                            , weight=ft.FontWeight.BOLD
                        )
                        ,ft.Icon(
                            name=value_controllers['icon'][data]
                            , color=ft.Colors.with_opacity(0.4, value_controllers['color'][data])
                            , size=30
                            # , weight=ft.FontWeight.BOLD
                        )
                    ]
                )
            ]
        )
    )

    return container

def AlertDialog(page: ft.Page, title: str, dados:list=[]):

    value_controls = {
        'hint_text': ['Id', 'Uuid', 'Nome', 'Cargo', 'Departamento', 'Email'],
        'icon': [Icons.KEY, Icons.KEY, ft.icons.PERSON, ft.icons.WORK, ft.icons.WORK, ft.icons.EMAIL],
    }

    def close(e):
        alertdialog.open=False
        page.update()

    controls = []
    for i in range(len(value_controls['hint_text'])):
        campo = value_controls['hint_text'][i].lower()

        controls.append(
            ft.TextField(
                hint_text=value_controls['hint_text'][i]
                , prefix_icon=value_controls['icon'][i]
                , hint_style=ft.TextStyle(
                    size=13
                    , color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK)
                    , weight=ft.FontWeight.BOLD
                )
                , text_style=ft.TextStyle(
                    size=13
                    , color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK)
                    , weight=ft.FontWeight.BOLD
                ),
                visible=False if i == 1 else True,
                value=dados[campo] if campo in dados else '',
                disabled=True if i == 0 else False,
                autofocus=True,
            )
        )

    alertdialog = ft.AlertDialog(
        modal=True,
        bgcolor=Colors.WHITE,
        title=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    value=title,
                    color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
                    size=16,
                    weight=FontWeight.BOLD,
                ),
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color=ft.Colors.RED,
                    icon_size=16,
                    on_click=lambda e: close(e)
                )
            ]
        ),
        content= ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={'sm':12},
                    height=250,
                    controls=controls
                )
            ]
        ),
        actions=[
            ResponsiveRow(
                controls=[
                    FloatingActionButton(
                        text='Salvar',
                        bgcolor=Colors.BLUE,
                        height=48,
                        foreground_color=Colors.WHITE,
                    ),
                ]
            )
        ]
    )

    page.overlay.append(alertdialog)
    alertdialog.open=True
    page.update()

    return alertdialog

def SnapBar(page: ft.Page, title:str, icon: Icons):
    snapbar = ft.SnackBar(
        content=ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    size=25,
                    color=Colors.BLUE,
                ),
                ft.Text(
                    value=title,
                    size=14,
                    color=Colors.BLUE,
                )
            ]
        )
    )

    page.overlay.append(snapbar)
    snapbar.open = True
    page.update()

    return snapbar