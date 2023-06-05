from app.ui.views.general import DefaultGeneralView


class HomeView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/home'
        self.navbar.focus_button(self.navbar.home_button)
