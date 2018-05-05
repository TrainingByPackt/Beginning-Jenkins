# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # Jenkins Master Server
  config.vm.define "master" do |master|
    master.vm.box = "nrel/CentOS-6.5-x86_64"
    master.vm.hostname = "master"
    master.vm.network "private_network", ip: "192.168.1.10"
    master.vm.network "forwarded_port", guest: 8080, host: 8080
    master.vm.provision "shell", path: "provision_master.sh"
  end

  # Slave Node 1
  config.vm.define "node1" do |node1|
    node1.vm.box = "nrel/CentOS-6.5-x86_64"
    node1.vm.hostname = "node1"
    node1.vm.network "private_network", ip: "192.168.1.20"
    node1.vm.provision "shell", path: "provision_slave.sh"
  end

  # Slave Node 2
  config.vm.define "node2" do |node2|
    node2.vm.box = "nrel/CentOS-6.5-x86_64"
    node2.vm.hostname = "node2"
    node2.vm.network "private_network", ip: "192.168.1.30"
    node2.vm.provision "shell", path: "provision_slave.sh"
  end
end
