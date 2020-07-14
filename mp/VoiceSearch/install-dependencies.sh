#! /bin/bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install portaudio19-dev libffi-dev libssl-dev
pip3 install --upgrade google-assistant-sdk[samples]
echo '>>> Goodle SDK support libraries installed'
pip3 install --upgrade google-auth-oauthlib[tool]
echo '>>> Goodle SDK oauth installed'
echo '>>> Authenticating now...'
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --save --headless --client-secrets client_secret_"insert key here"
