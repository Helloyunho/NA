import sys
import re


def convert_to_python(x):
    with open(x, 'r', 1, 'utf8') as w:
        file_value = w.read()

    var_assign = re.compile(r'^안해$')
    create_function = re.compile(r'^안해해$')
    use_if = re.compile(r'^안안해$')

    file_value = re.sub(var_assign, '=', file_value)
    file_value = re.sub(create_function, 'def', file_value)
    file_value = re.sub(use_if, 'if', file_value)

    exec(file_value)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        convert_to_python(sys.argv[1])
    else:
        raise Exception('저기요 파일 이름을 안 넣었지 않습니까')