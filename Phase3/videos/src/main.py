import flet as ft
from pages.login import login_page

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    page.add(login_page(page))


if __name__ == "__main__":
    ft.run(main)
