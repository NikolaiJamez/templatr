import flet as ft
from setuptools.command.saveopts import saveopts


def main(page: ft.Page):
    page.window.frameless = True


    nav_filter = ft.TextField(label = "Search/Filter")

    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.COPY_ALL),
        leading_width = 50,
        title = ft.Text("Templatr"),
        bgcolor = ft.colors.SURFACE_VARIANT,
        actions = [
            nav_filter,
            ft.VerticalDivider(width = 50, opacity = 0),
        ],
    )

    page.add()


if __name__ == "__main__":
    ft.app(main)
