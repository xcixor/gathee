#! /bin/bash

# echo "$GOOGLE_JSON_CREDENTIALS" > src/core/account.json
echo "${SERVICE_ACCOUNT}" > src/core/account.json

# create_service_account() {
#     mkdir gs-account
#     touch gs-account/account.json
    # echo "${SERVICE_ACCOUNT}" > gs-account/account.json
#     echo "success!"
# }

# main(){
#     create_service_account
# }

# main