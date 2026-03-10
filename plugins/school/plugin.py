from .page import SchoolPage


class SchoolPlugin:
    name = "School"

    def create_page(self):
        return SchoolPage()