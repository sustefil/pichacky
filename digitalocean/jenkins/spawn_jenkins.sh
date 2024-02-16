doctl compute droplet create \
    --image 149803532 \
    --size s-1vcpu-1gb \
    --region fra1 \
    --vpc-uuid 915a4ee9-ecef-4cbe-a2b0-fafefa349ecb \
    --ssh-keys 40830502 \
    ubuntu-jenkins-22-s-1vcpu-1gb-fra1-01
