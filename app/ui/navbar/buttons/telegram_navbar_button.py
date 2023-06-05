import flet as ft

from app.ui.navbar.buttons import DefaultNavBarButton


class TelegramNavBarButton(DefaultNavBarButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon_content.name = ft.icons.TELEGRAM_OUTLINED
        self.selected_icon_name = ft.icons.TELEGRAM
        self.text_content.value = 'Telegram'
