- [ ] excludes.txt 中不能使用 `~`，可以使用 `$HOME`。
- [ ] includes.txt 中 `~` 和 `$HOME` 都不能使用。

> Environment variables in exclude files are expanded with os.ExpandEnv, so /home/$USER/foo will be expanded to /home/bob/foo for the user bob. To get a literal dollar sign, write $$ to the file - this has to be done even when there’s no matching environment variable for the word following a single $. Note that tilde (~) is not expanded, instead use the $HOME or equivalent environment variable (depending on your operating system).
> 
> - https://restic.readthedocs.io/en/latest/040_backup.html#excluding-files
> - https://github.com/restic/restic/issues/2825

- [ ] 