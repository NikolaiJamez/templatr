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
            Template(
                str(uuid4()),
                category_field.value,
                title_field.value,
                template_field.value,
                delete_template)
        )
        category_field.value = ""
        title_field.value = ""
        template_field.value = ""
        category_field.update()
        title_field.update()
        template_field.update()
        templates_row.update()

        save_button.icon = ft.icons.SAVE_AS
        save_button.update()


    def save_templates (e: ft.ControlEvent):
        data = [template.data for template in templates_row.controls]
        with open(PERSISTENT_FILENAME, "w") as outfile:
            outfile.writelines(dumps(data, indent = 4))
        pending_changes(e)


    def refresh_templates (e: ft.ControlEvent = None):
        try:
            with open(PERSISTENT_FILENAME, "r") as infile:
                template_data = loads(infile.read())
        except FileNotFoundError:
            with open(PERSISTENT_FILENAME, 'w') as outfile:
                pass
            return
        
        templates_row.controls = []
        for data in template_data:
            templates_row.controls.append(
                Template(
                    data.get("template_id"),
                    data.get("template_category"),
                    data.get("template_title"),
                    data.get("template_text"),
                    delete_template)
            )
        
        templates_row.update()
        
        if e:
            save_button.icon = ft.icons.SAVE
            delete_all_button.icon = ft.icons.DELETE
            save_button.update()
            delete_all_button.update()


    def reorder_templates (e: ft.ControlEvent):
        for template in templates_row.controls:
            template.delete_button.visible = not template.delete_button.visible
            template.update()


    def delete_all_templates (e: ft.ControlEvent):
        if len(templates_row.controls) == 0:
            # TODO Show message advising no templates to remove
            return
        templates_row.controls = []
        templates_row.update()
        pending_changes(e)

    
    def delete_template(e: ft.ControlEvent):
        for idx, template in enumerate(templates_row.controls):
            template_id = template.data.get("template_id")
            
            if e.control.data != template_id:
                continue

            templates_row.controls.pop(idx)
            templates_row.update()
            save_button.icon = ft.icons.SAVE_AS
            save_button.update()
            break

    
    def pending_changes(e: ft.ControlEvent = None):
        save_button.icon = ft.icons.SAVE_AS
        delete_all_button.icon = ft.icons.AUTO_DELETE
        save_button.update()
        delete_all_button.update()


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
    
    delete_all_button = ft.IconButton(
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
            delete_all_button,
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
