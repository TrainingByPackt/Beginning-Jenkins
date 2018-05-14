#!/bin/bash
# Install Java
sudo yum install java-1.8.0-openjdk -y
java -version

# Install Jenkins
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install jenkins -y

# Start Jenkins & ensure Jenkins is started at startup
sudo service jenkins start
sudo chkconfig jenkins on

# Disable Firewall To Allow Port Forwarding To Host
sudo service iptables stop
