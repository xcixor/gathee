#!/usr/bin/env bash

create_service_account() {
    mkdir gs-account
    touch gs-account/account.json
    echo "${SERVICE_ACCOUNT}" > gs-account/account.json
}

main(){
    create_service_account
}

main