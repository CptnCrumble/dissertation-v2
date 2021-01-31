def pid_check(real_pid,data):
    try:
        if real_pid == data["pid"]:
            return True
        else:
            return False
    except:
        return False

def pdq8(data):
    try:
        if len(data) != 11:
            return False            
        elif [*data] != ['pid', 'ass_num', 'ass_date', 'PDQ1', 'PDQ2', 'PDQ3', 'PDQ4', 'PDQ5', 'PDQ6', 'PDQ7', 'PDQ8']:
            return False
        else:
            return True
    except:
        return False