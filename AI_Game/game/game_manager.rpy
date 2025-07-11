init python:
    class GameManager:
        def __init__(self):
            self.company_stats = [50, 50, 50, 50, 50] # People. Process, Tech, Policy, Impact.
            self.boss_satisfaction = 50
            self.coworker_relationship = 50
            self.company_money = 250
        
        def update_scores(self, p, pr, t, po, i):
            self.company_stats[0] += p
            self.company_stats[1] += pr
            self.company_stats[2] += t
            self.company_stats[3] += po
            self.company_stats[4] += i
        
        def evaluate_ending(self):
            local_scores = []
            for stat in self.company_stats:
                local_scores.append(self.evaluate_score(stat))
            return local_scores
        
        def evaluate_score(self, score):
            if score <= 30:
                return "Poor"
            elif score <= 60:
                return "Fair"
            elif score <= 80:
                return "Good"
            else:
                return "Excellent"