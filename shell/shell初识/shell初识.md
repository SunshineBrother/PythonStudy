# shell初识

## shell



`Shell（Unix Shell）`是一种命令行解释器，是Unix操作系统下最传统的人机接口。`Shell`脚本是解释执行的，不需要编译，和大部分的编程语言很相似，也有基本的变量和流程控制语句。我们平时使用Shell有两种方式：

- 1、输入命令，执行，这种方式称为交互式
- 2、批处理方式，用户事先写好shell脚本，然后顺序批次执行



第一个`Shell`环境是`ThompsonShell`，在贝尔实验室开发并于1971年发布。
现代`Shell`最突出的祖先是被称为sh的`BourneShell`，这是以在`AT&T`工作的创始人stephenBourne命名的



`shell`一直基于这个概念，不断添加各种新功能，演变出很多`shell`



例如，很早版本的`OS X`中使用的是`tcsh`作为默认的`shell`，这是由`csh(c shell)`，一种`C`语言演变而来

在`os x 10.3`版本之后，默认的`shell`是`bash`

除了默认的`bash`，现在`macos`中，默认的Shell变成了zsh。这是一种由`Paul Falstad`于1990年开发的。它是一个`Bourne`式`Shell`，它使用`bash`和previous shell的特性，并添加了更多的特性：

- 拼写检查功能
- 内置的编程特性
- 友好的交互



![bash](/Users/jiangjunhui/Desktop/myGithub/ScriptStudy/shell/shell初识/bash.png)



确认当前终端`tty`使用的`shell`类型

![shell](https://github.com/SunshineBrother/ScriptStudy/blob/main/shell/shell初识/shell.png)































































