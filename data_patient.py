from data_validation import *

class Patient:
    def __init__(self, pid, gender, diagnosis, depi ):
        self.pid = pid
        self.gender = gender
        self.diagnosis = diagnosis
        self.deprivation_index = depi
    
    pdq8_scores = []
    pdq39_scores = []
    hads_scores = []

    def add_pdq8(self, pdq8_result):
        if pid_check(self.pid, pdq8_result) & validate_pdq8(pdq8_result):
            self.pdq8_scores.append(pdq8_result)

    def add_pdq39(self,pdq39_result):
        if pid_check(self.pid, pdq39_result) & validate_pdq39(pdq39_result):
            self.pdq39_scores.append(pdq39_result)

    def add_hads(self,hads_result):
        if pid_check(self.pid, hads_result) & validate_hads(hads_result):
            self.hads_scores.append(hads_result)

