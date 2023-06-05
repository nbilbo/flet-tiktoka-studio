import flet as ft

from app.ui.navbar.buttons import DefaultNavBarButton


class SettingsNavBarButton(DefaultNavBarButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon_content.name = ft.icons.SETTINGS_OUTLINED
        self.selected_icon_name = ft.icons.SETTINGS
        self.text_content.value = 'Settings'
