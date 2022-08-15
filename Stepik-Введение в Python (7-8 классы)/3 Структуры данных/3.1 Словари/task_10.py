'''
Телефонная книга. Этап 3
    Коле очень понравилась Ваша программа, однако он стал замечать, что иногда в его телефонную книгу попадают номера в некорректном формате. Чтобы не сохранять недействительные номера, он попросил Вас обрабатывать только номера, соответствующие критериям:

номер должен начинаться либо с +7, либо с 8 и состоять из 11 цифр.

блоки цифр могут разделяться пробелами или дефисами.

вторая, третья и четвертая цифры могут помещаться в скобки.

    Если программа встречает некорректный номер, она должна его проигнорировать. В обратном случае она должна привести номер к виду +7 (900) 800-70-60 и запомнить. Остальной функционал программы остается без изменений.'''


def convert_phone_number(phone: str) -> str:
    # номер должен начинаться либо с +7, либо с 8
    if not (phone.startswith('+7') or phone.startswith('8')):
        return ''

    # убираем пробелы

    clean_format = phone.replace('+', '')

    if len(clean_format) == 11:
        return f"+7 ({clean_format[1:4]}) {clean_format[4:7]}-{clean_format[7:9]}-{clean_format[9:]}"
    else:
        return ''


dict_phone = {}
list_phone = []
while True:
    s = input()
    if s == '.':
        break

    # вычленяем имя
    pos = s.find(' ')
    if pos == -1:  # пробел не найден
        name = s
        if dict_phone.get(name, 0) == 0 or dict_phone[name] == []:
            print("Не найдено")
        else:
            print(*dict_phone[name], sep=', ')
    else:
        name = s[:pos]
        other = s[pos + 1:]

        clean_format = other.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        arr = clean_format.split(',')

        if len(arr) > 0:
            list_phone = [convert_phone_number(item) for item in arr]
            list_phone = list(filter(None, list_phone))
            dict_phone[name] = dict_phone.get(name, []) + list_phone
