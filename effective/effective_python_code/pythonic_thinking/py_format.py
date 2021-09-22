"""
This file will dedicated to the illustration of Python string formatting.
Formatting is the process of combining predefined text with data values into a single human-readable message that's
stored as a string.
Python has 4 different ways of formatting strings.
1. Approach one, C-Style formatting. Initial style
  The reason this approach is called C-Style formatting is because it is borrowed from the C programming language.
  To get started with this approach, we need to use the %. The most common two are %d, %s, %f
2. Approach two, similar to c style, but with dict
3. format built-in and str.format
  Python 3 added the support of advanced string formatting that is more expressive than the old-styled C formatting.
  By using this approach, Python users can get rid of the % formatting. Extremely powerful. It also brings some extra
  complexity when formatting the string.

4. Interpolated format strings - f-strings, is added in Python 3.6
Assume key and value are all Python variables.
key = "Variable"
value = 100.0 # float
f_string: str = f'{key:<10} = {value:.2f}'
c_style_tuple: str = '%-10s = %.2f' % (key, value)
c_style_dict: str = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
str_format: str = '{:<10} = {:.2f}'.format(key, value)
str_kw_format: str = '{key:<10}:{value:.2f}'.format(key=key, value=value) # keyword approach

Homework: practice formatting, especially with {:<space_num} {:>space_num}
"""


def c_style_formatting():
    age: int = 25
    name: str = 'albert'
    score: float = 77.77
    # {name} is {age} years old and he had got {score} in this test
    # In this print, the sequence of formatted parameter is important
    print('%s is %d years old and he had got %f in this test' % (name, age, score))
    # By replacing the tuple with dict, the sequence or order of the formatted parameter is not important any more
    print('%(name)s is %(age)d years old and he had got %(score)f in this test' % {
        'name': name,
        'score': score,
        'age': age
    })
    # issue 1
    # print(f'{name} likes food and {name} loves to cook, also {name} loves to play piano')
    print('%s likes food and %s loves to cook, also %s loves to play piano' % (name, name, name))  # tuple style
    # possible solution
    print('%(name)s likes food and %(name)s loves to cook, also %(name)s loves to play piano' % {'name': name})  # dict

    template_str: str = '%s is having a Python class' % name
    template_str_2: str = '%(student_name)s is having a Python class' % {'student_name': name}
    # so do template_str and template_str_2 equal -> same value, not same object
    if template_str == template_str_2:
        print('the two formatting will have the same formatted str')
    else:
        print('thw two formatting will have different formatted str')


def built_in_format():
    # we get started with the built in format
    pi: float = 3.141592653
    # the . here is still the c formatting
    print(format(pi, '.5f'))
    key: str = 'my variable'
    secret: float = 1.23456
    # The {key} is {secret}
    # Note: adjust string position {} + : + > or < + space_number
    print('The {:<15} -> {:>15}'.format(key, secret))  # super easy to understand
    print('The %-15s -> %15f' % (key, secret))
    print('The %(key)-15s -> %(secret)15f' % {'key': key, 'secret': secret})
    # What we initially use
    print(f'The {key} -> {secret}')


def conclusion():
    key = "Variable"
    value = 100.0  # float
    #  this is not human language, not python at all
    f_string: str = f'{key:<10} = {value:<10.3f}'
    c_style_tuple: str = '%-10s = %-10.3f' % (key, value)
    c_style_dict: str = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}
    str_format: str = '{:<10} = {:.2f}'.format(key, value)
    str_kw_format: str = '{key:<10} = {value:.2f}'.format(key=key, value=value)  # keyword approach
    print(f_string)
    print(c_style_tuple)
    print(c_style_dict)
    print(str_format)
    print(str_kw_format)


if __name__ == '__main__':
    # c_style_formatting()
    built_in_format()
    conclusion()
