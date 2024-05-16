import argparse
import sys
from collections import namedtuple
import math

KunitBuildRequest = namedtuple('KunitBuildRequest', ['jobs', 'build_dir', 'alltests', 'make_options'])
Point = namedtuple('Point', 'x y', defaults=(0, 0))
def main(argv, linux=None):
    #创建ArgumentParser对象
    parser = argparse.ArgumentParser(description='示例程序，展示如何使用 argparse 处理命令行参数。')
    #创建子命令
    subparsers = parser.add_subparsers(title='subcommand', description='可用子命令', help='子命令帮助', dest='subcommand')
    #添加run命令
    run_parser = subparsers.add_parser('run', help='Run a KUnit test.')
    #添加run命令参数
    run_parser.add_argument('--build_dir',help='The directory where the test is build.',
                         type=str, default='.kunit', metavar='build_dir')
    #解析程序输入参数
    args = parser.parse_args(argv)
    print(args)
    print(args.subcommand)

def calculate_distance(a, p) -> float:
    """
    计算两点之间的距离。
    参数:
    self - 第一个点的坐标。
    p - 第二个点的坐标。

    返回:
    float - 两点之间的欧氏距离。
    """
    return math.sqrt((a.x - p.x) ** 2 + (a.y - p.y) ** 2)

X = namedtuple('X', 'a b c')  # 定义一个名为X的namedtuple，包含三个字段：a、b、c
class Z(X):  # 定义一个名为Z的类，继承自namedtuple X
    #如下方式不能使用
    '''
    def __init__(self, a, b, c, d):
        super(Z, self).__init__(a, b, c)  # 调用父类X的构造函数，初始化字段a、b、c
        self.d = d  # 添加一个新的属性d
    '''
    #namedtuple 返回的是一个不可变的对象类型，因此不能像普通类那样添加属性。
    def __new__(cls, a, b, c, d):
        obj = super(Z, cls).__new__(cls, a, b, c)  # 创建一个X的实例
        obj.d = d  # 动态添加属性d
        return obj
if __name__ == '__main__':
    #设置程序入口 并配置至少一个参数
    #程序编写补全使用tab键
    main(sys.argv[1:])

    KunitBuildRequest(jobs=1, build_dir='.kunit', alltests=False, make_options='opts')
    print(KunitBuildRequest)
    print(KunitBuildRequest._fields)
    Pointa = Point(1, 2)
    Pointb = Point(4, 6)
    print(calculate_distance(Pointa, Pointb))
    newZ = Z(1, 2, 3, 4)
    print(newZ.d)
