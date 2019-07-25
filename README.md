# demo
水电费是
10 *args and **kwargs
用*args和**kwargs只是为了方便并没有强制使用它们.

当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数:

>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print '{0}. {1}'.format(count, thing)
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage
