username_rule = "仅包含字母数字或下划线，长度在[3, 14]之间"
password_rule = "仅包含字母数字下划线或#*&，长度在[8, 14]之间"

def add_format_info(data):
    data['username_rule'] = username_rule
    data['password_rule'] = password_rule
    return data