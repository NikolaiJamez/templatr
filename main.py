import flet as ft
from blivet.partitioning import align_size_for_disklabel
from setuptools.command.saveopts import saveopts


def main (page: ft.Page):
    # Page Attributes
    page.window.frameless = True

    # Functions
    def create_template (e: ft.ControlEvent):
        templates_row.controls.append(
            ft.Card(
                content = ft.Container(
                    content = ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(
                                        opacity = 0.5,
                                        size = 8,
                                        value = "Category",
                                        italic = True,
                                    ),
                                    ft.IconButton(
                                        height = 32,
                                        icon = ft.icons.CLOSE,
                                        icon_color = ft.colors.RED,
                                        icon_size = 16,
                                        visible = False,
                                        width = 32)
                                ],
                                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Row(
                                [
                                    ft.Text(
                                        size = 16,
                                        value = "Title Text",
                                        weight = ft.FontWeight.W_700,
                                    ),

                                ],
                                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.ResponsiveRow([ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae velit massa. Proin tempus placerat nunc, et dignissim odio lacinia at. Donec fermentum luctus ante nec pulvinar.")]),
                        ]
                    ),
                    padding = 10,
                ),
                col = {"md": 5, "lg": 4}
            )
        )
        templates_row.update()

    def save_templates (e: ft.ControlEvent):
        raise NotImplemented("save_templates function note implemented")

    def refresh_templates (e: ft.ControlEvent):
        raise NotImplemented("refresh_templates function note implemented")

    def reorder_templates (e: ft.ControlEvent):
        raise NotImplemented("reorder_templates function note implemented")

    def delete_all_templates (e: ft.ControlEvent):
        raise NotImplemented("delete_all_templates function note implemented")

    nav_filter = ft.TextField(label = "Search/Filter")
    templates_row = ft.ResponsiveRow(columns = 20)

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


    page.add(
        ft.Divider(opacity = 0),
        ft.ResponsiveRow(
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [
                ft.IconButton(
                    col = 2,
                    icon = ft.icons.ADD,
                    on_click = create_template)
            ],
        ),
        ft.Divider(opacity = 0),
        templates_row,
    )


if __name__ == "__main__":
    ft.app(main)
