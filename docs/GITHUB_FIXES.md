# GitHub Repository Fixes and Sync Guide

## 📋 Summary of Changes

This document explains all the errors found in your GitHub repository and how to fix them.

---

## ❌ Errors Found

### 1. `esphome/brook_sensor_node.yaml`
**Error:** Line 49-50 has `floa\nt` (split across lines)  
**Fix:** Changed to `float`

```yaml
# BEFORE (ERROR):
            float voltage = id(level_raw).state / 1000.0;

# AFTER (FIXED):
            float voltage = id(level_raw).state / 1000.0;
```

### 2. `esphome/brook_air_quality.yaml`
**Error:** Line 58-59 has `da\nta` (split across lines)  
**Fix:** Changed to `data`

```yaml
# BEFORE (ERROR):
        {"value_type": "pressure", "value": )" + to_string(id(pressure).state / 100.0) + R"("}

# AFTER (FIXED):
        {"value_type": "pressure", "value": ")" + to_string(id(pressure).state / 100.0) + R"("}
```

### 3. `esphome/secrets.yaml`
**Error:** Contains full `brook-Gateway.yaml` content instead of secrets template  
**Fix:** Replaced with proper secrets template

```yaml
# BEFORE (ERROR): Full gateway YAML file

# AFTER (FIXED):
# ESPHome Secrets Template
wifi_ssid: "YourWiFiSSID"
wifi_password: "YourWiFiPassword"
mqtt_broker: "192.168.1.10"
mqtt_user: "mqtt_user"
mqtt_password: "mqtt_password"
```

### 4. `LICENSE.txt`
**Error:** Contains markdown artifacts (`## File 2: LICENSE`, backticks, etc.)  
**Fix:** Replaced with clean MIT License text

### 5. `home-assistant/ui-lovelace.yaml`
**Error:** Indentation error with `\n    red: 50`  
**Fix:** Proper YAML indentation

```yaml
# BEFORE (ERROR):
        severity:
          green: 0
          yellow: 25
          \n    red: 50

# AFTER (FIXED):
        severity:
          green: 0
          yellow: 25
          red: 50
```

### 6. `docs/wiring.md`
**Error:** Saved as RTF format with control codes  
**Fix:** Converted to proper Markdown with clean formatting

### 7. `gitignore.txt`
**Error:** Wrong filename (should be hidden `.gitignore`)  
**Fix:** Renamed to `.gitignore` with proper content

---

## 📥 How to Sync Your Local Folder with GitHub

### Method 1: Using Git Command Line (Recommended)

#### Step 1: Clone the Repository (if you haven't already)
```bash
cd /path/to/your/projects
git clone https://github.com/geert2/citizen-science-Brook-monitoring-.git
git cd citizen-science-Brook-monitoring-
```

#### Step 2: Pull the Latest Changes
```bash
# Navigate to your repository
cd /path/to/citizen-science-Brook-monitoring-

# Pull the latest changes from GitHub
git pull origin main
```

#### Step 3: Copy Your Corrected Files
```bash
# Copy all corrected files from this session
# Replace /workspace/... with your actual path
cp /workspace/github__geert2__citizen-science-Brook-monitoring-/* .
cp /workspace/github__geert2__citizen-science-Brook-monitoring-/.gitignore .
```

#### Step 4: Commit and Push the Changes
```bash
# Add all corrected files
git add .

# Commit with a descriptive message
git commit -m "Fix YAML errors, replace secrets.yaml, fix LICENSE, fix wiring.md format, add sensor_choices.md"

# Push to GitHub
git push origin main
```

### Method 2: Using GitHub Web Interface

#### Step 1: Download Corrected Files
1. Download each corrected file from this conversation
2. Save them to your computer

#### Step 2: Upload to GitHub
1. Go to your repository: https://github.com/geert2/citizen-science-Brook-monitoring-
2. Click on each file you want to replace
3. Click the pencil (edit) icon
4. Delete the old content
5. Paste the new content
6. Click "Commit changes"

**OR** (for new files):
1. Click "Add file" → "Upload files"
2. Drag and drop the new files
3. Click "Commit changes"

### Method 3: Using GitHub Desktop

1. Install GitHub Desktop: https://desktop.github.com/
2. Clone your repository
3. Copy the corrected files into the local folder
4. GitHub Desktop will detect changes
5. Write a commit message and click "Commit to main"
6. Click "Push origin" to sync with GitHub

---

## 📁 Files Changed Summary

| File | Status | Action |
|------|--------|--------|
| `esphome/brook_sensor_node.yaml` | ❌ Error → ✅ Fixed | Fixed `float` typo |
| `esphome/brook_air_quality.yaml` | ❌ Error → ✅ Fixed | Fixed `data` typo |
| `esphome/secrets.yaml` | ❌ Wrong content → ✅ Fixed | Replaced with secrets template |
| `LICENSE.txt` | ❌ Formatting → ✅ Fixed | Clean MIT License |
| `home-assistant/ui-lovelace.yaml` | ❌ Indentation → ✅ Fixed | Fixed YAML formatting |
| `docs/wiring.md` | ❌ RTF format → ✅ Fixed | Converted to Markdown |
| `gitignore.txt` | ❌ Wrong name → ✅ Fixed | Renamed to `.gitignore` |
| `docs/sensor_choices.md` | ➕ New | Added sensor justification document |

---

## 🔍 How to Verify the Fixes

### Check YAML Syntax

```bash
# Install ESPHome
pip install esphome

# Check each YAML file
cd /path/to/citizen-science-Brook-monitoring-
esphome check esphome/brook_sensor_node.yaml
esphome check esphome/brook_air_quality.yaml
esphome check esphome/brook-Gateway.yaml
```

All files should compile without errors.

### Check Markdown Files

Open the Markdown files in a text editor or Markdown viewer to ensure they render correctly (no RTF codes, proper formatting).

---

## 🎯 Next Steps After Fixing

1. ✅ **Fix all errors** in your GitHub repository
2. ⏳ **Order CN3791** (MPPT charger) to replace XL6019
3. ⏳ **Test ESPHome configurations** when sensors arrive
4. ⏳ **Deploy and test** the full system
5. ⏳ **Monitor data** in Home Assistant and sensor.community

---

## 💡 Additional Notes

### About XL6019
You mentioned you bought XL6019 based on earlier recommendations. **This was incorrect advice** - XL6019 is a DC-DC converter, NOT an MPPT charger. For your solar panel (12V nominal, 19V open circuit) charging 1S Li-ion batteries, you need:
- **CN3791** (12V version) - proper MPPT charger
- **OR** LM2596 buck converter + TP4056 (less efficient, but works)

### Battery Configuration
Your batteries are **2× 18650 in parallel (1S2P)**, NOT series. This means:
- Voltage: 3.7V (same as single cell)
- Capacity: 2× (double the mAh)
- Compatible with: TP4056, CN3791, Heltec V3

### Sensor Delivery
You're waiting for sensors from China. Once they arrive:
1. Test each sensor individually
2. Calibrate according to `docs/calibration.md`
3. Assemble according to `docs/wiring.md`
4. Flash ESPHome firmware
5. Deploy and monitor

---

## 📞 Need Help?

If you get stuck:
1. **Git issues**: Check GitHub's documentation or use GitHub Desktop
2. **YAML errors**: Run `esphome check filename.yaml` for detailed errors
3. **Hardware questions**: Refer to `docs/wiring.md` and `docs/sensor_choices.md`
4. **General questions**: Just ask!

---

*Last updated: November 2025*
