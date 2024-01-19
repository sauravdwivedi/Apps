# Python program to optimize charging and improve battery life

## Instalation

### Run manually

```bash
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 battery.py
```

Make alias

```bash
echo "alias battery='python3 path-to-battery.py'" >> ~/.zshrc
```

### Run in the background as a service

Make ~/Library/LaunchAgents/battery.plist file with following content

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST 1.0//EN http://www.apple.com/DTDs/PropertyList-1.0.dtd >
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>battery</string>
    <key>Program</key>
    <string>/Users/sdwivedi/battery.py</string>
    <key>KeepAlive</key>
    <true/>
  </dict>
</plist>
```

Load and run the program

```bash
launchctl load ~/Library/LaunchAgents/battery.plist
```

Remove the program 

```bash
launchctl unload ~/Library/LaunchAgents/battery.plist
```

Find the program

```bash
System Settings > General > Login Items
```
