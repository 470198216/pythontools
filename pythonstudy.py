import argparse
import sys  
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

if __name__ == '__main__':
    #设置程序入口 并配置至少一个参数
    #程序编写补全使用tab键
    main(sys.argv[1:])

