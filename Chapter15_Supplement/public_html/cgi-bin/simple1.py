#!/userdata/Li/miniconda3/envs/python_study/bin/python3
#python -m http.server --cgi 8000
#http://192.168.1.16:8000/cgi-bin/simple1.py
import cgitb; cgitb.enable();
print('Content-type: text/plain')
print() # Prints an empty line, to end the headers

print('Hello, world!') 