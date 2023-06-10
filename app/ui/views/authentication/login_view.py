import flet as ft

from app.ui.views.authentication import DefaultAuthenticationView


class LoginView(DefaultAuthenticationView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/authentication/login'
        self.title.value = 'Login'

        self.username_field = ft.TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = ft.TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.login_button = ft.OutlinedButton()
        self.login_button.text = 'Login'
        self.login_button.icon = ft.icons.LOGIN_OUTLINED
        self.login_button.style = ft.ButtonStyle()
        self.login_button.style.shape = ft.RoundedRectangleBorder(radius=2)
        self.login_button.expand = True

        self.dont_have_account_button = ft.OutlinedButton()
        self.dont_have_account_button.text = 'Don\'t have an account? Sign up'
        self.dont_have_account_button.icon = ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT
        self.dont_have_account_button.style = ft.ButtonStyle()
        self.dont_have_account_button.style.shape = ft.RoundedRectangleBorder(radius=2)
        self.dont_have_account_button.style.side = ft.BorderSide(0, ft.colors.TRANSPARENT)
        self.dont_have_account_button.expand = True

        self.content.controls.append(ft.Row([self.username_field]))
        self.content.controls.append(ft.Row([self.password_field]))
        self.content.controls.append(ft.Row([self.login_button]))
        self.content.controls.append(ft.Row([self.dont_have_account_button]))
