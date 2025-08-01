#!/bin/bash

SERVICE_NAME="updatemanagementpy"
PYTHON_SCRIPT_PATH="/home/$(whoami)/Desktop/auto_update/automation.py"
SERVICE_DIR="$HOME/.config/systemd/user"
SERVICE_FILE="${SERVICE_DIR}/${SERVICE_NAME}.service"

mkdir -p "${SERVICE_DIR}"

cat << EOF > "${SERVICE_FILE}"
[Unit]
Description=Python Script User Service
After=default.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 ${PYTHON_SCRIPT_PATH}
Restart=on-failure
WorkingDirectory=$(dirname ${PYTHON_SCRIPT_PATH})
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=default.target
EOF

echo "Created user service file at ${SERVICE_FILE}"

systemctl --user daemon-reload
systemctl --user enable ${SERVICE_NAME}.service
systemctl --user start ${SERVICE_NAME}.service

echo "User service ${SERVICE_NAME} enabled and started."
echo "It will run automatically on your user login."


















