#!/usr/bin/env bash
# set -eou pipefail
set -ou pipefail

source utils/utils.sh

echo "Installing  vim, plugins, and configs..."

if [[ `check_deps "vim git asdf"` -ne 0 ]]
then
  exit 1
fi

if [[ `present "~/.vim/bundle/Vundle.vim"` -eq 0 ]]
then
  echo "vundle already installed"
  exit 1
fi

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
