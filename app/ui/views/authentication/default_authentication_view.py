import flet as ft


class DefaultAuthenticationView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.title = ft.Text()
        self.title.text_align = ft.TextAlign.CENTER
        self.title.expand = True

        self.username_field = ft.TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = ft.TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.content = ft.Column()
        self.content.width = 500
        self.content.alignment = ft.MainAxisAlignment.CENTER
        self.content.controls.append(ft.Row([self.title]))
        self.content.controls.append(ft.Row([self.username_field]))
        self.content.controls.append(ft.Row([self.password_field]))

        container = ft.Container()
        container.content = self.content
        container.padding = ft.padding.all(5)
        self.controls.append(container)
