# Wikipedia-six-way-handshake-theory-homework
任务是用 Python 编写一个应用程序/脚本，该应用程序/脚本将分析维基百科文章主要块中的链接，并找到从 url1 =*> url2 开始的正确跳转链，反之亦然。

限制：

1) 两个输入链接将使用相同的语言。您应该找到相同语言文章的链接。（可能用俄语、英语）

2) 链接必须来自文章正文或来自参考资料块。仅考虑到维基百科的链接。

3）您需要实施速率限制并将其作为第三个参数传递 - 您不能创建大于限制的连接

4) 如果在 5 次转换中没有达到目标 url1 -> url2 和 url2 -> url1 - 我们报告这个。忽略深度超过 5 的链接并避免重复

输入（示例）：https://en.wikipedia.org/wiki/Six_degrees_of_separation https://en.wikipedia.org/wiki/American_Broadcasting_Company 10

输出：url2 =>[url] => [url] =>url1
