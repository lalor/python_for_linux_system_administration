for ip in `cat ips.txt`
do
    if ping $ip -c 2 &> /dev/null
    then
        echo "$ip is alive"
    else
        echo "$ip is unreachable"
    fi
done
