#!/usr/bin/env python
import subprocess
import argparse,os
from os.path import expanduser


source_directory = os.path.dirname(os.path.realpath(__file__))
working_directory = os.getcwd()
home_directory = expanduser("~")

print home_directory

def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


def install_git():
    script("zypper install git")
    pass

def install_vim_config():
    script("git clone https://github.com/wangeen/vim.git")
    script("mv vim/.vim ~")
    script("mv vim/.vimrc ~")

def install_pip():
	script("wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg")
	script("sh setuptools-0.6c11-py2.7.egg")

	script("wget http://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz")
	script("tar -zvxf pip-1.2.1.tar.gz")
	os.chdir("pip-1.2.1")
	script("python setup.py install")
	os.chdir("..")
	pass

def install_django():
	script("pip install Django==1.5.1")

def install_github():
	print "help on public key for github"
	print "https://help.github.com/articles/generating-ssh-keys/"

def install_uwsgi():
	print "please add python dev from yast"
	script("export LDFLAGS="-Xlinker --no-as-needed")
	script("pip install uwsgi")
	pass

if __name__  == "__main__":
    #install_git()
    #install_vim_config()
	#install_pip()
	#install_django()
	#install_github()
	#install_uwsgi()

