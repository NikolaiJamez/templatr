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

DEFAULT_COL_SIZE = {"md": 5, "lg": 4}

class Template(Card):

    def __init__(self, category: str, title: str, template_text: str):
        super().__init__(col = DEFAULT_COL_SIZE)
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
                            IconButton(
                                height = 32,
                                icon = icons.CLOSE,
                                icon_color = colors.RED,
                                icon_size = 16,
                                visible = False,
                                width = 32)
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


    def build(self):
        return self
