# numberlines.py

import fileinput

for line in fileinput.input(inplace=True):
    '''
    这段代码使用了fileinput模块,它可以从文件中读取内容,并且可以处理多个输入流。
    当你在命令行中运行python numberlines.py file1时,file1会被作为输入流传递给fileinput.input()函数。
    因此,在代码中的for循环中,可以通过fileinput.input()获取到文件名参数,然后对文件中的每一行进行处理。
    '''
    line = line.rstrip()
    #line.rstrip()是对当前行的字符串进行去除末尾的换行符操作,确保输出时不会有多余的空行。
    num  = fileinput.lineno()
    print('{:<110} # {:2d}'.format(line, num))
    '''
    '{:<50} # {:2d}'.format(line, num)是一个字符串格式化操作,其中：
    - '<50'表示左对齐,总宽度为50个字符
    - '# {:2d}'表示输出一个#符号和一个整数,总宽度为2个字符
    - format(line, num)将line和num的值填入格式化字符串中,并输出。
    '''