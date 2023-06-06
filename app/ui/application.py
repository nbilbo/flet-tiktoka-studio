from typing import List

import flet as ft

from app.handler import Handler
from app.ui.views.authentication import LoginView
from app.ui.views.authentication import RegisterView
from app.ui.views.general import AboutView
from app.ui.views.general import AccountsView
from app.ui.views.general import DefaultGeneralView
from app.ui.views.general import DiscordView
from app.ui.views.general import HomeView
from app.ui.views.general import SettingsView
from app.ui.views.general import TelegramView


class Application:
    def __init__(self, page: ft.Page) -> None:
        # page settings.
        self.page = page
        self.page.on_route_change = self.__route_change
        self.page.theme = ft.Theme()

        # views.
        self.login_view = LoginView()
        self.register_view = RegisterView()
        self.home_view = HomeView()
        self.accounts_view = AccountsView()
        self.telegram_view = TelegramView()
        self.discord_view = DiscordView()
        self.settings_view = SettingsView()
        self.about_view = AboutView()

        # settings widgets events.
        self.handler = Handler(self)

        # initial state.
        self.__set_page_transition(ft.PageTransitionTheme.NONE)
        self.active_dark_theme()
        self.gray_colors_scheme()
        self.go_accounts_view()

    def __route_change(self, *_args) -> None:
        template_route = ft.TemplateRoute(self.page.route)
        self.page.views.clear()

        if template_route.match(self.home_view.route):
            self.page.views.append(self.home_view)

        elif template_route.match(self.accounts_view.route):
            self.page.views.append(self.accounts_view)

        elif template_route.match(self.telegram_view.route):
            self.page.views.append(self.telegram_view)

        elif template_route.match(self.discord_view.route):
            self.page.views.append(self.discord_view)

        elif template_route.match(self.login_view.route):
            self.page.views.append(self.login_view)

        elif template_route.match(self.register_view.route):
            self.page.views.append(self.register_view)

        elif template_route.match(self.settings_view.route):
            self.page.views.append(self.settings_view)

        elif template_route.match(self.about_view.route):
            self.page.views.append(self.about_view)

    def __set_page_transition(self, transition: ft.PageTransitionTheme) -> None:
        self.page.theme.page_transitions.linux = transition
        self.page.theme.page_transitions.macos = transition
        self.page.theme.page_transitions.windows = transition
        self.page.theme.page_transitions.ios = transition
        self.page.theme.page_transitions.android = transition

    def __get_general_views(self) -> List[DefaultGeneralView]:
        return [
            self.home_view,
            self.accounts_view,
            self.telegram_view,
            self.discord_view,
            self.settings_view,
            self.about_view
        ]

    def __set_appbar_toggle_theme_selected(self, selected: bool) -> None:
        for view in self.__get_general_views():
            view.get_appbar().toggle_theme_button.selected = selected

    def __set_appbar_background_color(self, color: str) -> None:
        for view in self.__get_general_views():
            view.get_appbar().bgcolor = color

    def __set_appbar_foreground_color(self, color: str) -> None:
        for view in self.__get_general_views():
            view.get_appbar().title.color = color
            view.get_appbar().leading.color = color

            view.get_appbar().toggle_theme_button.icon_color = color
            view.get_appbar().toggle_theme_button.selected_icon_color = color

            view.get_appbar().logout_button.icon_color = color
            view.get_appbar().logout_button.selected_icon_color = color

    def __set_navbar_background_color(self, color: str) -> None:
        for view in self.__get_general_views():
            view.navbar.container.bgcolor = color

    def __set_navbar_foreground_color(self, color: str) -> None:
        for view in self.__get_general_views():
            for button in view.navbar.get_navbar_buttons():
                button.icon_content.color = color
                button.text_content.color = color
                button.arrow_icon_content.color = color

    def __set_navbar_border_color(self, color: str) -> None:
        for view in self.__get_general_views():
            view.navbar.container.border = ft.border.only(right=ft.BorderSide(5, color))

    def __set_toggle_navbar_background_color(self, color: str) -> None:
        for view in self.__get_general_views():
            view.toggle_navbar_button.bgcolor = color

    def __set_toggle_navbar_foreground_color(self, color: str) -> None:
        for view in self.__get_general_views():
            view.toggle_navbar_button.icon_color = color
            view.toggle_navbar_button.selected_icon_color = color

    def go_home_view(self) -> None:
        self.page.go(self.home_view.route)

    def go_accounts_view(self) -> None:
        self.page.go(self.accounts_view.route)

    def go_telegram_view(self) -> None:
        self.page.go(self.telegram_view.route)

    def go_discord_view(self) -> None:
        self.page.go(self.discord_view.route)

    def go_login_view(self) -> None:
        self.page.go(self.login_view.route)

    def go_register_view(self) -> None:
        self.page.go(self.register_view.route)

    def go_settings_view(self) -> None:
        self.page.go(self.settings_view.route)

    def go_about_view(self) -> None:
        self.page.go(self.about_view.route)

    def active_light_theme(self) -> None:
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.__set_appbar_toggle_theme_selected(False)
        self.page.update()

    def active_dark_theme(self) -> None:
        self.page.theme_mode = ft.ThemeMode.DARK
        self.__set_appbar_toggle_theme_selected(True)
        self.page.update()

    def blue_colors_scheme(self) -> None:
        self.__set_appbar_background_color('#0554F2')
        self.__set_appbar_foreground_color('#ffffff')

        self.__set_navbar_background_color('#056CF2')
        self.__set_navbar_foreground_color('#ffffff')
        self.__set_navbar_border_color('#0554F2')

        self.__set_toggle_navbar_background_color('#056CF2')
        self.__set_toggle_navbar_foreground_color('#ffffff')

    def gray_colors_scheme(self) -> None:
        self.__set_appbar_background_color('#0D0D0D')
        self.__set_appbar_foreground_color('#ffffff')
        
        self.__set_navbar_background_color('#F2F2F2')
        self.__set_navbar_foreground_color('#0D0D0D')
        self.__set_navbar_border_color('F2F2F2')

        self.__set_toggle_navbar_background_color('#F2F2F2')
        self.__set_toggle_navbar_foreground_color('#0D0D0D')

    def fashion_colors_scheme(self) -> None:
        self.__set_appbar_background_color('#D92534')
        self.__set_appbar_foreground_color('#ffffff')

        self.__set_navbar_background_color('#0F1926')
        self.__set_navbar_foreground_color('#ffffff')
        self.__set_navbar_border_color('#D9B64E')
        
        self.__set_toggle_navbar_background_color('#0F1926')
        self.__set_toggle_navbar_foreground_color('#ffffff')
        
    def toggle_theme(self) -> None:
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.active_light_theme()

        elif self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.active_dark_theme()
