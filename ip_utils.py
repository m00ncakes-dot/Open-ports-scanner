def is_valid_ip(word):
    parts = word.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if not (0 <= int(part) <= 255):
            return False

    return True


def get_ips(text):
    ips = []
    for word in text.split():
        if is_valid_ip(word):
            ips.append(word)
    return ips