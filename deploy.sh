#!/usr/bin/env bash

create_service_account() {
    ls
    sudo mkdir gs-account
    sudo touch gs-account/account.json
    echo "${SERVICE_ACCOUNT}" > gs-account/account.json
    echo "success!"
}

main(){
    create_service_account
}

main