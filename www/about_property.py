# coding: utf-8
from types import MethodType
#Bad Demo


class Students(object):
    pass

def set_scores(self, scores):
    self.scores = scores

s = Students
s.name = "Michael"  # 随时随地绑定实例属性
print(s.name)

#同样也可以给一个实例绑定方法
s.set_age = MethodType(set_scores, s)
print(s.scores)

#同样给所有实例绑定方法
Students.set_scores = set_scores  #动态绑定意味在运行过程中绑定，虽然可以在class中直接定义




