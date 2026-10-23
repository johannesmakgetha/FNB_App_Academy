import flet as ft
import json
import os
from pathlib import Path

import flet as ft

def get_assets_dir() -> Path:
    default_assets_dir = Path(__file__).parent / "assets"   # fallback for local runs
    return Path(os.environ.get("FLET_ASSETS_DIR", str(default_assets_dir))).resolve()

def write_username(username):
    file_path = get_assets_dir() / "data" / "username.json"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    user ={
        "username":username,
        }

    with open(file_path,"w") as f:
        json.dump(user,f,indent=2)



def home_page(page: ft.Page) ->ft.View:

    async def go_greet(e):
        await page.push_route("/greetings")

    alert = ft.AlertDialog(
        content=ft.Text("Please Enter a username!"),
        alignment=ft.Alignment.CENTER,
        title_padding=ft.Padding.all(25),
    )

    username = ft.TextField(
                text_style=ft.TextStyle(
                    color=ft.Colors.BLACK
                ),
                bgcolor=ft.Colors.WHITE,
                border_radius=30,
                hint_text='e.g "Johannes"',
                label= "Username",
                label_style=ft.TextStyle(
                    color=ft.Colors.BLACK
                ),
                helper_style=ft.TextStyle(
                    color=ft.Colors.RED,
                    size=15)
            
            )
   
    async def greet(e):
        if not username.value:
            page.show_dialog(alert)
            page.update()
            return
        else:
            write_username(username.value)
            await go_greet(e)
            username.helper = None
            username.update()



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
                            username,
                           
                            ft.Container(
                                
                                content=ft.Button(
                                    content= "Continue",
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_400,
                                    on_click=greet
                                )
                            )
            ])
                )
            ]
        )

    )




    return ft.View(
        route="/",
        controls=[
            body
        ]
    )