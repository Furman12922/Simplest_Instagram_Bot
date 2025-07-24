# Simplest Instagram Bot

This project is a simple Instagram automation bot built using the [instabot](https://github.com/instagrambot/instabot) library. It allows you to automate basic Instagram actions such as logging in, uploading photos, and following users with minimal setup.

## Features
- Log in to Instagram automatically
- Upload photos with captions
- (Optional) Follow users by username

## Setup
1. **Clone this repository** or download the files to your local machine.
2. **Install the required dependencies:**
   
   The main dependency is `instabot`. Install it using pip:
   ```bash
   pip install instabot
   ```
3. **Configure your credentials:**
   
   Open `instagram.py` and replace:
   - `enter your insta user name` with your Instagram username
   - `enter your insta password` with your Instagram password

4. **Set your photo and caption:**
   
   Update the `bot.upload_photo` line with the path to your photo and your desired caption.

## Usage
Run the script using Python:
```bash
python instagram.py
```

## Notes
- The script deletes the `config` folder on each run to avoid login issues.
- Make sure your photo path is correct and the file exists.
- Use this bot responsibly and in accordance with Instagram's terms of service.

## Example
```python
bot = Bot()
bot.login(username="your_username", password="your_password")
bot.upload_photo("path/to/photo.jpg", caption="Your caption here")
```

---

**Disclaimer:** This project is for educational purposes only. Use at your own risk. 