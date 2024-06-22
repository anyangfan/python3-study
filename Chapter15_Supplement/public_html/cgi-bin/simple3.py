#!/userdata/Li/miniconda3/envs/python_study/bin/python3
#python -m http.server --cgi 8000
#http://192.168.1.16:8000/cgi-bin/simple3.py
import cgitb; cgitb.enable();
import cgi
form = cgi.FieldStorage()

name = form.getvalue('name', 'world')

print("""Content-type: text/html

<html>
  <head>
    <title>Greeting Page</title>
  </head>
  <body>
    <h1>Hello, {}!</h1>


    <form action='simple3.py'>
    Change name <input type='text' name='name' />
    <input type='submit' />
    </form>
  </body>
</html>
""".format(name))