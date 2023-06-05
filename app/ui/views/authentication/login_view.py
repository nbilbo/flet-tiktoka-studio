import flet as ft

from app.ui.views.authentication import DefaultAuthenticationView


class LoginView(DefaultAuthenticationView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/authentication/login'
        self.title.value = 'Login'
        self.title.style = ft.TextThemeStyle.DISPLAY_LARGE

        self.login_button = ft.OutlinedButton()
        self.login_button.text = 'Login'
        self.login_button.icon = ft.icons.LOGIN_OUTLINED
        self.login_button.style = ft.ButtonStyle()
        self.login_button.style.shape = ft.RoundedRectangleBorder(radius=2)
        self.login_button.expand = True

        self.register_button = ft.OutlinedButton()
        self.register_button.text = 'Don\'t have an account? Register here'
        self.register_button.icon = ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT
        self.register_button.style = ft.ButtonStyle()
        self.register_button.style.shape = ft.RoundedRectangleBorder(radius=2)
        self.register_button.style.side = ft.BorderSide(0, ft.colors.TRANSPARENT)
        self.register_button.expand = True

        self.content.controls.append(ft.Row([self.login_button]))
        self.content.controls.append(ft.Row([self.register_button]))
