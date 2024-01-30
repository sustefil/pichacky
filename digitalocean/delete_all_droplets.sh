for id in $(doctl compute droplet list --format ID |tail +2); do doctl compute droplet delete $id; done
