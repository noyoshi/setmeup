import os
import subprocess as sub
from utils import is_installed, does_exist

class Installer:
    def __init__(self, name, prefix, package=None):
        self.name = name
        self.prefix = prefix
        self.package = package

    def install(self, force=True):
        package = self.package
        if not force and is_installed(package):
            print(f"====> Package {package} is already installed!")
            return False

        print(f"====> Installing package {package} using installer {self.name}")

        install_command = f"{self.prefix} {package}"
        print(f"=====> running {install_command}")

        code = sub.call(install_command.split())

        if code != 0:
            return False

        return True

    def __call__(self, package):
        return Installer(self.name, self.prefix, package)

class FileInstaller:
    def __init__(self, filepath, command):
        self.filepath = filepath
        self.command = command

    def install(self, force=False):
        if does_exist(self.filepath) and not force:
            print(f"{self.filepath} exists")
            return False
        print(f"=====> running {self.command}")
        code = sub.call(self.command.split())
        if code != 0:
            return False

        return True

class CustomInstaller:
    def __init__(self, command):
        self.command = command

    def install(self):
        print(f"=====> running {self.command}")
        code = sub.call(self.command.split())
        if code != 0:
            return False

        return True


class Brew(Installer):
    def __init__(self):
        super().__init__("Homebrew", "brew install")

class Apt(Installer):
    def __init__(self):
        super().__init__("Apt", "apt-get install")

class Step:
    def __init__(self, name, installer, skip=False):
        self.name = name
        self.installer = installer
        self.skip = skip

    def run(self):
        print(f"===> Running step {self.name}")
        ret = self.installer.install()
        # If we are ok with having an error at this stage, just return true
        if self.skip:
            return True
        return ret

# TODO a program package is a program (such as vim) along with configs, and dependencies
# that this program needs to have installed (like vundle), and all steps to set it up
# (such as vim -c "PluginInstall" -c "q" -c "q")
class ProgramPackage:
    def __init__(self, prog_name, steps=[]):
        self.name = prog_name
        # steps would be bash steps to do before hand?
        self.steps = steps

    def install(self):
        print(f"=> Installing package {self.name}")
        for step in self.steps:
            if not step.run():
                return False

        return True

brew = Brew()

# TODO this stuff fails when you try to do stuff with symlinked things... like 
# how I have 'vim=neovim', this will run with vim, whereas the user thinks maybe they 
# are going to be doing the thing that happens when in the shell you run 'vim ...', 
# what is really happening is that you are using neovim!
VimPackage = ProgramPackage(
    "vim",
    steps = [
        Step("install vim", brew("vim")),
        Step("install git", brew("git"), True),
        Step("get vundle", FileInstaller(
            "~/.vim/bundle/Vundle.vim",
            "echo 'uh oh'"
            ), True),
        Step("install plugins", CustomInstaller("vim -c 'PluginInstall' -c 'q' -c 'q'"))
    ]
)

VimPackage.install()

