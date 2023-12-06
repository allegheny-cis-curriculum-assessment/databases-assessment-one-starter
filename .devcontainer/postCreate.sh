#!/bin/bash
# Install new dependencies
pipx install gatorgrade
# Set the aliases
echo "alias evalugator='gatorgrade --config config/gatorgrade.yml'" >> ~/.bashrc
source ~/.bashrc