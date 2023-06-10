import flet as ft


class NavBarButton(ft.OutlinedButton):
    def __init__(self) -> None:
        super().__init__()

        self.style = ft.ButtonStyle()
        self.style.shape = ft.RoundedRectangleBorder(radius=0)
        self.style.side = ft.BorderSide(width=0, color=ft.colors.TRANSPARENT)

        self.arrow_icon_content = ft.Icon()
        self.arrow_icon_content.name = ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_SHARP
        self.arrow_icon_content.visible = False

        self.selected_icon_name: str = ''
        self.icon_content = ft.Icon()
        self.text_content = ft.Text()

        content = ft.Row()
        content.controls.append(self.arrow_icon_content)
        content.controls.append(self.icon_content)
        content.controls.append(self.text_content)
        self.content = content
