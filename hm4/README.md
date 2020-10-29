**BASH SCRIPT**

Usage: 

    ./log_analysis.sh [OPTION] [FILE or DIRECTORY]
Analysis log files

arguments:

        -a, --requestcountall           count of all requests
        -m, --requestcountsepar         count of requests by method
        -g, --greatestrequests          top 10 requests by num of characters
        -c, --locwithclienterror        top 10 locations by num of client errors
        -s, --locwithservererror        top 10 locations by num of server errors
            --help                      display this help and exit

Examples:

        ./log_analysis.sh -a file.log
        ./log_analysis.sh -m "PUT" ../logs/ 




**PYTHON SCRIPT**

usage:
 
    python log_analysis.py [-h] command [method] filename

Analysis log files

positional arguments:

      command     requestcountall or a, requestcountsepar or m, greatestrequests
                  or g, locwithclienterror or c, locwithservererror or s
      method      POST, GET, ...
      filename    filename or dir

Examples:

        python log_analysis.py a file.log

optional arguments:
    
    -h, --help  show this help message and exit
