import logging

module_logger = logging.getLogger('mainModule.sub')
class SubModuleClass(object):
    def __init__(self):
        self.logger = logging.getLogger('mainModule.sub.module:mainModule.sub.module')
        self.logger.info('mainModule.sub.module:creating an instance in mainModule.sub.module')
    def doSomething(self):
        self.logger.info('mainModule.sub.module:do something from mainModule.sub.module')
        a=[]
        a.append(1)
        self.logger.debug('added 1 to a')
        self.logger.info("finish something in mainModule.sub.module")

def som_function():
    module_logger.info('mainModule.sub(som_function):call function in som_function')