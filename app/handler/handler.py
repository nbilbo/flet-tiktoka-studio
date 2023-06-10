from __future__ import annotations

from typing import TYPE_CHECKING

import flet as ft

if TYPE_CHECKING:
    from app.ui import Application
    from app.ui.views.authentication import LoginView
    from app.ui.views.authentication import RegisterView
    from app.ui.views.general import DefaultGeneralView


class Handler:
    def __init__(self, application: Application) -> None:
        self.application = application
        self.__bind_default_general_view(self.application.home_view)
        self.__bind_default_general_view(self.application.accounts_view)
        self.__bind_default_general_view(self.application.telegram_view)
        self.__bind_default_general_view(self.application.discord_view)
        self.__bind_default_general_view(self.application.settings_view)
        self.__bind_default_general_view(self.application.about_view)
        self.__bind_login_view(self.application.login_view)
        self.__bind_register_view(self.application.register_view)

    def __bind_default_general_view(self, view: DefaultGeneralView) -> None:
        view.home_button.on_click = self.__home_navbar_click
        view.accounts_button.on_click = self.__accounts_navbar_click
        view.telegram_button.on_click = self.__telegram_navbar_click
        view.discord_button.on_click = self.__discord_navbar_click
        view.settings_button.on_click = self.__settings_navbar_click
        view.about_button.on_click = self.__about_navbar_click
        view.appbar.logout_button.on_click = self.__logout_appbar_click
        view.appbar.toggle_theme_button.on_click = self.__toggle_theme_appbar_click
        view.toggle_navbar_button.on_click = self.__toggle_navbar_click

    def __bind_login_view(self, view: LoginView) -> None:
        view.login_button.on_click = self.__login_click
        view.dont_have_account_button.on_click = self.__dont_have_account_click

    def __bind_register_view(self, view: RegisterView) -> None:
        view.register_button.on_click = self.__register_click
        view.already_have_account_button.on_click = self.__already_have_account_click

    def __home_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_home_view()

    def __accounts_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_accounts_view()

    def __telegram_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_telegram_view()

    def __discord_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_discord_view()

    def __settings_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_settings_view()

    def __about_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_about_view()

    def __logout_appbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_login_view()

    def __toggle_theme_appbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.toggle_theme()

    def __login_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_home_view()

    def __register_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_home_view()

    def __dont_have_account_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_register_view()

    def __already_have_account_click(self, _event: ft.ControlEvent) -> None:
        self.application.go_login_view()

    def __toggle_navbar_click(self, _event: ft.ControlEvent) -> None:
        self.application.toggle_navbar()
