
# Google Calendar API Python 

## Prerequisites

1. **Google Cloud Console Setup:**
   - Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Calendar API for your project.
   - Create credentials (OAuth client ID) and download the `credentials.json` file.
   - Add `http://localhost:8080/` as an authorized redirect URI in the credentials section.

## Usage

1. Run the script:

   ```bash
   python quickstart.py
   ```

   The script will guide you through the OAuth 2.0 authorization process, and upon successful authorization, it will print the start time and name of the next 10 events on your Google Calendar.

2. If this is your first run, the script will create a `token.json` file to store your access and refresh tokens. Subsequent runs will use this file for authentication.

## Troubleshooting

- If you encounter any issues related to the redirect URI or authorization, double-check your Google Cloud Console settings, especially the authorized redirect URI.

- If you need to reset the authorization, you can delete the `token.json` file and re-run the script.


```

Make sure to replace placeholders like `your-username` and `your-repo` with your actual GitHub username and repository name. Additionally, if your script has a different name, replace `script_name.py` with the correct filename.