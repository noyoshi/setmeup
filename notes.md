```py
vimPackage = Package("vim", steps=[
  step("install vim", Installer.install("vim")),
  step("install git", Installer.install("git")), 
  step("get vundle", FileInstaller("~/vim/vundle/vim", cmd="git clone ...")
)
```
