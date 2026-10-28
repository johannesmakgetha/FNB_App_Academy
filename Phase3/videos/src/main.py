import flet as ft


def main(page: ft.Page):
    page.title = "Login Page"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    body = ft.Container(
        expand=True,
        bgcolor="#0084a8",
        alignment=ft.Alignment.CENTER,
        content=ft.Container(
            height=page.height * 0.8,
            width=page.width * 0.5,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.BorderRadius.all(20),
            padding=ft.Padding(40,40,40,40),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    #Login Text
                    ft.Container(
                        padding=ft.Padding(0,20,0,40),
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
                    ft.TextField(
                        hint_text="Username",
                        text_style=ft.TextStyle(
                            color="#0084a8"
                        ),
                        width=page.width * 0.5,
                        border_radius=ft.BorderRadius.all(20)
                    ),
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
                    ft.TextField(
                        hint_text="Password",
                        text_style=ft.TextStyle(
                            color="#0084a8"
                        ),
                        password=True,
                        can_reveal_password=True,
                        width=page.width * 0.5,
                        border_radius=ft.BorderRadius.all(20)
                    ),

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
                            ft.Text(
                                "Forgot password",
                                style=ft.TextStyle(
                                    color=ft.Colors.BLUE
                                )
                            )
                        ]
                    ),

                    # error message
                    ft.Text(
                        "Invalid username or password",
                        size=15,
                        weight=ft.FontWeight.BOLD,
                        visible=False
                    ),

                    # Login Button
                    ft.Container(
                        padding=ft.Padding(0,40,0,0),
                        content=ft.Button(
                            content="Login",
                            bgcolor="#0084a8",
                            color="#ffffff",
                            width=page.width * 0.3,
                            height=50
                        )
                    ),
                    
                    
                ]
            )

        )
    )

    page.add(body)


if __name__ == "__main__":
    ft.run(main)
