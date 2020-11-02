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
        python log_analysis.py m POST ../logs/access.log

optional arguments:
    
    -h, --help  show this help message and exit
