# replace_function_name

### 主要功能

LLVM生成IR时使用md5替换函数名

### 使用方法

clone仓库，将replace文件夹放到任意位置，并设置replace路径为环境变量REPATH


```
git clone https://github.com/penguin-wwy/replace_function_name.git
cd replace_function_name
mv replace /Users/home/
```

添加环境变量

```
export REPATH=/Users/home/replace
```

```
mkdir ../build
cd ../build
cmake ../replace_function_name
make -j 4
```

编译完成后使用bin/clang编译

首先打开replace下的1.code，没有则创建

输入如下内容

```
1
ClassName:FucntionName1
ClassName:FucntionName2
...
```

除第一行外格式为类名 + 冒号 + 函数名，暂时不支持构造函数、析构函数、非成员函数。

之后执行第一次编译

编译完成后执行replace/replace.py，再执行第二次编译即可