
for i in {1,2}
do
  doctl compute droplet create \
    --image ubuntu-22-04-x64 \
    --size s-1vcpu-2gb \
    --region fra1 \
    --enable-monitoring \
    --ssh-keys 40830502 \
    ubuntu-fra-0${i}
done
