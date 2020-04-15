#!/usr/bin/env bash
set -eou pipefail

echo "Installing  vim, plugins, and configs..."

which vim > /dev/null 2>&1

if [[ $? -ne 0 ]] ; then
  echo "vim not installed"
  exit 1;
fi

ls ~/.vim/bundle/Vundle.vim > /dev/null 2>&1
if [[ $? -eq 0 ]]; then
  echo "vundle already installed"
  exit 1;
fi

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
