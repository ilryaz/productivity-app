class Notebook:
    def __init__(self, name, target_hours):
        self.name = name
        self.target_hours = target_hours
        self.current_hours = 0

    def add_hours(self, hours):
        self.current_hours += hours

    def progress(self):
        if self.target_hours == 0:
            return 100
        return (self.current_hours / self.target_hours) * 100