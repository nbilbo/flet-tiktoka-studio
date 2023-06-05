import flet as ft

from app.ui.navbar.buttons import DefaultNavBarButton


class AccountsNavBarButton(DefaultNavBarButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon_content.name = ft.icons.GROUP_OUTLINED
        self.selected_icon_name = ft.icons.GROUP
        self.text_content.value = 'Accounts'
