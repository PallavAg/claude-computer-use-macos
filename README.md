# Claude Computer Use Demo for MacOS

This repository contains a Python script that demonstrates Anthropic's Computer Use capabilities, modified to run on MacOS without requiring a Docker container. The script allows Claude 3.5 Sonnet to perform tasks on your Mac by simulating mouse and keyboard actions as well as running bash command.

Forked from Anthropic's [computer use demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) - optimized for MacOS.
View Anthropic's docs [here](https://docs.anthropic.com/en/docs/build-with-claude/computer-use).

> [!WARNING]  
> Use this script with caution. Allowing Claude to control your computer can be risky. By running this script, you assume all responsibility and liability.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PallavAg/claude-computer-use-macos.git
   cd claude-computer-use-macos
   ```

2. **Create a virtual environment + install dependencies:**

   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   pip3.12 install -r requirements.txt
   ```

3. **Set your Anthropic API key as an environment variable:**

   ```bash
   export ANTHROPIC_API_KEY="CLAUDE_API_KEY"
   ```

   Replace `CLAUDE_API_KEY` with your actual Anthropic API key. You find yours [here](https://console.anthropic.com/settings/keys).

4. **Grant Accessibility Permissions:**

   The script uses `pyautogui` to control mouse and keyboard events. On MacOS, you need to grant accessibility permissions. These popups should show automatically the first time you run the script so you can skip this step. But to manually provide permissions:

   - Go to **System Preferences** > **Security & Privacy** > **Privacy** tab.
   - Select **Accessibility** from the list on the left.
   - Add your terminal application or Python interpreter to the list of allowed apps.

## Usage

You can run the script by passing the instruction directly via the command line or by editing the `main.py` file.

**Example using command line instruction:**

```bash
python3.12 main.py 'Open Safari and look up Anthropic'
```

Replace `'Open Safari and look up Anthropic'` with your desired instruction.

**Note:** If you do not provide an instruction via the command line, the script will use the default instruction specified in `main.py`. You can edit `main.py` to change this default instruction.

## Running Tests

To run the tests using `pytest`, follow these steps:

1. **Install `pytest` if you haven't already:**

   ```bash
   pip install pytest
   ```

2. **Run the tests:**

   ```bash
   pytest
   ```

This will automatically discover and run all the test files in the `tests` directory.

## Exiting the Script

You can quit the script at any time by pressing `Ctrl+C` in the terminal.

## ⚠ Disclaimer

> [!CAUTION]
> - **Security Risks:** This script allows claude to control your computer's mouse and keyboard and run bash commands. Use it at your own risk.
> - **Responsibility:** By running this script, you assume all responsibility and liability for any results.
