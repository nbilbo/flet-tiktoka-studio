import flet as ft

from app.ui.navbar.buttons import DefaultNavBarButton


class HomeNavBarButton(DefaultNavBarButton):
    def __init__(self) -> None:
        super().__init__()
        self.selected_icon_name = ft.icons.HOME
        self.icon_content.name = ft.icons.HOME_OUTLINED
        self.text_content.value = 'Home'
