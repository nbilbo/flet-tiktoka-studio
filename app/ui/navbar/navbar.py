from typing import List

import flet as ft

from app.ui.navbar.buttons import AboutNavBarButton
from app.ui.navbar.buttons import AccountsNavBarButton
from app.ui.navbar.buttons import DefaultNavBarButton
from app.ui.navbar.buttons import DiscordNavBarButton
from app.ui.navbar.buttons import HomeNavBarButton
from app.ui.navbar.buttons import SettingsNavBarButton
from app.ui.navbar.buttons import TelegramNavBarButton


class NavNar(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.home_button = HomeNavBarButton()
        self.home_button.expand = True

        self.accounts_button = AccountsNavBarButton()
        self.accounts_button.expand = True

        self.telegram_button = TelegramNavBarButton()
        self.telegram_button.expand = True

        self.discord_button = DiscordNavBarButton()
        self.discord_button.expand = True

        self.settings_button = SettingsNavBarButton()
        self.settings_button.expand = True

        self.about_button = AboutNavBarButton()
        self.about_button.expand = True

        content = ft.Column()
        content.controls.append(ft.Row([self.home_button]))
        content.controls.append(ft.Row([self.accounts_button]))
        content.controls.append(ft.Row([self.telegram_button]))
        content.controls.append(ft.Row([self.discord_button]))
        content.controls.append(ft.Row([self.settings_button]))
        content.controls.append(ft.Row([self.about_button]))

        self.container = ft.Container()
        self.container.content = content
        self.container.border = ft.border.only(right=ft.BorderSide(5, ft.colors.BLACK))
        self.container.width = 300

    def build(self) -> ft.Container:
        return self.container

    @staticmethod
    def focus_button(button: DefaultNavBarButton) -> None:
        button.arrow_icon_content.visible = True
        button.icon_content.name = button.selected_icon_name
        button.text_content.weight = ft.FontWeight.BOLD
        button.icon_content.size = 35

    def get_navbar_buttons(self) -> List[DefaultNavBarButton]:
        return [
            self.home_button,
            self.accounts_button,
            self.telegram_button,
            self.discord_button,
            self.settings_button,
            self.about_button
        ]
