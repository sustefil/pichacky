curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

#echo "$nrconf{restart} = 'l';" >> /etc/needrestart/needrestart.conf

sudo apt update -y
sudo apt install -y fontconfig openjdk-17-jre
sudo apt install -y jenkins

#sudo systemctl start jenkins.service

