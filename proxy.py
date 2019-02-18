class Subject:
  "主题"
  def request(self):
    pass

class RealSubject(Subject):
  "真实主题"
  def request(self):
    print("RealSubject todo something...")

class ProxySubject(Subject):
  "代理主题"
  def __init__(self,subject):
    self.__realsubject = subject
  def request(self):
    self.preRequest()
    if self.__requset is not None:
      self.__request.request()
    self.afterRequest()
  def preRequest():
    pass
  def afterRequest():
    pass
  
def client():
  "客户端调用"
  realsubject = RealSubject()
  proxysubject = ProxySubject(realsubject)
  proxysubject.request()
