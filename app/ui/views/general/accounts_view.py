from app.ui.views.general import DefaultGeneralView


class AccountsView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/accounts'
        self.navbar.focus_button(self.navbar.accounts_button)
