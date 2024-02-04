from stack import Stack


def check_balance_brackets(data_list):
    stack = Stack()
    for item in data_list:
        if item in '([{':
            stack.push(item)
        else:
            if stack.is_empty():
                return False
            else:
                if stack.peek() + item in ('()', '[]', '{}'):
                    stack.pop()
                else:
                    return False

    return stack.is_empty() or False


def main(*balanced):
    for balans in balanced:
        print(f"Сбалансированно: {balans}") if check_balance_brackets(balans) \
            else print(f"Неcбалансированно: {balans}")


if __name__ == '__main__':

    test_list = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '{{[(])]}}',
        '{[}]'
        ]

    main(*test_list)

