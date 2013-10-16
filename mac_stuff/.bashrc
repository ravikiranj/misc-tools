#Custom functions
function trmake()
{
    cd $TRTOP
    ant compile-tr merge-classes
    cd -
}

function trcleanmake(){
    cd $TRTOP/tr; 
    make clean; make;
    cd -
}

function appmake()
{
    cd $TRTOP
    ant compile-applications merge-classes
    cd -
}

function appcleanmake()
{
    cd $TRTOP/Applications;
    make clean; make
    cd -
}

function featuresmake(){
    cd $TRTOP
    ant compile-features merge-classes
    cd -
}

function jsmake(){
    cd $TRTOP/site/js3;
    make;
    cd -;
}

function cssmake(){
    cd $TRTOP/site/css2;
    make;
    cd -;
}

function macspotify(){
    if [ $# -gt 0 ]; then
        ssh rjanardhana@rj-mac-dev.dhcp.tripadvisor.com "/Users/rjanardhana/shpotify-master/spotify '$@'"
    else
        echo -e "Syntax: macspotify <status|play|pause|next|prev|vol up|vol down|vol #|quit>"
    fi
}

function brightness(){
    `python /home/rjanardhana/git/misc-tools/brightness-control/brightness.py`
}

function log(){
    echo -e "Cmd: tail -f /etc/httpd-MAINLINE/logs/tripadvisor.log"
    tail -f /etc/httpd-MAINLINE/logs/tripadvisor.log
}

function trlog(){
    if [ $# -gt 0 ]; then
        echo -e "Cmd: tail -f /etc/httpd-MAINLINE/logs/tripadvisor.log | grep -i '$@'"
        tail -f /etc/httpd-MAINLINE/logs/tripadvisor.log | grep -i "$@"
    else
        echo -e "Syntax: trlog <grep_expression>"
    fi
}

# run single selenium test against mainline
function selsingle(){
    if [ $# -gt 1 ]; then
        echo -e "Cmd: pythontr.sh run-single-test --filename $1 --browser '*firefox' -u ${2}.tripadvisor.com"
        pythontr.sh run-single-test --filename $1 --browser '*firefox' -u ${2}.tripadvisor.com
    else
        echo -e "Syntax: selsingle testFileName testServer[mainline|prerelease]"
    fi
}

# run all live content selenium tests
function selall(){
    ./run-tests --testsuite live_content --browser 'firefox3.6' -u mainline.tripadvisor.com | tee sel_lc_all.log
}

# run same command as jenkins build
function seljenkins(){
    #./run-tests -P X -a bogus-slice -t live_content -u mainline.tripadvisor.com -b '*firefox' -s win09n -F -q -A
    ./run-tests -t live_content -u mainline.tripadvisor.com -b '*firefox' -s win09n -P X -a bogus_slice -F -A -m 1 | tee sel_lc_jenkins.log
}

# custom jshint
function jshint(){
    filename=$@
    echo "/usr/local/bin/jshint --config /home/rjanardhana/.jshint $filename"
    /usr/local/bin/jshint --config /home/rjanardhana/.jshint $filename
}

# custom jshints (simple)
function jshints(){
    filename=$@
    echo "/usr/local/bin/jshint --config /home/rjanardhana/.jshint_simple $filename"
    /usr/local/bin/jshint --config /home/rjanardhana/.jshint_simple $filename
}

# RSYNC FBRS for USA
function rsyncmas(){
    /Users/rjanardhana/ta/cron-scripts/rsync-fbrs-28942.sh --verbose | tee /Users/rjanardhana/ta/cron-scripts/logs/rsync-fbrs-28942.log
}

# RSYNC FBRS for WORLD
function rsync1(){
    /Users/rjanardhana/ta/cron-scripts/rsync-fbrs-1.sh --verbose | tee /Users/rjanardhana/ta/cron-scripts/logs/rsync-fbrs-1.log
}

#Custom aliases and exports
#exports
export PS1='[\u@rj-mac-dev \W]# '
#export PS1='[\u@rj-mac-dev \W$(__git_ps1 " (%s)")]\# '
export JAVA_HOME='/usr/lib/jvm/java-7-openjdk-amd64'
export PATH=$PATH:$JAVA_HOME/bin:$TRTOP/scripts:/usr/lib/postgresql/8.4/bin
export SVN_EDITOR='vim'
export css="$TRTOP/site/css2"
export js="$TRTOP/site/js3"
export fb='/Users/rjanardhana/ta/cron-scripts/logs/rsync-fbrs.log'
export HISTTIMEFORMAT="%F %T "

# aliases
# command alias
alias apt-get='sudo apt-get'
alias axel='axel -n 10'
alias eclipse='/Users/rjanardhana/ide/eclipse/eclipse & disown'
alias grep="grep --exclude-dir=\.svn --exclude=*.class --color=auto"
alias find="find . -iname "
alias cpv="rsync -P"
alias up="svntr up"
alias so=". ~/.bashrc"
alias vimso="vim ~/.bashrc"
alias vimvim="vim ~/.vimrc"

# dev alias
alias ini="vim config/hosts/rj-mac-dev.ini"
alias features='vim $TRTOP/config/features.ini'
alias error="tail -f /etc/httpd-MAINLINE/logs/error_log"
alias appconfig="vim $TRTOP/config/webserver/app_tripadvisor.xml"
alias reconf="./configure mainline; make -C config; make -C config/webserver"
alias mac="ssh rjanardhana@rj-mac-dev.dhcp.tripadvisor.com"
alias makeunit='cd $TRTOP; make java_unittests; cd -'
alias c='colordiff | less -R'
alias slogin='echo "svntr login rjanardhana"; svntr login rjanardhana'

# tweak alias
alias csson="tweak feature on css_CONCAT; tweak feature on css_COMPRESS"
alias cssoff="tweak feature off css_CONCAT; tweak feature off css_COMPRESS"
alias json="tweak feature on JS_CONCAT; tweak feature on JS_COMPRESS"
alias jsoff="tweak feature off JS_CONCAT; tweak feature off JS_COMPRESS"

# directories
alias ta='cd /Users/rjanardhana/ta'
alias M='cd /Users/rjanardhana/ta/trsrc-MAINLINE'
alias P='cd /Users/rjanardhana/ta/trsrc-PRERELEASE'
alias D='cd /Users/rjanardhana/ta/tr-data'
alias I='cd /Users/rjanardhana/ta/tr-images'
alias L="cd /etc/httpd-MAINLINE/logs/"
alias v='cd $TRTOP/site/velocity_redesign'
alias t='cd $TRTOP'
alias trt='cd $TRTOP/tr'
alias css='cd $TRTOP/site/css2'
alias js='cd $TRTOP/site/js3'

# modules framework
alias dm='cd $TRTOP/site/dust/src/modules'
alias d='cd $TRTOP/site/dust'
alias cm='cd $TRTOP/config/modules.d'
alias tm='cd $TRTOP/tr/com/TripResearch/modules'
alias jsm='cd $TRTOP/site/js3/src/modules'
alias cssm='cd $TRTOP/site/css2/src/modules'
alias td='tweak flush dust'

# svn
alias bdiff='svntr diff -B'

# databases
alias ptma='psql -U tripmaster -h dev-db'
alias ptmo='psql -U tripmonster -h tripmonster'

# misc

# Source additional files
#source ~/.git-completion.bash
