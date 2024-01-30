for id in $(doctl compute lb list --format ID --no-header); do doctl compute lb delete $id; done
