#!/userdata/Li/miniconda3/envs/python_study/bin/python3
#python -m http.server --cgi 8000
#http://192.168.1.16:8000/cgi-bin/simple2.py
import cgitb; cgitb.enable();
import cgi
form = cgi.FieldStorage()

name = form.getvalue('name', 'world')

print('Content-type: text/plain\n')

print('Hello, {}!'.format(name))