import flet as ft
from pages.home import home_page
from pages.search import search_page



co_ordinates = {
    "selected_lat": None,
    "selected_lon": None
}

def main(page: ft.Page):

    def route_change():
        page.views.clear()

        if page.route == "/":
            page.views.append(home_page(page,co_ordinates))
        elif page.route == "/home":
            page.views.append(home_page(page,co_ordinates))
        elif page.route == "/search":
            page.views.append(search_page(page,co_ordinates))

        page.update()

    page.on_route_change = route_change
    route_change()
    # page.add(home_page(page))


if __name__ == "__main__":
    ft.run(main)
