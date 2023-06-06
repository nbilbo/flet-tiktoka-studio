from app.ui.views.general import DefaultGeneralView


class AboutView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/about'
        self.title_text.value = 'About'
        self.navbar.focus_button(self.navbar.about_button)
