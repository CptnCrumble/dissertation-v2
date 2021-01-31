import validation

class Patient:
    def __init__(self, pid, gender, diagnosis, depi ):
        self.pid = pid
        self.gender = gender
        self.diagnosis = diagnosis
        self.deprivation_index = depi
    
    pdq8_scores = []
    def add_pdq8(self, pdq8_result):
        if validation.pid_check(self.pid, pdq8_result):
            self.pdq8_scores.append(pdq8_result)

