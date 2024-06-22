import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

fdmap = {s.fileno(): s}
'''
fdmap是一个字典,键是socket的文件描述符(fileno),值是对应的socket对象。
在这里,将服务器socket s的文件描述符作为键,s本身作为值存储在fdmap中。
'''
s.listen(5)
p = select.poll()
p.register(s)
'''
代码中使用select.poll()创建了一个poll对象p,并将服务器socket s注册到p中。
然后进入一个无限循环,调用p.poll()来获取就绪的文件描述符和事件。
如果文件描述符在fdmap中,表示有新的连接请求,调用s.accept()来接受连接,并注册新的socket c。
如果事件是select.POLLIN,表示有数据可读,调用fdmap[fd].recv(1024)来接收数据。
'''
while True:
    events = p.poll()
    for fd, event in events:                        #遍历events列表中的每个元素,每个元素是一个包含文件描述符fd和事件event的元组。
        if fd in fdmap:                             #检查文件描述符fd是否在fdmap字典中。如果在fdmap中,表示有新的连接请求。
            c, addr = s.accept()                    #接受新的连接请求,返回一个新的socket对象c和客户端地址addr。
            print 'Got connection from', addr
            p.register(c)                           #将新的socket对象c注册到poll对象p中,以便检测其事件。
            fdmap[c.fileno()] = c                   #将新的socket对象c的文件描述符作为键,c本身作为值存储在fdmap字典中。
        elif event & select.POLLIN:                 #如果事件是数据可读事件(select.POLLIN),表示有数据可读取。
            data = fdmap[fd].recv(1024)
            if not data:                            # No data -- connection closed
                print fdmap[fd].getpeername(), 'disconnected'
                p.unregister(fd)
                del fdmap[fd]
                '''
                当没有数据可读时,表明连接已经关闭,需要从fdmap中删除对应的socket对象。
                使用del fdmap[fd]来删除文件描述符fd对应的socket对象。
                '''
            else:
                print data