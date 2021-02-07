import logging

log = logging.getLogger(__name__)

def pid_check(real_pid,data):
    try:
        if real_pid == data["pid"]:
            return True
        else:
            log.info('pid_check() failed')
            return False
    except:
        return False

def validate_pdq8(data):
    try:
        if len(data) != 11:
            log.info('invalid pdq8data: incorrect length')
            return False            
        elif set(data.keys()) != {'pid', 'assessment_number', 'assessment_date', 'PDQ1', 'PDQ2', 'PDQ3', 'PDQ4', 'PDQ5', 'PDQ6', 'PDQ7', 'PDQ8'}:
            log.info('invalid pdq8 data: keys dont match')
            return False
        else:
            return True
    except:
        return False

def validate_pdq39(data):
    try:
        if len(data) != 42:
            log.info('invalid pdq39data: incorrect length')
            return False            
        elif set(data.keys()) != {'pid', 'assessment_number', 'assessment_date', 'PDQ1', 'PDQ2', 'PDQ3', 'PDQ4', 'PDQ5', 'PDQ6', 'PDQ7', 'PDQ8', 'PDQ9', 'PDQ10', 'PDQ11', 'PDQ12', 'PDQ13', 'PDQ14', 'PDQ15', 'PDQ16', 'PDQ17', 'PDQ18', 'PDQ19', 'PDQ20', 'PDQ21', 'PDQ22', 'PDQ23', 'PDQ24', 'PDQ25', 'PDQ26', 'PDQ27', 'PDQ28', 'PDQ29', 'PDQ30', 'PDQ31', 'PDQ32', 'PDQ33', 'PDQ34', 'PDQ35', 'PDQ36', 'PDQ37', 'PDQ38', 'PDQ39'}:
            log.info('invalid pdq39 data: keys dont match')
            return False
        else:
            return True
    except:
        return False

def validate_hads(data):
    try:
        if len(data) != 17:
            log.info('invalid HADS result: incorrect length')
            return False            
        elif set(data.keys()) != {'pid', 'assessment_number', 'assessment_date', 'tense', 'enjoy', 'fright', 'laugh', 'worry', 'cheer', 'ease', 'slow', 'butterfly', 'interest', 'restless', 'forward', 'panic', 'book'}:
            log.info('invalid HADS data: keys dont match')
            return False
        else:
            return True
    except:
        return False