import flet as ft

from app.ui.navbar.buttons import DefaultNavBarButton


class AboutNavBarButton(DefaultNavBarButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon_content.name = ft.icons.INFO_OUTLINE
        self.selected_icon_name = ft.icons.INFO
        self.text_content.value = 'About'
