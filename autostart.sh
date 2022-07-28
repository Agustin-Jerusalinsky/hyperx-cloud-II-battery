echo "[Desktop Entry]" > ~/.config/autostart/cloud_II.desktop
echo "Type=Application" >> ~/.config/autostart/cloud_II.desktop
echo "Name=Cloud II" >> ~/.config/autostart/cloud_II.desktop
dir=$(pwd)
path=$dir/panel.py
echo "Exec=python3 ${path}" >> ~/.config/autostart/cloud_II.desktop