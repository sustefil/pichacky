DROPLET_IDS=$(doctl compute droplet list --format ID --no-header)
DROPLET_IDS=$(echo $DROPLET_IDS | tr ' ' ',')

doctl compute load-balancer create --droplet-ids "$DROPLET_IDS" --name "lb-fra-01" --region "fra1" \
  --forwarding-rules entry_protocol:tcp,entry_port:80,target_protocol:tcp,target_port:8000 \
  --health-check protocol:http,port:8000,path:/ahoj.html,check_interval_seconds:10,response_timeout_seconds:5,healthy_threshold:3,unhealthy_threshold:2
