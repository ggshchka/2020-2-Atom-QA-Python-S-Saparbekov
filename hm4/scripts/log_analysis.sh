#!/bin/bash

arg=${*: -1}

err_handler(){
	echo $1
}

check_arg(){
	if [ $arg != '--help' ]; then
		if [ ! -f $arg ] && [ ! -d $arg ]; then
        	        err_handler 'ERROR: file not found'
			exit 0
		fi
	fi
}

req_cnt_all() {
	grep 'HTTP' $1 | wc -l 
}

req_cnt_separ() {
        grep $1 $2 | wc -l 
}

greatest_req(){
	awk '{ print length, $0 }' $1 | sort -gr | head -10 | cut -d" " -f1-10
}

greatest_loc_with_40x(){
	grep -e 'HTTP/1.*" 4[0-9][0-9]' $1 | cut -d' ' -f7 | sort | uniq -c | sort -nr | head
}

greatest_loc_with_50x(){
        grep -e 'HTTP/1.*" 5[0-9][0-9]' $1 | cut -d' ' -f7 | sort | uniq -c | sort -nr | head
}

help(){
	echo 'Usage: '${0}' [OPTION] [FILE or DIRECTORY]'
	echo 'Analysis log files'
	echo
	echo 'Optional arguments:'
	echo '	-a, --requestcountall		count of all requests'
	echo '	-m, --requestcountsepar		count of requests by method'
	echo '	-g, --greatestrequests		top 10 requests by num of characters'
	echo '	-c, --locwithclienterror	top 10 locations by num of client errors'
	echo '	-s, --locwithservererror	top 10 locations by num of server errors'
        echo '	    --help			display this help and exit'
        echo
        echo 'Examples:'
	echo '	'${0}' -a file.log'
	echo '	'${0}' -m "PUT" logs/ '
	echo
}

options(){
	case $1 in
		--requestcountall | -a)
			req_cnt_all $2;;
		--requestcountsepar | -m)
			req_cnt_separ $3 $2;;
		--greatestrequests | -g)
			greatest_req $2;;
		--locwithclienterror | -c)
			greatest_loc_with_40x $2;;
 		--locwithservererror | -s)
			greatest_loc_with_50x $2;;
		--help)
			help;;
		*)
			err_handler "$0: unknown option"
			err_handler "Try '$0 --help' for more information";;
	esac
}

#---------------------------------------------------------------------------------------
if [ $1 = --help ]; then
  options $1 ${file} $2
else
  check_arg
  if [ -d $arg ]; then
      for file in $arg/*.log; do
                    echo '******************************************************************'
                    echo "          FILE: $file	COMMAND: $1                             "
                    echo '-------------------------------------------------------------------'
                    options $1 ${file} $2
                    echo '-------------------------------------------------------------------'
                    echo
                    echo
            done >> ../result/res_bash.txt
  else
    echo "******************************************************************
    FILE: $arg	COMMAND: $1
-------------------------------------------------------------------
  $( options $1 ${arg} $2 )
-------------------------------------------------------------------


  " >> ../result/res_bash.txt
  fi
fi