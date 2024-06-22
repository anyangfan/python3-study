from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass
'''
这段代码定义了一个名为Server的类,它继承了ForkingMixIn和TCPServer两个类。
ForkingMixIn是一个多进程混合类,用于实现多进程处理客户端请求,而TCPServer是一个基于TCP协议的服务器类。
通过继承这两个类,Server类可以实现基于TCP协议的多进程服务器功能。
在代码中,pass表示空语句,因为类本身并不包含任何额外的方法或属性。
'''

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()