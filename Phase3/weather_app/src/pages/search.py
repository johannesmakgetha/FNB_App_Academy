import flet as ft
import httpx

CITY_URL = "http://127.0.0.1:8000/city"

def search_page(page: ft.Page,co_ordinates) -> ft.View:
    
    
    async def go_to_settings(e):
        await page.push_route('/settings')
    
    async def go_to_home(e):
        await page.push_route('/home')

    app_bar = ft.AppBar(

        leading=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.WHITE,
            on_click=go_to_home
            
        ),
        bgcolor=ft.Colors.BLACK,
        title="Weather",
        center_title=True,
        elevation= 4,
        shadow_color=ft.Colors.WHITE,
        title_text_style=ft.TextStyle(
            size = 20,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD
        ),
        
        )

    error_message = ft.Text(
        "Please check Internet connection or correct your city name",
        size= 15,
        weight=ft.FontWeight.BOLD,
        visible= False
    )

    city_name = ft.TextField(
        expand=True,
        hint_text = 'e.g "Johannesburg"',
        text_style= ft.TextStyle(
            color = ft.Colors.BLACK
        ),
        bgcolor = ft.Colors.WHITE,
        border_radius=30,
        helper_style=ft.TextStyle(
            color=ft.Colors.RED,
            size=15
        )
    )

    searched_column = ft.Column(
        spacing = 0,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        scroll=ft.ScrollMode.AUTO
    )

    async def select_city(lat,lon):

        co_ordinates["selected_lat"] = lat
        co_ordinates["selected_lon"] = lon

        await page.push_route("/home")

    def searched_city_container(city_name,lat,lon,state,country):
        return ft.Container(
                    border=ft.Border.only(bottom=ft.BorderSide(2,ft.Colors.with_opacity(0.3,ft.Colors.GREY_100))),
                    bgcolor=ft.Colors.GREY_800,
                    padding=ft.Padding(0,5,5,10),
                    on_click= lambda e: page.run_task(select_city,lat,lon),
                    content = ft.Row(
                        controls=[
                            ft.Column(
                                spacing = 0,
                                controls=[
                                ft.Text(
                                        city_name,
                                        size=25,
                                        color=ft.Colors.WHITE
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            state,
                                            size=15,
                                            color=ft.Colors.GREY_300
                                        ),
                                        ft.Text(
                                            ",",
                                            size=15,
                                            color=ft.Colors.GREY_300
                                        ),
                                        ft.Text(
                                            country,
                                            size=15,
                                            color=ft.Colors.GREY_300
                                        )
                                    ]
                                )
                                ]
                            )
                            
                            
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        
                    )
                    
                )

    app_city_data = {
        "searched_results": {}
    }
    async def search_name(e):
        if not city_name.value:
            city_name.helper = "Please enter a place"
            city_name.update()
            return
        else:
            city_name.helper = None
            city_name.update()
    
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url=CITY_URL,
                    params={
                        "city_name":city_name.value,
                    }    
                )
                response.raise_for_status()
                app_city_data["searched_results"] = response.json()

                display_container = [
                    searched_city_container(
                        app_city_data["searched_results"][i]["name"],
                        app_city_data["searched_results"][i]["lat"],
                        app_city_data["searched_results"][i]["lon"],
                        app_city_data["searched_results"][i]["state"],
                        app_city_data["searched_results"][i]["country"],
                        )
                    for i in app_city_data["searched_results"]
                ]

                searched_column.controls = display_container
                
               
    
        except httpx.HTTPError as e:
            print(e)

    
        page.update()
    
    top_body = ft.Container(
        bgcolor=ft.Colors.BLACK,
        border=ft.Border.only(bottom=ft.BorderSide(3,color=ft.Colors.WHITE)),
        content=ft.Column(
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.BLUE_ACCENT,
                    border_radius=0,
                    padding = 15,
                    content=ft.Column(
                        controls=[
                            city_name,
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                content=ft.Button(
                                    content= "Search",
                                    color = ft.Colors.WHITE,
                                    bgcolor=ft.Colors.LIGHT_BLUE_400,
                                    on_click=search_name
                                )
                            )]
                            )
                        ]
                    )

                ),
                
                ] 
            )
        )

    bottom_body = ft.Container(
        padding= 10,
        border_radius= 10,
        bgcolor=ft.Colors.GREY_800,
        content = searched_column
    )
        
    main_layout = ft.Container(
        expand=True,
        bgcolor = ft.Colors.BLACK,
        content=ft.Column(
            expand = True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                top_body,
                bottom_body
            ]
        )
    )
    

    return ft.View(
        bgcolor=ft.Colors.BLACK,
        route="/search",
        appbar=app_bar,
        controls=[
            main_layout
        ]
    )