import flet as ft


def home_page(page: ft.Page) -> ft.View:

    top = ft.Container(
        width = 310,
        height = 660 * 0.40,
        gradient = ft.LinearGradient(
                begin = ft.Alignment.BOTTOM_LEFT,
                end = ft.Alignment.TOP_LEFT,
                colors = [ft.Colors.LIGHT_BLUE_600,ft.Colors.LIGHT_BLUE_900]
                ),
        border_radius=30,
        animate=ft.Animation(duration=350,curve=ft.AnimationCurve.DECELERATE),
        padding=15,
        content=ft.Column(
            alignment=ft.Alignment.TOP_LEFT,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Ficksburg, FS",size=17,weight=ft.FontWeight.W_500,color=ft.Colors.WHITE)
                        ],
                    ),
                ft.Container(padding=ft.Padding(bottom=5)),
                ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        width =200,
                                        height=150,
                                        alignment=ft.Alignment.CENTER_LEFT,
    
                                        content=ft.Image(
                                            src="src/assets/9176536.png",
                                            width=120,
                                            height=120,
                                            fit=ft.BoxFit.CONTAIN
                                        )

                                    )
                                ]
                            ),
                            ft.Column(
                                spacing=5,
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Today",
                                            size=12,
                                            text_align=ft.TextAlign.CENTER,
                                            color=ft.Colors.WHITE,
                                            ),
                                ]
                            )

                        ]
                    )
                ]
            )
            )

    return top
            