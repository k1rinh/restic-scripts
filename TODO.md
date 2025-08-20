- [ ] excludes.txt 中不能使用 `~`，可以使用 `$HOME`。
- [ ] includes.txt 中 `~` 和 `$HOME` 都不能使用。

> Environment variables in exclude files are expanded with os.ExpandEnv, so /home/$USER/foo will be expanded to /home/bob/foo for the user bob. To get a literal dollar sign, write $$ to the file - this has to be done even when there’s no matching environment variable for the word following a single $. Note that tilde (~) is not expanded, instead use the $HOME or equivalent environment variable (depending on your operating system).
> 
> - https://restic.readthedocs.io/en/latest/040_backup.html#excluding-files
> - https://github.com/restic/restic/issues/2825

- [ ] 写一个 Python 脚本快速创建一个默认的备份任务。
    - 自动从 Healthchecks 创建 Check，获取 Ping URL 用于 `.service`。
    - 请求计划任务，或许可以自然语言 + LLM 生成 OnCalendar Expression。

