import flet as ft


def main(page: ft.Page):


    page.title = "Greetings" 

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE_70


    name = ft.TextField(
            border_radius=30,
            width=float('inf'),
            hint_text='e.g "Johannes"',
            label= "Name",
            helper_style=ft.TextStyle(
                color=ft.Colors.RED,
                size=15)
        
        )
    display = ft.Text(
                weight=ft.FontWeight.BOLD,
                size=20
                )

    def greet(e):
        if not name.value:
            name.helper = "Enter a name"
            display.value = None
            name.update()
            display.update()
            return
        else:
            display.value = f"Hello, {name.value}!"
            name.helper = None
            name.update()
            display.update()



    body = ft.Container(
        
        content=ft.Container(
            padding=ft.Padding(10,20,10,10),
            width=page.width * 0.4,
            height=page.height * 0.5,
            bgcolor=ft.Colors.LIGHT_BLUE_800,
            border_radius=20,
            content = ft.Column(
                width=float('inf'),
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                   ft.Row(
                       margin=ft.Margin(0,0,0,20),
                       alignment=ft.MainAxisAlignment.CENTER,
                       controls=ft.Text(
                           value = "Greetings",
                           size=15,
                           weight=ft.FontWeight.BOLD
                           )

                   ),   
                name,
                ft.Row(
                    
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=ft.Button(
                        
                        content= "Greet Me",
                        style=ft.ButtonStyle(
                            color= ft.Colors.BLACK,
                            bgcolor=ft.Colors.WHITE,
                            
                        ),
                        on_click=greet
                    )
                ),
                ft.Row(
                    margin=ft.Margin(0,15,0,0),
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=display
                )
            ]    
        )
        )
    )
    
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=body,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
