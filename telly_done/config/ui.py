from textual.app import App


class ConfigApp(App):
    pass


def spawn_ui():
    app = ConfigApp()
    app.run()
