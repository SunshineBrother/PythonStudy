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



![bash](https://github.com/SunshineBrother/ScriptStudy/blob/main/shell/01-shell初识/bash.png)



确认当前终端`tty`使用的`shell`类型

![shell](https://github.com/SunshineBrother/ScriptStudy/blob/main/shell/01-shell初识/tty.png)



于此同时，`macOS`还提供了很多种其他类型的`shell`

![lsshell](https://github.com/SunshineBrother/ScriptStudy/blob/main/shell/01-shell初识/lsshell.png)





## 运行shell脚本

- 1、进入所在目录，然后输入命令`./test.sh`

- 2、直接将`.sh`拖到终端

  ```shell
  #!/bin/bash
  echo "Hello World !"
  ```

  **`#!`** 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 `Shell`。

  `echo` 命令用于向窗口输出文本。



## .zshrc .bashrc .bash_profile 的区别

在使用命令行工具时，我们可能会遇到一些教程，可能需要你把一些配置写入到`.bashrc`、`.bash_profile`或者`.zshrc`等。那么这几个文件到底有什么作用和区别？

首先，从文件名称判断`.bashrc、.bash_profile`是给`Bash`来使用的。而.zshrc是给`zsh`来使用的。



### 交互式登录和非登录`Shell`

当调用`Shell`时，`Shell`从一组启动文件中读取信息并执行命令。读取什么文件取决于`Shell`是作为`交互式登录还是非登录调用`

换而言之，Shell分为交互式的或者非交互式的

- `交互式Shell`是读取和写入到用户终端的Shell程序，用户在终端输入命令，并在回车后立即执行
- `非交互式Shell`是与终端不相关的Shell程序，如脚本执行



当作为交互式登录`Shell`调用时，`Bash`会先查找/etc/profile文件，如果该文件存在，它将运行文件中列出的命令。然后，搜索`~/.bashprofile` `~/.bash_login`以及`~/.profile`文件，顺序读取。

当`Bash`作为交互式非登录shell调用时，会读取`~/.bashrc`。



所以说，`.bashrc`和.bash_profile之间的区别是，`.bash_profile`当`Bash`作为交互式登录`shell`调用时被读取并执行，而`.bashrc`对于交互式非登录shell被执行。



**确认当前是登录还是非登录shell**
在`tty`中执行`echo $0`，输出的Shell如果前面带`-`，说明是登录Shell。

![shell](https://github.com/SunshineBrother/ScriptStudy/blob/main/shell/01-shell初识/shell1.png)



### 建议配置

- `1、bash`：
  - 将配置选项放到`~/.bashrc`中，然后在`~/.bash_profile`中通过`source`调用。
- `2、zsh`
  - 建议仍然将配置选项放到`~/.bashrc`，`~/.bash_profile`中通过`source`调用，最后在`~/.zshrc`中`source`调用`~/.bash_profile`.



























