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
        elif set(data.keys()) != {'pid', 'ass_num', 'ass_date', 'PDQ1', 'PDQ2', 'PDQ3', 'PDQ4', 'PDQ5', 'PDQ6', 'PDQ7', 'PDQ8'}:
            log.info('invalid pdq8 data: keys dont match')
            return False
        else:
            return True
    except:
        return False