class Cell:
    def __init__(self):
        self.isAlive = False

    def set_alive(self):

        if self.isAlive:
            return False

        self.isAlive = True
        return True

    def set_dead(self):

        if not self.isAlive:
            return False

        self.isAlive = False
        return True

    def is_alive(self):
        return self.isAlive

    def get_print_character(self):
        return '█' if self.isAlive else ' '
