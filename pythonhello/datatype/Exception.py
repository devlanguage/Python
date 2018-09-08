#!/usr/bin/python
# coding: UTF-8
def testException(level):
    print "level=" + str(level)
    if level < 1:
        raise Exception("SmallThan1", level)
    elif level < 5:
        raise 'SmallThan5'
        # 触发异常后，后面的代码就不会再执行


for i in range(0, 8, 2):  # print 0,2,4,6
    try:
        testException(i);
    except 'SmallThan1':
        print 'catched SmallThan1 exception:' + str(Exception)
    except Exception('SmallThan5'):
        print 'catched SmallThan5 exception:' + str(Exception)
    except:
        print 'catched all exception:' + str(Exception)    
    else:
        print "there is no exception"
    finally:
        print "finally"    
