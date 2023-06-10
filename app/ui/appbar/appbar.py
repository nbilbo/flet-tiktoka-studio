import flet as ft


class AppBar(ft.AppBar):

    def __init__(self) -> None:
        super().__init__()
        self.toolbar_height = 75
        self.leading_width = 75

        self.leading = ft.Icon()
        self.leading.name = ft.icons.APPS

        self.title = ft.Text()
        self.title.value = 'TikToka-Studio'

        self.logout_button = ft.IconButton()
        self.logout_button.icon = ft.icons.LOGOUT_OUTLINED
        self.logout_button.tooltip = 'Logout'

        self.toggle_theme_button = ft.IconButton()
        self.toggle_theme_button.icon = ft.icons.DARK_MODE
        self.toggle_theme_button.selected_icon = ft.icons.LIGHT_MODE
        self.toggle_theme_button.tooltip = 'Toggle Theme'

        self.actions.append(self.toggle_theme_button)
        self.actions.append(self.logout_button)
