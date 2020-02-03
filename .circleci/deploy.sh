set -o errexit
set -o pipefail

download_terraform() {
    wget https://releases.hashicorp.com/terraform/0.12.19/terraform_0.12.19_linux_amd64.zip
    unzip terraform_0.12.19_linux_amd64.zip
    chmod +x terraform
    sudo mv terraform /usr/local/bin/
}

prepare_deployment_script() {
    cd ~
    git clone -b develop https://github.com/xcixor/gathee-deployment.git
    cd ~/gathee-deployment/account
    touch account.json
    echo "${SERVICE_ACCOUNT}" > account.json
}

check_branch(){
    if [[ "$BRANCH" == 'develop' ]]; then
        export ENVIRONMENT="staging"
        export DJANGO_SETTINGS_MODULE=core.settings.${ENVIRONMENT}
        echo "${STAGING_ENVIRONMENTAL_VARIABLES}" | base64 -di > ~/gathee-deployment/infrastructure/terraform.tfvars
    elif [[ "$BRANCH" == 'master' ]]; then
        export ENVIRONMENT="production"
        export DJANGO_SETTINGS_MODULE=core.settings.${ENVIRONMENT}
        echo "${PRODUCTION_ENVIRONMENTAL_VARIABLES}" | base64 -di > ~/gathee-deployment/infrastructure/terraform.tfvars
    else
        export ENVIRONMENT="staging"
        export DJANGO_SETTINGS_MODULE=core.settings.${ENVIRONMENT}
        echo "${INTEGRATION_ENVIRONMENTAL_VARIABLES}" | base64 -di > ~/gathee-deployment/infrastructure/terraform.tfvars
    fi
}

initialise_terraform() {
    cd ~/gathee-deployment/infrastructure/
    terraform init -lock=false -backend-config=bucket="${GS_BUCKET_NAME}" \
        -backend-config=prefix="/infrastructure-terraform/${ENVIRONMENT}/terraform.tfstate"
}

destroy_previous_infrastructure(){
    terraform destroy -lock=false -auto-approve -var=github_branch="${BRANCH}" -var=django_environment="${ENVIRONMENT}" -var=gs_credentials="${SERVICE_ACCOUNT}"
}

build_current_infrastructure() {
    terraform apply -lock=false -auto-approve -var=github_branch="${BRANCH}" -var=django_environment="${ENVIRONMENT}" -var=gs_credentials="${SERVICE_ACCOUNT}"
}

destroy_infrastructure() {
    download_terraform
    prepare_deployment_script
    check_branch
    initialise_terraform
    destroy_previous_infrastructure
}

create_infrastructure() {
    destroy_infrastructure
    build_current_infrastructure
}
"$@"
