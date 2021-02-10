def check_email(string):
    if " " not in string and '@' in string and '@.' not in string:
        if string.rfind('.') > string.find('@') + 1:
            return True

    return False

words = input().split()

websites = [word for word in words if word.lower().startswith(('https://', 'http://', 'www.'))]
print('\n'.join(websites))
