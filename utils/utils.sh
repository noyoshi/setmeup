#!/usr/bin/env bash

error_print() {
  echo "$1" 1>&2
}

check_deps() {
  r=0

  for val in $1; do
    if [[ `exists $val` -ne 0 ]]
    then
      r=1
      break
    fi
  done

  return $r
}

exists() {
  which $1 > /dev/null 2>&1
  if [[ $? -ne 0 ]]
  then
    return 1
  fi

  return 0
}

present() {
  ls $1 > /dev/null 2>&1
  if [[ $? -ne 0 ]]
  then
    return 1
  fi

  return 0
}

get_os() {
  OS=$(awk '/DISTRIB_ID=/' /etc/*-release | sed 's/DISTRIB_ID=//' | tr '[:upper:]' '[:lower:]')
}
