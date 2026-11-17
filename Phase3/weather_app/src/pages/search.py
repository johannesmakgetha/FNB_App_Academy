import flet as ft


def search_page(page: ft.Page) -> ft.View:
    async def go_to_settings(e):
        await page.push_route('/settings')
    
    async def go_to_home(e):
        await page.push_route('/home')

    app_bar = ft.AppBar(
        leading=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.BLACK,
            on_click=go_to_home
            
        ),
        bgcolor=ft.Colors.WHITE_70,
        title="Profile",
        center_title=True,
        title_text_style=ft.TextStyle(
            size = 20,
            color=ft.Colors.BLACK,
            weight=ft.FontWeight.BOLD
        ),
        
        )

    body = ft.Container(
        bgcolor=ft.Colors.BLACK_12,
        alignment=ft.Alignment.CENTER,
        width=330,
        height=660,
        align=ft.Alignment.CENTER,
        border_radius=30,
        content=ft.Column(
            controls=[
                app_bar,
                ft.Row(
                    margin=30
                ),
                ft.Text(
                    text_align=ft.TextAlign.END,
                    value="Profile",
                    size=30,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD 
                    ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.TextButton(
                            content="Home",
                            on_click=go_to_home,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLACK,
                                icon_size=20
                            )),
                        ft.TextButton(
                            content="Settings",
                            on_click=go_to_settings,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLACK,
                                icon_size=20
                            ))
                        ]
                    )
                ] 
            )
        )
        

    

    return ft.View(
        route="/search",
        appbar=app_bar,
        controls=[
            body
        ]
    )