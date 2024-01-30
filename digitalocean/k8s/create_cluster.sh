doctl kubernetes cluster create pichacky-cluster --tag pichacky --auto-upgrade=true --node-pool "name=mypool;count=2;auto-scale=true;min-nodes=1;max-nodes=3;tag=pichacky"
