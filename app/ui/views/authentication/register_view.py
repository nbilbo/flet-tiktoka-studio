import flet as ft

from app.ui.views.authentication import DefaultAuthenticationView


class RegisterView(DefaultAuthenticationView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/authentication/register'
        self.title.value = 'Register'

        self.username_field = ft.TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = ft.TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.register_button = ft.OutlinedButton()
        self.register_button.text = 'Register'
        self.register_button.icon = ft.icons.SAVE_OUTLINED
        self.register_button.style = ft.ButtonStyle()
        self.register_button.style.shape = ft.RoundedRectangleBorder(radius=2)
        self.register_button.expand = True

        self.already_have_account_button = ft.OutlinedButton()
        self.already_have_account_button.text = 'Already have an account? Sign in'
        self.already_have_account_button.icon = ft.icons.KEYBOARD_DOUBLE_ARROW_LEFT
        self.already_have_account_button.style = ft.ButtonStyle()
        self.already_have_account_button.style.shape = ft.RoundedRectangleBorder(radius=2)
        self.already_have_account_button.style.side = ft.BorderSide(0, ft.colors.TRANSPARENT)
        self.already_have_account_button.expand = True

        self.content.controls.append(ft.Row([self.username_field]))
        self.content.controls.append(ft.Row([self.password_field]))
        self.content.controls.append(ft.Row([self.register_button]))
        self.content.controls.append(ft.Row([self.already_have_account_button]))
