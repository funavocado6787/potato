


import getopt
import logging
import sys

try:
    import config
except:
    sys.path.append('/etc/sofabuddy')
    import config

#    Function to display help message


def usage():
    print "sofabuddy.py [options]\n"
    print 'Example'
    print '\tsofabuddy.py -d "/media/downloads" -h "192.168.1.1"\n'
    print "Options"
    print "\t-?, --help\t\t\tWill bring up this message"
    print "\t-d, --download_dir\t\tOverride the default download directory"
    print "\t-n, --nuke_dir\t\t\tOverride the default nuke directory"
    print "\t-t, --tv_dir\t\t\tOverride the default tv directory"
    print "\t-l, --log_file\t\t\tChoose the location for your log file (default=/tmp/sofabuddy_log)"
    print "\t-k, --lock_file\t\t\tChoose the location for your lock file (default=/tmp/sofabuddy_lock)"
    print "\t-h, --host\t\t\tChoose the ip address of your XBMC box (default=127.0.0.1)"
    pass


#    Parse command line options


try:
    opts, args = getopt.getopt(sys.argv[1:], "?d:n:t:l:h:k:", ["help", "download_dir=", "nuke_dir=", "tv_dir=", "log_file=", "host=", "lock_file="])
except getopt.GetoptError, err:
    message = 'ERROR=sofabuddy.py: ' + str(err)
    print message
    usage()
    sys.exit(2)

for o, a in opts:
    if o in ("-?", "--help"):
        usage()
        sys.exit()
    if o in ("-d", "--download_dir"):
        download_dir = a
    elif o in ("-n", "--nuke_dir"):
        nuke_dir = a
    elif o in ("-t", "--tv_dir"):
        tv_dir = a
    elif o in ("-l", "--log_file"):
        log_file = a
    elif o in ("-k", "--lock_file"):
        lock_file = a
    elif o in ("-h", "--host"):
        xbmc_ip = a
    else:
        assert False, "unhandled option"


#    If option has not been set explicitly on the command line then check if it
#    has been set in the config file.


#    These options are required and do not have a default value set. The module
#    will raise an exception if a value for these variables cannot be obtained.


try:
    download_dir
except NameError:
    download_dir = config.download_dir

try:
    tv_dir
except NameError:
    tv_dir = config.tv_dir

try:
    nuke_dir
except NameError:
    nuke_dir = config.nuke_dir


#    These values are optional and if they are not specified then default
#    values will be used.


try:
    xbmc_ip
except NameError:
    try:
        xbmc_ip = config.xbmc_ip
    except AttributeError:
        xbmc_ip = '127.0.0.1'

try:
    debug_logging
except NameError:
    try:
        debug_logging = config.debug_logging
    except AttributeError:
        debug_logging = 0

try:
    debug_logfile
except NameError:
    try:
        debug_logfile = config.debug_logfile
    except AttributeError:
        debug_logfile = '/tmp/sofabuddy.debug.log'

try:
    log_file
except NameError:
    try:
        log_file = config.log_file
    except AttributeError:
        log_file = '/tmp/sofabuddy.log'

try:
    lock_file
except NameError:
    try:
        lock_file = config.lock_file
    except AttributeError:
        lock_file = '/tmp/sofabuddy.lock'

try:
    sleep_time
except NameError:
    try:
        sleep_time = config.sleep_time
    except AttributeError:
        sleep_time = 900

try:
    recursive
except NameError:
    try:
        recursive = config.recursive
    except AttributeError:
        recursive = False

try:
    sleep_interrupt
except NameError:
    try:
        sleep_interrupt = config.sleep_interrupt
    except AttributeError:
        sleep_interrupt = '/tmp/sbsleepinterrupt'

#    Read any advanced settings from config file if set, otherwise use default
#    values

try:
    episode_number_regexes = config.episode_number_regexes
except AttributeError:
    episode_number_regexes = [['s[0-9][0-9]e[0-9][0-9]', 1, 3, 4, 6], ['s[0-9]e[0-9][0-9]', 1, 2, 3, 5], ['s[0-9]e[0-9]', 1, 2, 3, 4], ['[0-9][0-9]x[0-9][0-9]', 0, 2, 3, 5], ['[0-9]x[0-9][0-9]', 0, 1, 2, 4], ['s[0-9][0-9] ep[0-9][0-9]', 1, 3, 6, 8], ['[0-9][0-9][0-9]', 0, 1, 1, 3], ['[0-9][0-9][0-9][0-9]', 0, 2, 2, 4]]
