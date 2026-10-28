import flet as ft
from components.reset_password import reset_password

def login_page(page: ft.Page) -> ft.View:
    page.title = "Login Page"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username = ft.TextField(
            hint_text="Username",
            text_style=ft.TextStyle(
                color="#0084a8"
            ),
            helper_style=ft.TextStyle(color=ft.Colors.RED),
            width=page.width * 0.5,
            border_radius=ft.BorderRadius.all(20)
        )

    password = ft.TextField(
            hint_text="Password",
            text_style=ft.TextStyle(
                color="#0084a8"
            ),
            helper_style=ft.TextStyle(color=ft.Colors.RED),
            password=True,
            can_reveal_password=True,
                width=page.width * 0.5,
            border_radius=ft.BorderRadius.all(20)
    )

    error_message = ft.Text(
        "Invalid username or password",
        size=15,
        weight=ft.FontWeight.BOLD,
        visible=False
        )

    user = {
        "username": "user1",
        "password":"pass1"
    }

    def login_click(e):
        # chech username if its not empty
        if not username.value:
            username.helper = "Username cannot be left empty"
            username.update()
            return
        else:
            username.helper = None
            username.update()

        if not password.value:
            password.helper = "Password cannot be left empty"
            password.update()
            return
        else:
            password.helper = None
            password.update()

        if username.value == user["username"] and password.value == user["password"]:
            error_message.visible = False
            error_message.update()
            print("Welcome back sir")
        else:
            error_message.visible = True
            error_message.update()
                                                                         
        
    def login_sign(e):
        if e.control.content.value == "Sign up":
            print("Sign up")

    def on_forgot_password(e):
        page.show_dialog(reset_password(page))
    
    body = ft.Container(
        expand=True,
        bgcolor="#0084a8",
        alignment=ft.Alignment.CENTER,
        content=ft.Container(
            height=page.height * 0.8,
            width=page.width * 0.5,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.BorderRadius.all(20),
            padding=ft.Padding(40,30,40,50),
            content=ft.Column(
                
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    #Login Text
                    ft.Container(
                        padding=ft.Padding(0,10,0,20),
                        content=ft.Text(
                            value="Login",
                            size = 40,
                            weight=ft.FontWeight.BOLD,
                            color = "#0084a8"
                        )
                    ),
                    #Username
                    ft.Row(
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.PERSON,
                                color="#0084a8"
                            ),
                            ft.Text(
                                value = "Username",
                                size=15,
                                weight=ft.FontWeight.BOLD,
                                color="#0084a8"
                            )
                        ]
                    ),
                    username,
                    ft.Container(height=15),
                    # Password
                    ft.Row(
                        controls=[
                            ft.Icon(
                                icon=ft.Icons.LOCK,
                                color="#0084a8"
                            ),
                            ft.Text(
                                value = "Password",
                                size=15,
                                weight=ft.FontWeight.BOLD,
                                color="#0084a8"
                            )
                        ]
                    ),
                    password,

                    # remember me and forgot password 
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Checkbox(
                                label="Keep me logged in",
                                label_style=ft.TextStyle(
                                    color="#0084a8"
                                )
                            ),
                            ft.GestureDetector(
                                on_tap=on_forgot_password,
                                content=ft.Text(
                                    "Forgot password?",
                                    size = 15,
                                    weight=ft.FontWeight.BOLD,
                                    color="#0084a8",
                                                                
                                    )
                            )
                        ]
                    ),

                    # error message
                    error_message,

                    # Login Button
                    ft.Container(
                        padding=ft.Padding(0,40,0,0),
                        content=ft.Button(
                            content="Login",
                            bgcolor="#0084a8",
                            color="#ffffff",
                            width=page.width * 0.3,
                            height=50,
                            on_click=login_click
                        )
                    ),

                    ft.Container(
                        padding=ft.Padding(0,20,0,0),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value ="Don't have an account?",
                                    size = 13,
                                    color="#0084a8"
                                ),
                                ft.GestureDetector(
                                    on_tap=login_sign,
                                    content=ft.Text(
                                        value = "Sign up",
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        color="#0084a8"
                                    )
                                )
                            ]
                        )
                    )
                    
                    
                ]
            )

        )
    )

    return body
