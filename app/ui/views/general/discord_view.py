from app.ui.views.general import DefaultGeneralView


class DiscordView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/discord'
        self.title_text.value = 'Discord'
        self.navbar.focus_button(self.navbar.discord_button)
