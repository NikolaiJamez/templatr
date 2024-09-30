import flet as ft
from setuptools.command.saveopts import saveopts


def main(page: ft.Page):
    page.window.frameless = True

    def save_templates():
        pass

    def refresh_templates():
        pass

    def reorder_templates():
        pass

    def delete_all_templates():
        pass

    nav_filter = ft.TextField(label = "Search/Filter")
    save_button = ft.IconButton(
        icon = ft.icons.SAVE,
        icon_color = ft.colors.GREEN,
        tooltip = "Save",
        on_click = save_templates)
    refresh_button = ft.IconButton(
        icon = ft.icons.REFRESH,
        tooltip = "Refresh",
        on_click = refresh_templates)
    reorder_button = ft.IconButton(
        icon = ft.icons.SHUFFLE,
        tooltip = "Reorder",
        on_click = reorder_templates)
    delete_button = ft.IconButton(
        icon = ft.icons.DELETE,
        icon_color = ft.colors.RED,
        tooltip = "Delete All - WARNING",
        on_click = delete_all_templates)



    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.COPY_ALL),
        leading_width = 50,
        title = ft.Text("Templatr"),
        bgcolor = ft.colors.SURFACE_VARIANT,
        actions = [
            nav_filter,
            ft.VerticalDivider(width = 50, opacity = 0),
            save_button,
            refresh_button,
            reorder_button,
            delete_button,
        ],
    )

    page.add()


if __name__ == "__main__":
    ft.app(main)
