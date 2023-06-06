from app.ui.views.general import DefaultGeneralView


class HomeView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/home'
        self.title_text.value = 'Home'
        self.navbar.focus_button(self.navbar.home_button)
