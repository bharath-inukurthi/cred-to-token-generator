# 🔐 cred-to-token-generator

This script generates a `token.json` file using a `credentials.json` file for Google OAuth 2.0 authorization. It allows developers to quickly acquire access tokens for Google APIs like Gmail, Drive, Calendar, etc.

> ✅ Ideal for developers who want to authenticate using OAuth and test their tokens via an API call.

---

## 📁 Files

- `credentials.json` – Your OAuth 2.0 client credentials (downloaded from Google Cloud Console).
- `token.json` – Generated token file with user credentials (auto-created).
- `requirements.txt` – All dependencies to install before running the script.

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/bharath-inukurthi/cred-to-token-generator.git
   cd cred-to-token-generator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Scopes**
   Open the script and replace:
   ```python
   SCOPES = [
       """add scopes which you want to acquire"""
   ]
   ```
   with actual scopes. Example:
   ```python
   SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
   ```

4. **Add Your Credentials**
   Place your `credentials.json` (from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)) in the root directory.

5. **Ensure Redirect URI is Set**
   In your OAuth 2.0 Client configuration in Google Cloud Console, add the following **Authorized redirect URI**:
   ```
   http://localhost:8000/
   ```
   > ⚠️ This URI **must match the port** used in the script (`run_local_server(port=8000)`). If you change the port (e.g. `port=5000`), make sure to update the redirect URI accordingly (`http://localhost:5000/`).

6. **Run the Script**
   ```bash
   python token_generator.py
   ```

   This will:
   - Open a browser window for authentication.
   - Save `token.json` after successful login.
   - Optionally verify the token with a sample Gmail API call.

---

## 🛠 Sample Use Case

Once the `token.json` is generated, it can be used in any Google API script like so:
```python
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_file('token.json')
```

---

## 🧪 Tested With

- Gmail API (sample call in script)

---

## 📌 Notes

- Use `flow.run_console()` instead of `flow.run_local_server()` if you're running on a headless server (no GUI).
- You can change the port from `8000` to any available port by modifying:
  ```python
  credentials = flow.run_local_server(port=YOUR_PORT)
  ```
- Always keep `credentials.json` and `token.json` secure. Do not expose them in public repositories.

---
