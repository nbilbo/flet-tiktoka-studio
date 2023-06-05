import flet as ft


class LogoutAppBarButton(ft.IconButton):
    def __init__(self) -> None:
        super().__init__()
        self.icon = ft.icons.LOGOUT_OUTLINED
        self.tooltip = 'Logout'
