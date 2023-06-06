import flet as ft

from app.ui.appbar import AppBar
from app.ui.navbar import NavNar
from app.ui.navbar.buttons import AboutNavBarButton
from app.ui.navbar.buttons import AccountsNavBarButton
from app.ui.navbar.buttons import DiscordNavBarButton
from app.ui.navbar.buttons import HomeNavBarButton
from app.ui.navbar.buttons import SettingsNavBarButton
from app.ui.navbar.buttons import TelegramNavBarButton


class DefaultGeneralView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.padding = ft.padding.all(0)
        self.appbar = AppBar()
        self.navbar = NavNar()

        self.toggle_navbar_button = ft.IconButton()
        self.toggle_navbar_button.icon = ft.icons.ARROW_LEFT
        self.toggle_navbar_button.selected_icon = ft.icons.ARROW_RIGHT
        self.toggle_navbar_button.on_click = self.toggle_click

        self.title_text = ft.Text()
        self.title_text.value = 'Default General View'
        self.title_text.text_align = ft.TextAlign.CENTER
        self.title_text.style = ft.TextThemeStyle.TITLE_LARGE
        self.title_text.expand = True

        self.inner_content = ft.Column()
        self.inner_content.controls.append(ft.Row([self.title_text]))

        self.inner_container = ft.Container()
        self.inner_container.content = self.inner_content
        self.inner_container.padding = ft.padding.all(2)
        self.inner_container.expand = True

        content = ft.Row()
        content.controls.append(self.navbar)
        content.controls.append(self.toggle_navbar_button)
        content.controls.append(self.inner_container)
        content.vertical_alignment = ft.CrossAxisAlignment.START

        container = ft.Container()
        container.content = content
        container.padding = ft.padding.all(0)
        container.expand = True
        self.controls.append(container)

    def toggle_navbar(self) -> None:
        self.navbar.visible = not self.navbar.visible
        self.toggle_navbar_button.selected = not self.toggle_navbar_button.selected
        self.update()

    def toggle_click(self, _event: ft.ControlEvent) -> None:
        self.toggle_navbar()

    @property
    def home_button(self) -> HomeNavBarButton:
        return self.navbar.home_button

    @property
    def accounts_button(self) -> AccountsNavBarButton:
        return self.navbar.accounts_button

    @property
    def telegram_button(self) -> TelegramNavBarButton:
        return self.navbar.telegram_button

    @property
    def discord_button(self) -> DiscordNavBarButton:
        return self.navbar.discord_button

    @property
    def settings_button(self) -> SettingsNavBarButton:
        return self.navbar.settings_button

    @property
    def about_button(self) -> AboutNavBarButton:
        return self.navbar.about_button

    def get_appbar(self) -> AppBar:
        return self.appbar

    @ft.View.appbar.getter
    def appbar(self) -> AppBar:
        return super().appbar
