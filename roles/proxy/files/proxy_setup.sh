#!/bin/bash

echo 'http_proxy="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"' >> /etc/environment
echo 'https_proxy="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"' >> /etc/enviroment
echo 'no_proxy=".mobi.ch,.mobicorp.ch,.mobicorp.test,localhost"' >> /etc/enviroment

echo 'HTTP_PROXY="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"' >> /etc/enviroment
echo 'HTTPS_PROXY="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"' >> /etc/environment
echo 'NO_PROXY=".mobi.ch,.mobicorp.ch,.mobicorp.test,localhost"' >> /etc/environment


export http_proxy="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"
export https_proxy="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"
export no_proxy=".mobi.ch,.mobicorp.ch,.mobicorp.test,localhost"

export HTTP_PROXY="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"
export HTTPS_PROXY="http://Z100805:Dc24Wt54Mn@dirproxy.mobi.ch:80"
export NO_PROXY=".mobi.ch,.mobicorp.ch,.mobicorp.test,localhost"

source /etc/environment