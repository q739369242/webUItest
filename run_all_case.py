import unittest
import HTMLTestRunner
import os,time
#加载所有用例，并且执行

def html_report():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    file_path=os.getcwd()+'/test_case_report/'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    fp=open(file_path +"/"+ now+"report.html", "wb")
    return fp

def allcase():
    casedir=os.getcwd()+'/unitTestCase/'
    testcase=unittest.TestSuite()
    #top_level_dir测试模块的顶层目录，如果没有顶层就为none
    discover=unittest.defaultTestLoader.discover(casedir,pattern="test_*.py")
    #discover 方法筛选出来的test_开头的用例（设置了跳过的除外），循环添加到测试套件中
    #这个是不管每个case下面if __name__ =="__main__":写的是执行全部还是执行其中一个，
    # 都是将全部test_开头的用例加入进去
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    return testcase


if __name__ =="__main__":
    outfile = html_report()
    runner1 = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='自动化测试报告',
        description='用例执行情况'
    )

    runner1.run(allcase())
    outfile.close()