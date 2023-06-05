import flet as ft


class ToggleThemeAppBarButton(ft.IconButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon = ft.icons.DARK_MODE
        self.selected_icon = ft.icons.LIGHT_MODE
        self.tooltip = 'Toggle Theme'
