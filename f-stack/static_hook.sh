#!/bin/bash

hook_functions=(fcntl sysctl ioctl socket setsockopt getsocketopt listen bind accept connect close shutdown getpeername getsockname read readv write writev send sendto sendmsg recv recvfrom recvmsg select poll kqueue kevent kevent_do_each epoll_create epoll_ctl epoll_wait gettimeofday dup dup2)

for function_name in ${hook_functions[@]}
do
    objcopy --redefine-sym ${function_name}=ff_${function_name} $@ 
done
