import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    '''
    1. 在 `select.select(inputs, [], [])` 中,`inputs` 是一个列表,包含了需要被监视的socket对象。
    第一个参数表示要监视的可读对象,第二个参数表示要监视的可写对象,第三个参数表示要监视的错误对象。
    在这里,我们只对可读对象感兴趣,所以第二个和第三个参数为空列表。

    2. `select.select()` 返回三个列表 `rs, ws, es`,分别包含了就绪的可读、可写和错误的socket对象。
    在这段代码中,我们只关心可读的对象,所以只使用了 `rs`。
    当 `select.select()` 返回时,`rs` 列表中包含了当前可以读取数据的socket对象。
    '''
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print('Got connection from', addr)
            inputs.append(c)
        '''
        1. `if r is s:`: 这个条件判断语句用来检查当前处理的socket对象 `r` 是否是监听socket `s`。如果是,说明有新的客户端连接请求到达。
        2. `c, addr = s.accept()`: 调用 `s.accept()` 方法来接受新的客户端连接,返回一个新的socket对象 `c` 和客户端的地址 `addr`。
        3. `print('Got connection from', addr)`: 打印出客户端连接的地址,即打印出客户端的IP地址和端口号。
        4. `inputs.append(c)`: 将新的客户端socket对象 `c` 添加到 `inputs` 列表中,以便后续对其进行监视。这样可以确保在下一次循环中,可以处理新客户端发送的数据。
        '''
        else:#如果当前对象不是监听socket,表示是已连接的客户端socket。
            try:
                data = r.recv(1024)
                disconnected = not data
                '''
                `disconnected = not data`是一个逻辑运算,`not data`是对`data`进行逻辑取反操作。
                在这里,`data`是接收到的客户端发送的数据,如果`data`为空（即没有接收到数据）,那么`not data`的结果为True,表示客户端已经断开连接。
                `not data`的数据类型是布尔类型,即True或False。
                '''
            except socket.error:
                disconnected = True

            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)#从inputs列表中移除断开连接的socket对象。
            else:
                print data