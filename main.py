import flet as ft

def main(page: ft.Page):
    page.window.frameless = True

    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.COPY_ALL),
        leading_width = 50,
        title = ft.Text("Templatr"),
        bgcolor = ft.colors.SURFACE_VARIANT,
    )

    page.add()


if __name__ == "__main__":
    ft.app(main)
