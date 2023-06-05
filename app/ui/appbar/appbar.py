import flet as ft

from app.ui.appbar.buttons import LogoutAppBarButton
from app.ui.appbar.buttons import ToggleThemeAppBarButton


class AppBar(ft.AppBar):

    def __init__(self) -> None:
        super().__init__()
        self.toolbar_height = 75
        self.leading_width = 75

        self.leading = ft.Icon()
        self.leading.name = ft.icons.APPS

        self.title = ft.Text()
        self.title.value = 'TikToka-Studio'
        self.logout_button = LogoutAppBarButton()
        self.toggle_theme_button = ToggleThemeAppBarButton()
        self.actions.append(self.toggle_theme_button)
        self.actions.append(self.logout_button)
