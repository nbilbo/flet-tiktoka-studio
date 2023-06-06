from app.ui.views.general import DefaultGeneralView


class SettingsView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/settings'
        self.title_text.value = 'Settings'
        self.navbar.focus_button(self.navbar.settings_button)
