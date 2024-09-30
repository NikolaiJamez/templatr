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

class Template(Card):

    def __init__(self):
        super().__init__(col = {"md": 5, "lg": 4})
        self.content = Container(
            content = Column(
                [
                    Row(
                        [
                            Text(
                                opacity = 0.5,
                                size = 8,
                                value = "Category",
                                italic = True,
                            ),
                            IconButton(
                                height = 32,
                                icon = icons.CLOSE,
                                icon_color = colors.RED,
                                icon_size = 16,
                                visible = False,
                                width = 32)
                        ],
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    Row(
                        [
                            Text(
                                size = 16,
                                value = "Title Text",
                                weight = FontWeight.W_700,
                            ),

                        ],
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ResponsiveRow(
                        [
                            Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae velit massa. Proin tempus placerat nunc, et dignissim odio lacinia at. Donec fermentum luctus ante nec pulvinar.")
                        ]
                    ),
                ]
            ),
            padding = 10,
        )
        self.col = {"md": 5, "lg": 4}


    def build(self):
        return self



# ft.Card(
#                 content = ft.Container(
#                     content = ft.Column(
#                         [
#                             ft.Row(
#                                 [
#                                     ft.Text(
#                                         opacity = 0.5,
#                                         size = 8,
#                                         value = "Category",
#                                         italic = True,
#                                     ),
#                                     ft.IconButton(
#                                         height = 32,
#                                         icon = ft.icons.CLOSE,
#                                         icon_color = ft.colors.RED,
#                                         icon_size = 16,
#                                         visible = False,
#                                         width = 32)
#                                 ],
#                                 alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
#                             ),
#                             ft.Row(
#                                 [
#                                     ft.Text(
#                                         size = 16,
#                                         value = "Title Text",
#                                         weight = ft.FontWeight.W_700,
#                                     ),
#
#                                 ],
#                                 alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
#                             ),
#                             ft.ResponsiveRow([ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae velit massa. Proin tempus placerat nunc, et dignissim odio lacinia at. Donec fermentum luctus ante nec pulvinar.")]),
#                         ]
#                     ),
#                     padding = 10,
#                 ),
#                 col = {"md": 5, "lg": 4}
#             )