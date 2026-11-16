import flet as ft
import httpx



LATLON_URL = "http://127.0.0.1:8000/weather"

def home_page(page: ft.Page) -> ft.View:
    lat_input = ft.TextField(
        label="lat"
    )
    lon_input = ft.TextField(
        label="lon"
    )
    
    city_name = ft.Text(value="",size=20,weight=ft.FontWeight.W_500,color=ft.Colors.WHITE)
    city_temp = ft.Text(value="",size=40,weight=ft.FontWeight.BOLD)
    city_description = ft.Text(value="",size=17,weight=ft.FontWeight.BOLD)
    city_high = ft.Text(value="",size=15,weight=ft.FontWeight.BOLD)
    city_low = ft.Text(value="",size=15,weight=ft.FontWeight.BOLD)
    city_feel_like = ft.Text(value="",color=ft.Colors.WHITE,size=12)
    city_humidity = ft.Text(value="")
    city_wind = ft.Text(value="")
    city_visibility = ft.Text(value="")
    

 
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
                        city_name
                        ],
                    ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            controls = [
                            city_temp,
                            city_description,
                            ft.Row(
                                controls=[
                                    city_low,
                                    city_high
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
                        content=city_feel_like,
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


    
    def create_container(title_container,value):
        if title_container == "Feels like":
            icon_to_use = ft.Icons.THERMOSTAT

        elif title_container == "Humidity":
            icon_to_use = ft.Icons.WATER_DROP
            
        elif title_container == "Wind":
            icon_to_use = ft.Icons.AIR
            
        elif title_container == "Visibility":
            icon_to_use = ft.Icons.VISIBILITY

        value_text = ft.Text(
                    str(value),
                    size=15,
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.BOLD
                )

        current_container =  ft.Container(
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
                                title_container,
                                size=15,
                                color=ft.Colors.GREY_800
                            ),
                            value_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
            )

        return current_container, value_text

    feels_like_container, feels_like_text = create_container("Feels like","")
    humidity_container, humidity_text = create_container("Humidity","")
    wind_container, wind_text = create_container("Wind","")
    visibility_container, visibility_text = create_container("Visibility","")


    
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
                        feels_like_container,
                        humidity_container,
                        wind_container,
                        visibility_container,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    
                ),
                
            ]
        )

    )

    def hour_forecast_container(time,icon,temp,rain):
        return ft.Container(
                    width=90,
                    height=150,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding = 10,
                    content = ft.Column(
                        controls=[
                            ft.Text(
                                time,
                                size=15,
                                color=ft.Colors.GREY_800
                            ),
                            ft.Icon(
                                icon,
                                size=25,
                                color=ft.Colors.BLUE_GREY
                            ),
                            ft.Text(
                                value=f"{temp}°",
                                size=15,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.Icon(
                                        icon=ft.Icons.WATER_DROP,

                                    ),
                                    ft.Text(
                                        value=f"{rain}%",
                                        color=ft.Colors.BLACK,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                ]
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        
                    )
                    
                )

    hourly_forecast = [
    {"time": "09:00", "icon": ft.Icons.WB_SUNNY, "temp": 24, "rain": 0},
    {"time": "10:00", "icon": ft.Icons.WB_SUNNY, "temp": 26, "rain": 0},
    {"time": "11:00", "icon": ft.Icons.WB_CLOUDY, "temp": 27, "rain": 5},
    {"time": "12:00", "icon": ft.Icons.CLOUD, "temp": 28, "rain": 10},
    {"time": "13:00", "icon": ft.Icons.WATER_DROP, "temp": 25, "rain": 60},
    {"time": "14:00", "icon": ft.Icons.THUNDERSTORM, "temp": 23, "rain": 80},
    {"time": "15:00", "icon": ft.Icons.CLOUD, "temp": 22, "rain": 20},
    {"time": "16:00", "icon": ft.Icons.WB_SUNNY, "temp": 21, "rain": 0},
    {"time": "17:00", "icon": ft.Icons.WB_SUNNY, "temp": 20, "rain": 0},
        ]

    day_forecast = [
    {"day": "Mon", "icon": ft.Icons.WB_SUNNY, "min_temp": 16, "max_temp": 28, "rain": 0},
    {"day": "Tue", "icon": ft.Icons.WB_CLOUDY, "min_temp": 17, "max_temp": 26, "rain": 10},
    {"day": "Wed", "icon": ft.Icons.CLOUD, "min_temp": 15, "max_temp": 24, "rain": 30},
    {"day": "Thu", "icon": ft.Icons.THUNDERSTORM, "min_temp": 14, "max_temp": 22, "rain": 80},
    {"day": "Fri", "icon": ft.Icons.WATER_DROP, "min_temp": 15, "max_temp": 23, "rain": 60},
]
    def day_forecast_container(days,icon,min_temp,max_temp,rain):
        return ft.Container(
                    border=ft.Border.all(1,ft.Colors.with_opacity(0.3,ft.Colors.GREY_800)),
                    height=80,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    padding = 10,
                    content = ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                days,
                                size=15,
                                color=ft.Colors.GREY_800
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                ft.Icon(
                                    icon=ft.Icons.WATER_DROP,
                                    ),
                                ft.Text(
                                    value=f"{rain}%",
                                    color=ft.Colors.BLACK,
                                    weight=ft.FontWeight.BOLD
                                    ),
                                ]
                            ),

                            ft.Icon(
                                icon,
                                size=25,
                                color=ft.Colors.BLUE_GREY
                            ),
                            ft.Text(
                                value=f"{min_temp}°",
                                size=15,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                value="|",
                                size=15,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                value=f"{max_temp}°",
                                size=15,
                                color=ft.Colors.BLACK,
                                weight=ft.FontWeight.BOLD
                            ),
                            
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        
                    )
                    
                )
    
    body_hour = ft.Container(
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

        content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls = [
                hour_forecast_container(hour["time"],hour["icon"],hour["temp"],hour["rain"]) for hour in hourly_forecast
            ],
            scroll=ft.ScrollMode.AUTO
        )
    )

    body_day = ft.Container(
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
    
            content = ft.Column(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing =0,
                controls = [
                    day_forecast_container(day["day"],day["icon"],day["min_temp"],day["max_temp"],day["rain"]) for day in day_forecast
                ],
                scroll=ft.ScrollMode.AUTO
            )
        )


    async def search_weather(e):
        print("\nYes")
        lat = lat_input.value
        lon = lon_input.value
    
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url=LATLON_URL,
                    params={
                        "lat":lat,
                        "lon":lon
                    }    
                )
                response.raise_for_status()
                data = response.json()
    
                print("\nYes")
                # data
                current = data.get("current",{})
                city = current.get("name","")
                current_temp = int(current.get("main",{}).get("temp",0))
                current_description = data["current"]["weather"][0]["description"]
                high_current_temp = int(current.get("main",{}).get("temp_max",0))
                low_current_temp = int(current.get("main",{}).get("temp_min",0))
    
                current_feel_like = int(current.get("main",{}).get("feels_like",0))
                humidity = current.get("main",{}).get("humidity",0)
                wind = int(current.get("wind",{}).get("speed",0) * 3.6)
                visibility = int(current.get("visibility",0) / 1000)
    
    
                curr_temp = data["current"]
                hour_cast = data["forecast"]["hours"]
                day_cast = data["forecast"]["days"]
    
                    # assign the data
    
                city_name.value = city
                city_temp.value = f"{current_temp}°C"
                city_description.value = current_description
                city_high.value = f"H: {high_current_temp}°C"
                city_low.value = f"L: {low_current_temp}°C"
                city_feel_like.value = f"Feel like {current_feel_like}°C"
                city_humidity_value = f"{humidity} %"
                city_wind_value = f"{wind} km/h"
                city_visibility_value = f"{visibility} km"

                feels_like_text.value = f"{current_feel_like}°C"
                humidity_text.value = city_humidity_value
                wind_text.value = city_wind_value
                visibility_text.value = city_visibility_value
                    
                    
                print(
                        f"""
                        name: {city}
                        temp: {current_temp}
                        description: {current_description}
                        high: {high_current_temp}
                        low: {low_current_temp}
                        
                        feels like: {current_feel_like}
                        humidity: {humidity} %
                        wind: {wind} km/h
                        visibility: {visibility} km
                        """)
    
        except:
            pass
    
        page.update()
        
    


    search_button = ft.Button(
            content = "Search",
            on_click = search_weather

            
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
            scroll=ft.ScrollMode.AUTO,
            controls=[
                lat_input,
                lon_input,
                search_button,
                top,
                ft.Text("Weather now", size=30,color=ft.Colors.WHITE,weight=ft.FontWeight.BOLD),
                top_body,
                ft.Text("Hour forecast", size=30,color=ft.Colors.WHITE,weight=ft.FontWeight.BOLD),
                body_hour,
                ft.Text("Day forecast", size=30,color=ft.Colors.WHITE,weight=ft.FontWeight.BOLD),
                body_day,
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
            