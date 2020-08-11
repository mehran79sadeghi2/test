def get_full_name(name, last, middle = ''):
    if middle:
        return (name + ' ' + middle + ' ' + last).title()
    else:
        return (name + ' ' + last).title()