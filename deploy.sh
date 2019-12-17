#!/usr/bin/env bash

sleep 1m

create_service_account() {
    mkdir gs-account
    touch gs-account/account.json
    echo "${SERVICE_ACCOUNT}" > gs-account/account.json
    echo "success!"
}

main(){
    create_service_account
}

main