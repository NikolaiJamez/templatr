from flet import (
Card,
Container,
Column,
Row,
Text,
IconButton,
ResponsiveRow,
colors,
icons,
MainAxisAlignment,
FontWeight,
)
from typing import Callable

DEFAULT_COL_SIZE = {"md": 5, "lg": 4}

class Template(Card):

    def __init__(self, id_str: str, category: str, title: str, template_text: str, delete_function: Callable):
        super().__init__(col = DEFAULT_COL_SIZE)
        self.delete_button = IconButton(
            height = 32,
            icon = icons.CLOSE,
            icon_color = colors.RED,
            icon_size = 16,
            visible = False,
            width = 32,
            on_click = delete_function,
            data = id_str)
        
        self.content = Container(
            content = Column(
                [
                    Row(
                        [
                            Text(
                                opacity = 0.5,
                                size = 8,
                                value = category,
                                italic = True,
                                offset = (-1, 0),
                            ),
                            self.delete_button
                        ],
                        alignment = MainAxisAlignment.END,
                    ),
                    Row(
                        [
                            Text(
                                size = 16,
                                value = title,
                                weight = FontWeight.W_700,
                            ),

                        ],
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ResponsiveRow(
                        [
                            Text(template_text)
                        ]
                    ),
                ]
            ),
            padding = 10,
        )
        self.data = {
            "template_id": id_str,
            "template_category": category,
            "template_title": title,
            "template_text": template_text,
        }


    def build(self):
        return self
