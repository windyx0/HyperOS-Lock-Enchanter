# HyperOS Enchanter 🌟

🌍 **[English](README.md) | [Русский](README_RU.md)**

![HyperOS Enchanter](https://github.com/windyx0/HyperOS-Lock-Enchanter/blob/main/hyperos_logo.jpg)

**HyperOS Enchanter** is an advanced AI-powered wallpaper and theme manager for Xiaomi's HyperOS (and MIUI) devices. 
With its intuitive GUI, you can instantly create stunning wallpapers with perfectly generated alpha masks for depth effects (lock screen clock hiding behind the subject) and effortlessly manage themes directly on your Rooted device!

---

## 🎨 Features

- **AI Mask Generation:** Uses state-of-the-art Neural Networks (`isnet-general-use`, `u2net`, `birefnet-general`) to perfectly cut out the subject and generate a depth mask.
- **Root ADB Integration:** Automatically pushes your generated wallpapers and modifies the `wallpaper_config.json` inside the HyperOS `/product/media/wallpaper` system directory without manual terminal commands.
- **Theme Manager:** Browse, preview, rename, and delete your themes and wallpapers directly from your PC.
- **Custom Masks:** Want absolute precision? Upload your own custom mask image!
- **Dual Language UI:** Fully supports English and Russian (configurable in the Settings tab).
- **Portable Windows EXE:** A fully standalone `.exe` version is available (no Python installation required).

---

## 🚀 Installation & Requirements

Ensure you have Python 3.10+ installed.

**Windows:**
```bat
cd scripts
install.bat
start.bat
```

**Linux/macOS:**
```bash
cd scripts
chmod +x *.sh
./install.sh
./start.sh
```

### Phone Requirements
- Your Xiaomi/POCO device **must be ROOTED** (Magisk/KernelSU).
- You must have **USB Debugging** enabled in Developer Options.
- Connect the phone to your PC via USB and authorize the connection.

---

## 🛠️ Usage Guide

### Tab 1: Wallpaper Creator
1. Click **Select Photo** and choose an image you want as your wallpaper.
2. Wait for the AI to calculate the depth mask (you will see the original image with a red overlay).
3. If the AI didn't catch the horizon properly, select a different model from the dropdown and click **AI Mask**.
4. Type a name for your wallpaper in the text box.
5. Click **Install to Phone (Root)**. Grant Superuser permission on your phone screen if prompted.

### Tab 2: Theme Manager
1. Click **Find all themes on phone**.
2. Select a Theme Folder on the left to see its wallpapers.
3. Select a wallpaper in the middle to preview the image and its mask.
4. You can freely **Rename**, **Delete**, or manage your wallpapers!

---

## ⚙️ Settings & Socials
Check out the **Settings** tab in the app to switch languages or visit my social media pages!
- Telegram: [Join my channel!](https://t.me/your_telegram)
- TikTok: [Follow me!](https://tiktok.com/@your_tiktok)

**Enjoy customizing your HyperOS lock screen!**
