#!/bin/bash

install_gcloud_and_gsutil() {

  # Skip if already installed
  if command -v gcloud >/dev/null 2>&1 && command -v gsutil >/dev/null 2>&1; then
    echo "✅ Google Cloud CLI and gsutil already installed."
    return 0
  fi

  echo "Adding Google Cloud SDK repository..."
  echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | \
    sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

  echo "Importing Google Cloud GPG key..."
  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg

  echo "Updating package list and installing Google Cloud CLI..."
  sudo apt-get update -y && sudo apt-get install google-cloud-cli -y

  echo "Downloading and installing gsutil..."
  wget https://storage.googleapis.com/pub/gsutil.zip && \
    unzip gsutil.zip && \
    rm gsutil.zip && \
    sudo mv gsutil /usr/local/bin

  echo "✅ Installation complete."
}

# Check if a project ID was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <gcp_project_id>"
  exit 1
fi

# Export the project ID
export gcp_dev_project_id="$1"

echo "Using project ID: $gcp_dev_project_id :)"
read -p "Press Enter to continue..."

install_gcloud_and_gsutil

# Run GCP authentication and configuration commands
gcloud auth login --no-launch-browser
gcloud auth application-default login --no-launch-browser
gcloud config set project "$gcp_dev_project_id"
gcloud auth application-default set-quota-project "$gcp_dev_project_id"
gcloud config list
