import flet as ft
import json
import os
from pathlib import Path

import flet as ft

def get_assets_dir() -> Path:
    default_assets_dir = Path(__file__).parent / "assets"   # fallback for local runs
    return Path(os.environ.get("FLET_ASSETS_DIR", str(default_assets_dir))).resolve()


def load_users():
    default_path = get_assets_dir()

    with open(f"{default_path}/data/users.json","r") as f:
        return json.load(f)

USERS = load_users()

def update_users(user):
    for i , existing in enumerate(USERS["users"]):
        if existing["username"] == user["username"]:
            USERS["users"][i] = user
            break

    default_path = get_assets_dir()

    with open(f"{default_path}/data/users.json","w") as f:
        json.dump(USERS,f,indent=2)

def check_username(username):
    for user in USERS["users"]:
        if user["username"].lower() == username.lower():
            return user

    return None

def reset_password(page:ft.Page):

    username = ft.TextField(
                hint_text="Username",
                helper_style=ft.TextStyle(color=ft.Colors.RED),
                border_radius=ft.BorderRadius.all(20)
            )
    
    password = ft.TextField(
                hint_text="Password",
                helper_style=ft.TextStyle(color=ft.Colors.RED),
                password=True,
                can_reveal_password=True,
                border_radius=ft.BorderRadius.all(20)
        )

    confirm_password = ft.TextField(
                    hint_text="Password",
                    helper_style=ft.TextStyle(color=ft.Colors.RED),
                    password=True,
                    can_reveal_password=True,
                    border_radius=ft.BorderRadius.all(20)
            )

    error_message = ft.Text(
            value ="Username not found",
            size=15,
            color=ft.Colors.RED,
            weight=ft.FontWeight.BOLD,
            visible=False
            )
    def on_cancel(e):
        page.pop_dialog()

    def on_save(e):
        if not password.value:
            password.helper = "Password cannot be left empty"
            password.update()
            return
        else:
            password.helper = None
            password.update()

        if not confirm_password.value:
            confirm_password.helper = "Password cannot be left empty"
            confirm_password.update()
            return
        else:
            confirm_password.helper = None
            confirm_password.update()

        if password.value != confirm_password.value:
            error_message.visible = True
            error_message.value = "Passwords do not match"
            error_message.update()
            return
        else:
            error_message.visible = False
            error_message.update()

        user = page.session.store.get("user")

        user["password"] = password.value

        update_users(user)
        page.session.store.set("user",user)

        page.pop_dialog()




    def on_next(e):
        if not username.value:
            username.helper = "Username cannot be left empty"
            username.update()
            return
        else:
            username.helper = None
            username.update()

        user = check_username(username.value)

        if not user:
            error_message.visible = True
            error_message.update()
            return
        else:
            error_message.visible= False
            error_message.update()

        page.session.store.set("user",user)

        modal.title = "Update password"
        modal.content = ft.Column(
            tight=True,
            controls = [
                ft.Text(f"Username: {username.value}"),
                password,
                confirm_password,
                error_message
            ]

        )
        modal.actions =[
            ft.Button(
                content="Cancel",
                on_click=on_cancel
            ),
            ft.Button(
                content="Save",
                on_click=on_save
               
            )
        ]
        page.update()

    modal = ft.AlertDialog(
        modal=True,
        title="Confirm username",
        content=ft.Column(
            tight=True,
            controls=[
                username,
                error_message
            ]
        ),
        actions=[
            ft.Button(
                content="Cancel",
                on_click=on_cancel
            ),
            ft.Button(
                content="Next",
                on_click=on_next
            )
        ]
    )

    return modal