from app.ui.views.general import DefaultGeneralView


class TelegramView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/telegram'
        self.navbar.focus_button(self.navbar.telegram_button)
