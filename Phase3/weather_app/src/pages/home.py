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
                            ft.Text("24°C",size=40,weight=ft.FontWeight.BOLD),
                            ft.Text("Partly cloudy",size=17,weight=ft.FontWeight.BOLD),
                            ft.Row(
                                controls=[
                                    ft.Text("H: 26°C",size=15,weight=ft.FontWeight.BOLD),
                                    ft.Text("L: 24°C",size=15,weight=ft.FontWeight.BOLD)
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
    
    def create_container(sett,value):
        if sett == "Feels like":
            icon_to_use = ft.Icons.THERMOSTAT

        elif sett == "Humidity":
            icon_to_use = ft.Icons.WATER_DROP
            
        elif sett == "Wind":
            icon_to_use = ft.Icons.AIR
            
        elif sett == "UV Index":
            icon_to_use = ft.Icons.WB_SUNNY
            
        elif sett == "Visibility":
            icon_to_use = ft.Icons.VISIBILITY
            
        elif sett == "Air quality":
            icon_to_use = ft.Icons.MASKS
            
        return ft.Container(
            width=150,
            height=100,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            padding = 10,
            content = ft.Row(
                controls=[
                    ft.Icon(
                        icon_to_use,
                        size=25,
                        color=ft.Colors.BLUE_GREY
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                sett,
                                size=15,
                                color=ft.Colors.GREY_800
                            ),
                            ft.Text(
                                str(value),
                                size=15,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.BOLD
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
            
        )
    top_body = ft.Container(
        padding = 10,
        border_radius=10,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-0.707, -0.707),
            end=ft.Alignment(0.707, 0.707),
            colors=[
                ft.Colors.with_opacity(1, "#EDF8F6"),
                ft.Colors.with_opacity(1, "#EDF1FB"),
            ],
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                # Top Row
                ft.Row(
                        
                    controls=[
                        create_container("Feels like", "24°C"),
                        create_container("Humidity", "65%"),
                        create_container("Wind", "12 km/h"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    
                ),
                # Bottow row
                ft.Row(
                    controls=[
                        create_container("UV Index", "5"),
                        create_container("Visibility", "10 km"),
                        create_container("Air quality", "Good"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
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
                ft.Text("Weather now", size=30,color=ft.Colors.WHITE,weight=ft.FontWeight.BOLD),
                top_body,
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
            