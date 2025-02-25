# **Set-Up**

## **1. Download the Required Files**
Download both files from the latest [Releases](https://github.com/jajtxs/jajts-tools/releases/latest):  
🔗 [**dependencies.py**](https://github.com/jajtxs/jajts-tools/releases/download/BETA/dependencies.py)  
🔗 [**jajts-tools.py**](https://github.com/jajtxs/jajts-tools/releases/download/BETA/jajts-tools.py)  

## **2. Install Requirements**

- **Python:** Ensure you have Python installed. If not, download it [here](https://www.python.org/downloads/) and install it.
- **Tesseract OCR (Optional, for OCR feature):**  
  - Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe).  
  - Make sure it is added to **system PATH** during installation.

## **3. Running the Program**

Open a terminal (Windows users: `Win + R` → type `cmd` → press Enter).  

### **Navigate to your Downloads folder:**  
```sh
cd C:\Users\YOUR_USERNAME\Downloads
```
*(Replace `YOUR_USERNAME` with your actual Windows username.)*

### **Run the dependencies installer:**  
```sh
py dependencies.py
```
- This will install the required Python packages.  
- **Must be run before `jajts-tools.py` or the program won’t work.**  

### **Run the main program:**  
```sh
py jajts-tools.py
```
- This file is **obfuscated** but safe.  
- If you’re concerned, you can check it on [VirusTotal](https://www.virustotal.com/gui/file/33990a751e5551caac06ff5b05e8e4648f1d9fca55ab048516d6301410ef8953) (last scan: **0/62 detected**).  

---

# **Key System 🔑**  
This program requires a **key** to access its features.  

### **How to Get a Key:**  
- Join the Discord server (**link available in the latest release description**).  
- During **BETA**, keys are **free**.  
- After BETA, premium features (OCR & Premium Account Generator) will require a **paid token**, while basic features (API & Basic Account Generator) will remain **free**.  

⚠️ **Attempting to bypass the key system may result in a blacklist.**  

---

# **FAQs**  

### **1. What features are coming next?**  
- **Expanded API support** (currently pets, will include enchants, potions, event items, etc.).  
- **New Gamepass Notifications** via Discord webhook (will work externally, no need to keep the program running).  

### **2. When will BETA end?**  
- No fixed date yet. It will exit BETA once the **Account Generator** is stable.  

### **3. How often are updates?**  
- `jajts-tools.py` is updated **only when new features are added**.  
- `dependencies.py` **rarely needs updates**, but always download the latest version before running `jajts-tools.py`.  

---

# **Troubleshooting & Common Issues**  

### **"Python is not recognized as an internal or external command."**  
- Install Python and restart your terminal.  
- Verify installation by running:  
  ```sh
  python --version
  ```  

### **"Tesseract OCR is not found."**  
- Ensure Tesseract is installed and added to **system PATH**.  
- Test by running:  
  ```sh
  tesseract --version
  ```  

### **"Key is invalid."**  
- Ensure you entered the key **exactly** as provided.  
- If issues persist, contact support in Discord. 

![image](https://github.com/user-attachments/assets/569a1428-920f-4e5e-9b33-ed6d905d3457)
*API Probe example.*

![image](https://github.com/user-attachments/assets/7ee50ee8-2c8b-45c6-b329-e423ef583cae)
*Verification needed webhook / Acc Gen. Premium will allow for automatic verification, however that functionality is not yet released.*

![image](https://github.com/user-attachments/assets/e8acf17d-6cb0-43a4-9832-5210b71d33dc)
*sample OCR webhook image.*
