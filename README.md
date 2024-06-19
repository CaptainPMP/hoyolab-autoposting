# Automated Posting on Hoyolab

This script automates the process of posting on Hoyolab using `pyautogui`. It identifies specific templates on the screen and performs actions like clicking and typing text.

## Prerequisites

- Python 3.x installed on your system
- `pyautogui` library installed

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/yourusername/hoyolab-autoposting.git
    cd hoyolab-autoposting
    ```

2. **Install the required Python package:**

    ```bash
    pip install pyautogui
    ```

## Usage

1. **Prepare Your Environment:**

    - Ensure you have the required template images saved in the same directory as `main.py`. These images should be screenshots of the specific buttons and areas you want to interact with on Hoyolab.

2. **Open the Hoyolab Post Page:**

    - Navigate to the Hoyolab post page that includes the pencil sticker (indicating a new post can be created).

3. **Run the Script:**

    - Execute the script by running:

    ```bash
    python main.py
    ```

4. **Switch to the Target Window:**

    - After running the script, you will have a few seconds (default is 5 seconds) to switch to the Hoyolab window.

## How It Works

The script follows these steps:
1. Moves the mouse to specific template images (e.g., title input, context input) and performs actions like clicking and typing text.
2. Scrolls the page if necessary to find and interact with other elements.
3. Posts the content on Hoyolab.

## Customization

- **Adjusting Template Images:**
  - If the templates provided do not match your screen or the Hoyolab layout, update the template images accordingly.
  
- **Changing the Text:**
  - Modify the text strings within the `main.py` file to customize your post content.

## Troubleshooting

- If the script cannot find a template image:
  - Ensure the template image is correct and clearly represents the UI element.
  - Adjust the `confidence` parameter in the `move_to_template_and_click` function to make the image matching more lenient or strict.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
