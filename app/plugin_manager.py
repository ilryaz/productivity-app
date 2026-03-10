class BasePlugin:
    name = "Base"

    def create_page(self):
        raise NotImplementedError