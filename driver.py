from selenium import webdriver
from selenium.webdriver import Remote

#启动浏览器驱动
def browser():
    #driver = webdriver.Chrome()
    
    #运行主机：端口号
    host = '127.0.0.1:4444' 

    #指定浏览器
    dc = {'browserName':'firefox','marionette':'Fales'}
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.close()
