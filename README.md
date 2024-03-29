# Auto Get Traffic
使用 GitHub Actions 自动获取 Airport 流量

## 使用说明

**Fork from Hostloc Auto Get Points**

Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加两个秘密环境变量。

其中 `EMAIL` 存放你在 KCJISU 的帐户名，`PASSWORD` 存放你的帐户密码。支持同时添加多个帐户，数据之间用半角逗号 `,` 隔开即可，帐户名和帐户密码需一一对应。

再加一个普通的环境变量DOMAIN。存放域名。

设置好环境变量后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 `I understand...` 按钮确认在 Fork 的仓库上启用 Github Actions 。

最后在你这个 Fork 的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符）提交一下手动触发一次 Github Actions 就可以了 **（重要！！！测试发现在 Fork 的仓库上 Github Actions 的定时任务不会自动执行，必须要手动触发一次后才能正常工作）** 。

仓库内包含的 GitHub Actions 配置文件会在每天国际标准时间 17 点（北京时间凌晨 1 点）自动执行获取积分的脚本文件，你也可以通过 `Push` 操作手动触发执行（测试发现定时任务的执行可能有 5 到 10 分钟的延迟，属正常现象，耐心等待即可）。
