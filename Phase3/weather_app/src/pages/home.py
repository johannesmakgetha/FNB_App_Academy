import flet as ft


def home_page(page: ft.Page) -> ft.View:

    top = ft.Container(
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
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(
                            content = ft.Icon(
                                ft.Icons.LOCATION_ON,
                                size=20,
                                color=ft.Colors.WHITE
                            ),
                            width=35,
                            height=35,
                            bgcolor=ft.Colors.with_opacity(0.15,ft.Colors.WHITE),
                            alignment=ft.Alignment.CENTER,
                            border_radius=10,
                            border= ft.Border.all(
                                1,
                                ft.Colors.with_opacity(0.3,ft.Colors.WHITE)
                            )
                        ),
                        ft.Text("Ficksburg",size=20,weight=ft.FontWeight.W_500,color=ft.Colors.WHITE)
                        ],
                    ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            controls = [
                            ft.Text("24",size=40,weight=ft.FontWeight.BOLD),
                            ft.Text("Partly cloudy",size=17,weight=ft.FontWeight.BOLD),
                            ft.Row(
                                controls=[
                                    ft.Text("H: 26",size=15,weight=ft.FontWeight.BOLD),
                                    ft.Text("L: 24",size=15,weight=ft.FontWeight.BOLD)
                                ]
                            )
                            ]

                        ),
                        ft.Container(
                            bgcolor=ft.Colors.WHITE,
                            content=ft.Text("Icon")
                        )
                    ]
                ),

            ft.Row(
                controls=[
                    ft.Container(
        content=ft.Text(
            "Feels like",
            color=ft.Colors.WHITE,
            size=12,
        ),
        padding=ft.Padding.symmetric(horizontal=12, vertical=6),
        bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
        border=ft.Border.all(
            1,
            ft.Colors.with_opacity(0.35, ft.Colors.WHITE)
        ),
        border_radius=20,
    ),

                ]
            )

               
            ]
            )
            )
    main_layout = ft.Container(
        expand=True,
        gradient= ft.LinearGradient(
                    begin=ft.Alignment.TOP_LEFT,
                    end = ft.Alignment.BOTTOM_RIGHT,
                    colors=[
                "#6988DC",
                "#769DEB",
                "#A27EE3",
            ]
                ),
        padding=20,
        content=ft.Column(
            controls=[
                top,
                ft.Text(
                    "Bottom Content",
                    size = 30,
                    color = ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD
                )
            ]
        )


    )
    return main_layout
            