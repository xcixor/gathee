#!/usr/bin/env bash

create_service_account() {
    ls
    mkdir gs-account
    touch gs-account/account.json
    echo "${SERVICE_ACCOUNT}" > gs-account/account.json
    echo "success!"
}

main(){
    create_service_account
}

main