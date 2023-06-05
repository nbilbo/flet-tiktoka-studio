import flet as ft

from app.ui.views.authentication import LoginView


class RegisterView(LoginView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/authentication/register'
        self.title.value = 'Register'
        self.login_button, self.register_button = self.register_button, self.login_button

        self.register_button.text = 'Register'
        self.register_button.icon = ft.icons.APP_REGISTRATION_OUTLINED

        self.login_button.text = 'Already have an account? Login here'
        self.login_button.icon = ft.icons.KEYBOARD_DOUBLE_ARROW_LEFT
