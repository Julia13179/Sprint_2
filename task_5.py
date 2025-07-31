class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
    
    
    def number_of_wins(self):
        return f"Футбольных побед:  {self.victories}"
    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"
    def number_of_losses(self):
        return f"Футбольных поражений: {self.number_of_losses}"
    def total_points(self):
        self.victories * 3 + self.draws
        return f"Общее количество очков: {self.total_points}"
    

class Hockey(Results):
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
    
    
    def number_of_wins(self):
        return f"Хоккейных побед:  {self.victories}"
    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"
    def number_of_losses(self):
        return f"Хоккейных поражений: {self.number_of_losses}"
    def total_points(self):
        self.victories * 2 + self.draws
        return f"Общее количество очков: {self.total_points}"
    