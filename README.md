### Miniconda

* [Download Now](https://www.anaconda.com/download/success)

  ```
  conda update conda
  conda list
  conda env list
  ```
  
* 创建虚拟环境并安装软件包
  ```
  conda create -n deepseek python=3.11 openai
  conda remove -n env_name
  conda remove -n env_name pkg_name
  ```

* 激活虚拟环境

  ```
  conda activate deepseek
  conda install pkg_name
  conda uninstall pkg_name
  conda deactivate
  ```

* 环境变量修改

  `export PATH=/path/to/python:$PATH`

* 重要文档

  [Python 3.13.0 documentation](https://docs.python.org/3.13/index.html)

### Cursor

* [Download Now](https://www.cursor.com/)
  
  * File > Prefereces > VS Code Settings > workbench.activityBar.orientation > vertical
  * File > Prefereces > Cursor Settings > General > Rules for AI
  * File > Prefereces > Cursor Settings > Models > Model Names
  * File > Prefereces > Cursor Settings > Features > Codebase indexing
  * File > Prefereces > Cursor Settings > Features > Docs

* LLM Extensions

    * Github Copilot
    * MarsCode AI
    * Raccoon
    * TONGYI Lingma

* Chat(Ctrl/⌘+L)

  * 主要负责通用问题的解决
  * 针对更宽泛的代码问题进行对话/多轮对话
  * 对话小技巧
    * @ 上下文引用
    * @Web 搜索互联网
    * Ctrl/⌘+Enter 搜索整个代码库
    * 直接粘贴图片

* Edit(Ctrl/⌘+K)

  * 代码生成和编辑
  * 主要负责用来生成或修改局部的代码
  * 提示栏分为两个类型
      * 代码编辑提示栏
      * 终端提示栏
  * @注记
    
    * 全局上下文
      * @Files：传递指定代码文件上下文
      * @Code：传递指定代码块（函数和类）上下文
      * @Docs：从官方文档获取上下文（需先在配置文件添加文档）
      * @Web：从搜索引擎结果获取上下文
      * @Folders：传递文件目录信息上下文
    
    * 仅限代码生成窗口
      * @Chat：传递对话窗口内容上下文
      * @Definitions：传递变量和类型定义上下文
    
    * 仅限对话窗
      * @Git：传递 Git commit history
      * @Codebase：在代码仓里扫描文件传入

* Composer(Ctrl/⌘+I) 

  * File > Prefereces > Cursor Settings > Features > Composer > Enabled

  * 主要特性
    * 多文件编辑
    * 完整应用生成
    * 上下文理解
    * 交互式优化

  * 使用场景
    * 快速原型设计和创建最小可行产品(MVP)
    * 跨多个文件实现复杂功能
    * 重构现有代码
    * 设置项目结构和样板代码
