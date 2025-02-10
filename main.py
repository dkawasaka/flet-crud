import flet as ft
# from model.db_wizard import db
from views.home import home


def main(page: ft.Page):
    # page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.window.min_width = 600
    # page.bgcolor = ft.Colors.BLACK


    page.title = page.route
    WIDTH = page.width
    HEIGHT = page.height

    def  router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(home(page, WIDTH, HEIGHT))

        page.title = page.route
        page.update()

    page.on_route_change = router
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)
    # ft.app(target=main)

    # image = ft.Container(
    #     expand=2,
    #     # alignment = ft.CrossAxisAlignment.CENTER,
    #      # = ft.CrossAxisAlignment.CENTER,
    #     # content=ft.Image(
    #     #     src=""
    #     # )
    # )

    # inputs = ft.Container(
    #     expand=2,
    # )
    #
    # buttons = ft.Container(
    #     expand=1,
    # )

    # layout = ft.Container(
    #     height=400,
    #     width=600,
    #     margin=ft.margin.symmetric(vertical=30, horizontal=100),
    #     shadow=ft.BoxShadow(blur_radius=100, color=ft.Colors.BROWN),
    #     border_radius=ft.border_radius.all(30),
    #     bgcolor = ft.Colors.WHITE,
    #     content=ft.Column(
    #         controls=[
    #             image,
    #             inputs,
    #             buttons,
    #         ]
    #     )
    # )

    # page.add(layout)


