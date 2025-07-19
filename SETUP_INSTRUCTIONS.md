# Secure Setup Instructions 🔐

## GitHub Token
The GitHub personal access token is stored securely on the DevOne laptop at:
`/home/chris/claude-space/config/github_token.txt`

Ask Chris to share it with you securely, or create a new one at:
https://github.com/settings/tokens

Required permissions:
- repo (full control)
- workflow (if needed)

## Encryption Key
The encryption key for shared memory is embedded in the sync script.
Check the `github_sync.py` file for the Fernet key.

## Security Notes
- Never commit tokens to the repository
- Store tokens in secure local files
- Use environment variables when possible
- The sync script handles encryption/decryption automatically

---
*For security reasons, sensitive credentials are not stored in the repository*