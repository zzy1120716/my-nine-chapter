"""
222. Getter与Setter
实现一个School的类，包含下面的这些属性和方法:

一个string类型的私有成员name.
一个setter方法setName，包含一个参数name.
一个getter方法getName，返回该对象的name。

样例
Java:
    School school = new School();
    school.setName("MIT");
    school.getName(); // 返回 "MIT" 作为结果

Python:
    school = School();
    school.setName("MIT")
    school.getName() # 返回 "MIT" 作为结果
"""


# __name 表示私有变量
class School:

    def __init__(self):
        self.__name = ''

    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    # write your code here
    def setName(self, name):
        self.__name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    # write your code here
    def getName(self):
        return self.__name
