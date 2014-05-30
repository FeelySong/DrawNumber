#!/bin/bash
ROOT="/data/app";
cd "$ROOT";

declare -A daemons;   #定义一个数组，key为目录，val为服务主程序
daemons=(
    ["JZDrawNumber"]="Number.py"
);

checkconfig () {   #检查函数，用来检查daemons数组中配置的程序文件是否存在
    for folder in "${!daemons[@]}";
    do
        file="$folder/${daemons[${folder}]}";
        if [ -f "$file" ]; then
            echo "$file yes.";
        else
            echo "$file no.";
        fi
    done;
}

status () {  #检查daemons数组中配置的所有程序是否正在运行
    if [ -z "$1" ]; then
        for folder in "${!daemons[@]}";
        do
            daemon="${daemons[${folder}]}";
            pid=$(ps aux|grep "\./$daemon"|grep -v grep|awk '{print $2}');
            if [ -n "$pid" ]; then
                echo "$daemon is running, pid: $pid";
            else
                echo "$daemon is not running";
            fi
        done
    else
        pid=$(ps aux|grep "\./$1"|grep -v grep|awk '{print $2}');
        echo $pid;
    fi
}

stop () { #停止daemons数组中配置的所有程序
    if [ -z "$1" ]; then
        for folder in "${!daemons[@]}";
        do
            daemon="${daemons[${folder}]}";
            pid=$(status $daemon);
            if [ -n "$pid" ]; then
                kill -9 "$pid";
                pid=$(status $daemon);
                if [ -z "$pid" ]; then
                    echo "$folder stop success";
                else
                    echo "$folder stop fail";
                fi
            else
                echo "$folder is not running";
            fi
        done
    else
        folder=$1;
        daemon="${daemons[${folder}]}";
        if ! [ -d "$ROOT/$folder" ] || ! [ -f "$ROOT/$folder/$daemon" ]; then
            echo "error: daemon $folder not exists;";
            return;
        fi
        pid=$(status $daemon);
        if [ -z "$pid" ]; then
            echo "$daemon is not running";
            return;
        fi
        kill -9 "$pid";
        pid=$(status $daemon);
        if [ -z "$pid" ]; then
            echo "$daemon stop success";
        else
            echo "$daemon stop fail, pid: $pid";
        fi
    fi
}

start () { #启动daemons数组中配置的所有程序
    if [ -z "$1" ]; then
        for folder in "${!daemons[@]}";
        do
            daemon="${daemons[${folder}]}";
            pid=$(status $daemon);
            if [ -n "$pid" ]; then
                echo "$daemon is running, pid: $pid;";
                continue;
            fi
            cd "$ROOT/$folder";
            if [ -f "$daemon" ]; then
                #chmod a+x "$daemon";
                nohup "/usr/local/python2.7/bin/python2.7 $daemon" & > /dev/null
                pid=$(status $daemon);
                if [ -n "$pid" ]; then
                    echo "$daemon start success, pid: $pid;";
                else
                    echo "$daemon start fail;";
                fi
            else
                echo "error: daemon $daemon not exists;";
            fi
        done;
    else
        folder=$1;
        daemon="${daemons[${folder}]}";
        if ! [ -d "$ROOT/$1" ] || ! [ -f "$ROOT/$folder/$daemon" ]; then
            echo "error: daemon $folder not exists;";
            return;
        fi
        pid=$(status $daemon);
        if [ -n "$pid" ]; then
            echo "$daemon is running, pid: $pid;";
            return;
        fi
        cd "$ROOT/$folder";
        chmod a+x "$daemon";
        nohup "./$daemon" & > /dev/null
        pid=$(status $daemon);
        if [ -n "$pid" ]; then
            echo "$daemon start success, pid: $pid;";
        else
            echo "$daemon start fail;";
        fi
    fi
}

#程序主入口
if [ -n "$1" ]; then
    case "$1" in
        "checkconfig" )
            checkconfig;;
        "status" )
            status "$2";;
        "start" )
            start "$2";;
        "stop" )
            stop "$2";;
        "restart" )
            stop "$2";
            start "$2";;
        "cleanlog" )
            stop;
            rm -rf `find $ROOT -name *.log`
            rm -rf `find $ROOT -name *.out`
            start;;
    esac
fi