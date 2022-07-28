# Hyperx Cloud II Wireless Battery level

## Installation/Dependencies


python3 `hidapi` library.
https://pypi.org/project/hidapi/

```bash
pip install hidapi
```

(tested with `hidapi==0.12.0.post2`)


### Permissions
`/etc/udev/rules.d/99-hidraw.rules`

```
KERNEL=="hidraw*", ATTRS{idVendor}=="0951", ATTRS{idProduct}=="1718", GROUP="plugdev", MODE="0660"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0951", ATTRS{idProduct}=="1718", GROUP="plugdev", MODE="0660"
```

Run following command to create the rule:
```bash
echo 'KERNEL=="hidraw*", ATTRS{idVendor}=="0951", ATTRS{idProduct}=="1718", GROUP="plugdev", MODE="0660"' | sudo tee /etc/udev/rules.d/99-hidraw.rules
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0951", ATTRS{idProduct}=="1718", GROUP="plugdev", MODE="0660"' | sudo tee -a /etc/udev/rules.d/99-hidraw.rules
```

### Reboot
reboot the system to reload udev rules.


## Usage

```bash
python3 battery.py
```


## References
hidapi: https://pypi.org/project/hidapi/

Cloud flight kondinskis repository:  https://github.com/kondinskis/hyperx-cloud-flight

Cloud flight srn repository: https://github.com/srn/hyperx-cloud-flight-wireless

