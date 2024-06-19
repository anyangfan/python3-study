# templates.py

import fileinput, re

# Matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')

# We'll collect variables in this:
scope = {}

# This is used in re.sub:
def replacement(match):
    code = match.group(1)
    try:
        # If the field can be evaluated, return it:
        return str(eval(code, scope))
    except SyntaxError:
        # Otherwise, execute the assignment in the same scope ...
        exec code in scope
        # ... and return an empty string:
        return ''

# Get all the text as a single string:

# (There are other ways of doing this; see Chapter 11)在print(field_pat.sub(replacement, text))中,replacement函数作为参数传递给sub方法时,sub方法会自动将匹配到的内容作为参数传递给replacement函数。因此,在replacement函数内部可以通过match.group(1)来获取匹配到的内容,而不需要在函数定义时显式声明match参数。
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

# Substitute all the occurrences of the field pattern:
print(field_pat.sub(replacement, text))
'''
在print(field_pat.sub(replacement, text))中,
replacement函数作为参数传递给sub方法时,sub方法会自动将匹配到的内容作为参数传递给replacement函数。
因此,在replacement函数内部可以通过match.group(1)来获取匹配到的内容,而不需要在函数定义时显式声明match参数。
'''