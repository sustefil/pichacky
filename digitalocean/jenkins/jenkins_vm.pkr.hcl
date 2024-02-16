packer {
  required_plugins {
    digitalocean = {
      source  = "github.com/digitalocean/digitalocean"
      version = ">= 1.2.1"
    }
  }
}

variable "do_token" {
  type    = string
  default = ""
}

source "digitalocean" "jenkins-ubuntu-22" {
  api_token    = "${var.do_token}"
  image        = "ubuntu-22-04-x64"
  region       = "fra1"
  size         = "s-1vcpu-1gb"
  ssh_username = "root"
}

build {
  sources = ["source.digitalocean.jenkins-ubuntu-22"]

  provisioner "file" {
    destination = "/tmp"
    source      = "configs/"
  }

  provisioner "shell" {
    scripts = ["scripts/install_jenkins.sh"]
  }

}
