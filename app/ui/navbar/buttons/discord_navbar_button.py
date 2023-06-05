import flet as ft

from app.ui.navbar.buttons import DefaultNavBarButton


class DiscordNavBarButton(DefaultNavBarButton):
    def __init__(self) -> None:
        super().__init__()
        self.selected_icon_name = ft.icons.DISCORD
        self.icon_content.name = ft.icons.DISCORD_OUTLINED
        self.text_content.value = 'Discord'
