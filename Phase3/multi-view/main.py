import flet as ft
from pages.home import home_page
from pages.greetings import greet_page

def main(page: ft.Page):


    page.title = "Greetings" 

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE_70


    def route_change():
        page.views.clear()

        if page.route == "/":
            page.views.append(home_page(page))
        elif page.route == "/greetings":
            page.views.append(greet_page(page))
        else:
            page.views.append(home_page(page))
        
        page.update() 

    page.on_route_change = route_change
    route_change()


if __name__ == "__main__":
    ft.run(main)
