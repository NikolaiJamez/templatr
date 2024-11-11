from json import dumps, loads
import flet as ft
from uuid import uuid4
from custom_controls.Template import Template

DISABLED_ARROW_ICON = ft.IconButton(disabled = True, opacity = 0, icon = ft.icons.ARROW_DOWNWARD)
PERSISTENT_FILENAME = "templates.json"

def main (page: ft.Page):
    # Page Attributes
    page.window.frameless = True

    # Functions
    def create_template (e: ft.ControlEvent):
        return_flag = False
        for field in [category_field, title_field, template_field]:
            field.border_color = None
            if field.value == "":
                field.border_color = ft.colors.RED
                return_flag = True
            field.update()
        if return_flag:
            return

        templates_row.controls.append(
            Template(str(uuid4()), category_field.value, title_field.value, template_field.value)
        )
        category_field.value = ""
        title_field.value = ""
        template_field.value = ""
        category_field.update()
        title_field.update()
        template_field.update()
        templates_row.update()

    def save_templates (e: ft.ControlEvent):
        data = [template.data for template in templates_row.controls]
        with open(PERSISTENT_FILENAME, "w") as outfile:
            outfile.writelines(dumps(data, indent = 4))

    def refresh_templates (e: ft.ControlEvent = None):
        try:
            with open(PERSISTENT_FILENAME, "r") as infile:
                template_data = loads(infile.read())
        except FileNotFoundError:
            with open(PERSISTENT_FILENAME, 'w') as outfile:
                pass
            return
        
        for data in template_data:
            templates_row.controls.append(
                Template(
                    data.get("template_id"),
                    data.get("template_category"),
                    data.get("template_title"),
                    data.get("template_text"))
            )
        templates_row.update()


    def reorder_templates (e: ft.ControlEvent):
        raise NotImplemented("reorder_templates function note implemented")

    def delete_all_templates (e: ft.ControlEvent):
        raise NotImplemented("delete_all_templates function note implemented")

    nav_filter = ft.TextField(label = "Search/Filter")

    category_field = ft.TextField(
        col = 2,
        label = "Category",
        suffix = DISABLED_ARROW_ICON)
    title_field = ft.TextField(
        col = 3,
        label = "Title",
        suffix = DISABLED_ARROW_ICON)
    template_field = ft.TextField(
        col = 6,
        label = "Template Text",
        multiline = True,
        on_submit = create_template,
        shift_enter = True,
        suffix = ft.IconButton(
            icon = ft.icons.ARROW_DOWNWARD,
            on_click = create_template))

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
                category_field,
                title_field,
                template_field,
            ],
        ),
        ft.Divider(opacity = 0),
        templates_row,
    )
    refresh_templates()


if __name__ == "__main__":
    ft.app(main)
