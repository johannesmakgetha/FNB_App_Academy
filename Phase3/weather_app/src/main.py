import flet as ft
from pages.home import home_page


def main(page: ft.Page):

    page.add(home_page(page))


if __name__ == "__main__":
    ft.run(main)
