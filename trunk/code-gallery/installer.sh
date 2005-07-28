#!/bin/sh

#
# Welcome dialog
#
if [[ -n $(type -p dialog) ]]; then
	dialog --backtitle "Code-Gallery Installation" --yesno "If you are running it by root, /usr/share/code-gallery will be crated, otherwise, if you are running in from user it will create a dir in your home ~/.code-gallery.\n\nDO YOU WANT TO CONTINUE?" 0 0
	case $? in
		0) C=y ;;
		1) C=n ;;
		255) exit 0 ;;
	esac
	
else
	echo -en "\n\033[0;31m>>> [WARNING] : THIS INSTALLER WILL CREATE A NEW DIR ON YOUR SYSTEM!\033[m\n\nIf you are running it by root, /usr/share/code-gallery will be crated, otherwise, if you are running in from user it will create a dir in your home ~/.code-gallery.\n\n>>> DO YOU WANT TO CONTINUE? [y/n]  "
read C
fi

clear


#
# This checks for user id and set the path correctly
#
if [[ $C = y ]]; then

	if [[ $UID -eq 0 ]]; then
			DIR=/usr/share/code-gallery
	else
			DIR=$HOME/.code-gallery
	fi

else
	
	exit 0
fi

#
# Check for convert (part of imagemagick suite)
#
if [[ -z $(type -p convert) ]]; then
	echo -en "\n\033[0;31m>>> [WARNING] : Looks like you don't have ImageMagick installed.\n                Download it from www.imagemagick.org in order to use code-gallery\033[m\n\n"
fi

#
# Check if DIR alredy exists
#
if [[ -d $DIR ]]; then
	
	echo -en "\033[0;36m>>> [WARNING] : $DIR already exist.\033[m\nShall I remove it? [y/n]  "
	read C

	if [[ $C != y ]]; then
		exit 0
	
	else
		rm -ri $DIR
	fi
fi

#
# File copy
#
mkdir $DIR
mkdir $DIR/css
cp ./css/* $DIR/css/

#
# Code-gallery copy
#
if [[ $UID -eq 0 ]]; then

	echo -en "\033[0;32m>>> [MESSAGE] : Coping exec file to /usr/bin/\033[m\n"
	cp ./code-gallery /usr/bin/code-gallery
	cp ./xcode-gallery /usr/bin/xcode-gallery

else

	echo -en "\033[0;36m>>> [WARNING] : You don't have the permission to copy code-gallery (and xcode-gallery) into /usr/bin/\n>>> I'll copy it into $HOME/bin/\033[m\n"
	if [[ -d $HOME/bin ]]; then
		cp ./code-gallery $HOME/bin
		cp ./xcode-gallery $HOME/bin
	else
		mkdir $HOME/bin
		cp ./code-gallery $HOME/bin
		cp ./xcode-gallery $HOME/bin
	fi

fi

#
# Finish message
#
echo -en "\n\033[1;32m>>> [MESSAGE] : Code-Gallery installation is now complete.\033[m\n\n\033[1;36m>>> [WARNING] : In order to run code-gallery, you need to type 'code-gallery' in your shell (if it is in your \$PATH). Type 'xcode-gallery' for code-gallery's gui\033[m\n\n\n\033[1;32mENJOY!\033[m\n\n"
