#!/usr/bin/env bash

create_service_account() {
    echo "${SERVICE_ACCOUNT}" > gs-account/account.json
    echo "success!"
}

main(){
    create_service_account
}

main