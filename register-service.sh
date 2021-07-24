#!/bin/bash
# Creates service for pinion.weather

default_port=5000
default_workers=3
directory=$(dirname -- $(readlink -fn -- "$0"))

printf "This script will setup pinion.weather as a service\n"
printf "Are you ok with this?\n"

select yn in "Yes" "No"; do
    case $yn in
        Yes )

            break;;

        No )

            # Exit script
            exit 0;;
    esac
done

printf "What port would you like the pinion.weather.service to run on?\n"
read -p "(DEFAULT=5000)" port

if [ -z "$port" ]
  then
    port=$default_port
fi

printf "Using port $port\n"

printf "How many workers would you like to assign to pinion.weather?\n"
printf "recommended formula is 1 + 2 * NUM_CORES\n"
read -p "(DEFAULT=3)" workers

if [ -z "$workers" ]
  then
    workers=$default_workers
fi

printf "Using $workers workers\n"

cat >> pinion.weather.service <<EOF
[Unit]
Description=pinion.weather service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=${USER}
ExecStart=${directory}/venv/bin/gunicorn -w ${workers} --bind 0.0.0.0:${port} app:app --chdir ${directory}

[Install]
WantedBy=multi-user.target
EOF

sudo mv pinion.weather.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start pinion.weather
sudo systemctl enable pinion.weather