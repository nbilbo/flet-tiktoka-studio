from typing import List

import flet as ft

from app.ui.components import NavBarButton


class NavNar(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.home_button = NavBarButton()
        self.home_button.text_content.value = 'Home'
        self.home_button.icon_content.name = ft.icons.HOME_OUTLINED
        self.home_button.selected_icon_name = ft.icons.HOME
        self.home_button.expand = True

        self.accounts_button = NavBarButton()
        self.accounts_button.text_content.value = 'Home'
        self.accounts_button.icon_content.name = ft.icons.GROUP_OUTLINED
        self.accounts_button.selected_icon_name = ft.icons.GROUP
        self.accounts_button.expand = True

        self.telegram_button = NavBarButton()
        self.telegram_button.text_content.value = 'Telegram'
        self.telegram_button.icon_content.name = ft.icons.TELEGRAM_OUTLINED
        self.telegram_button.selected_icon_name = ft.icons.TELEGRAM
        self.telegram_button.expand = True

        self.discord_button = NavBarButton()
        self.discord_button.text_content.value = 'Discord'
        self.discord_button.icon_content.name = ft.icons.DISCORD_OUTLINED
        self.discord_button.selected_icon_name = ft.icons.DISCORD
        self.discord_button.expand = True

        self.settings_button = NavBarButton()
        self.settings_button.text_content.value = 'Settings'
        self.settings_button.icon_content.name = ft.icons.SETTINGS_OUTLINED
        self.settings_button.selected_icon_name = ft.icons.SETTINGS
        self.settings_button.expand = True

        self.about_button = NavBarButton()
        self.about_button.text_content.value = 'About'
        self.about_button.icon_content.name = ft.icons.INFO_OUTLINE
        self.about_button.selected_icon_name = ft.icons.INFO
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
    def focus_button(button: NavBarButton) -> None:
        button.arrow_icon_content.visible = True
        button.icon_content.name = button.selected_icon_name
        button.text_content.weight = ft.FontWeight.BOLD
        button.icon_content.size = 35

    def get_navbar_buttons(self) -> List[NavBarButton]:
        return [
            self.home_button,
            self.accounts_button,
            self.telegram_button,
            self.discord_button,
            self.settings_button,
            self.about_button
        ]
