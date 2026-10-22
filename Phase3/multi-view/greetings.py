import flet as ft

def greet_page(page: ft.Page) ->ft.View:

    async def go_back(e):
        await page.push_route("/")

    
    display = ft.Text(
            value="Hello",
            weight=ft.FontWeight.BOLD,
            size=20
                    )

    async def back(e):
        await go_back(e)
    # def greet(e):
    #     if not username.value:
    #         username.helper = "Enter a name"
    #         username.update()
    #         return
    #     else:
    #         go_greet()
    #         username.helper = None
    #         username.update()



    body = ft.Container(
        bgcolor=ft.Colors.BLUE_ACCENT,
        width=page.width,
        height=page.height,
        padding=ft.Padding(30,0,30,0),
        content=ft.Column(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                        bgcolor=ft.Colors.BLACK,
                        border_radius=20,
                        padding=35,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                            controls=[
                                ft.Text(
                                text_align=ft.TextAlign.CENTER,    
                                value = "Two-View Greeting App",
                                size=20,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.BOLD
                            ),
                            display,
                           
                            ft.Container(             
                                content=ft.Button(
                                    content= "Back",
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_400,
                                    on_click=back
                                )
                            )
            ])
                )
            ]
        )

    )




    return ft.View(
        route="/greeting",
        controls=[
            body
        ]
    )