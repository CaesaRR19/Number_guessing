class Chest:
    def __init__(self) -> None:
        self.time = 60

    def substract_time(self, time: int):
        self.time -= time

    def check_time(self):
        if self.time <= 0:
            return "The treasure is gone, rascal. Good luck next time hahahaha!"
