#!/bin/bash

cd /opt/app/postfix
echo "cp main.cf"
cp -f main.cf /etc/postfix
chmod 644 main.cf
echo "cp sasl_passwd.lmdb"
cp -f sasl_passwd.lmdb /etc/postfix
chmod 600 sasl_passwd.lmdb

# Start mscluster
#echo "postfix start"
#/bin/sh -c /scripts/run.sh

#exec "$@"
