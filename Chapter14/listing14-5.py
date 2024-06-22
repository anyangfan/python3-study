from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()

'''
这段代码定义了一个自定义的服务器类Server,继承自ThreadingMixIn和TCPServer。
ThreadingMixIn是一个多线程混合类,用于实现多线程处理客户端请求,而TCPServer是一个基于TCP协议的服务器类。

在Server类中并没有定义任何额外的方法或属性,只是使用pass语句来占位。
这是因为Server类主要是用来指定服务器的行为,具体的处理逻辑会在Handler类中实现。

Handler类继承自StreamRequestHandler,这个类用于处理客户端请求的具体逻辑。
在handle方法中,首先获取客户端的地址信息,然后打印出连接信息。接着使用self.wfile.write方法向客户端发送一条消息"Thank you for connecting"。

最后,创建一个Server实例server,指定服务器监听的IP地址和端口号为('', 1234),并指定Handler类来处理客户端请求。
 调用server.serve_forever()方法启动服务器,开始接受客户端连接并处理请求。
'''