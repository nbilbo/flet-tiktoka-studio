import flet as ft

from app.ui.appbar import AppBar
from app.ui.components import NavBarButton
from app.ui.navbar import NavNar


class DefaultGeneralView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.padding = ft.padding.all(0)
        self.appbar = AppBar()
        self.navbar = NavNar()

        self.toggle_navbar_button = ft.IconButton()
        self.toggle_navbar_button.icon = ft.icons.ARROW_LEFT
        self.toggle_navbar_button.selected_icon = ft.icons.ARROW_RIGHT

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

    @property
    def home_button(self) -> NavBarButton:
        return self.navbar.home_button

    @property
    def accounts_button(self) -> NavBarButton:
        return self.navbar.accounts_button

    @property
    def telegram_button(self) -> NavBarButton:
        return self.navbar.telegram_button

    @property
    def discord_button(self) -> NavBarButton:
        return self.navbar.discord_button

    @property
    def settings_button(self) -> NavBarButton:
        return self.navbar.settings_button

    @property
    def about_button(self) -> NavBarButton:
        return self.navbar.about_button

    def get_appbar(self) -> AppBar:
        return self.appbar

    @ft.View.appbar.getter
    def appbar(self) -> AppBar:
        return super().appbar
