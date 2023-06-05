from app.ui.views.general import DefaultGeneralView


class DiscordView(DefaultGeneralView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/discord'
        self.navbar.focus_button(self.navbar.discord_button)
