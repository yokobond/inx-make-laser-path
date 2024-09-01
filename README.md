# inx-make-laser-path


## Description

This is an Inkscape extension for creating laser-cuttable paths from your designs. It simplifies the process of preparing artwork for laser cutting by:

- **Generating offset paths:** Creates an offset path around your selected objects, maintaining the desired cutting width.
- **Customizable offset distance:**  Specify the desired spacing between the original path and the laser-cut path.


This extension is particularly useful when working with laser cutters that require a specific kerf width for precise cutting.

## Installation

1. **Prerequisites:**
   - Inkscape (version 1.0 or later recommended) installed on your system.
   - Python 3 installed on your system. 

2. **Download the extension:**
   - Download the latest release ZIP file from the [Releases](link-to-releases-page) section of this repository.

3. **Install the extension:**
   - Start Inskscape.
   - Go to the **Extensions > Manage Extensions...** menu.
   - Open the **Install Pakcages** tab.
   - Click the folder icon next to the **Install Package** button.
   - Choose the ZIP file you downloaded in step 2.
   - Click **Install**.

##  Using the Extension

1. **Open your design:** Launch Inkscape and open the SVG file containing the artwork you want to laser cut.

2. **Select objects:** Select the objects or paths for which you want to create laser-cuttable paths.

3. **Access the extension:**
   - Go to the  **Extensions > TukuMana > Make Laser Path**.

4. **Set offset width:** In the extension dialog, enter the desired width to leave between the laser path in millimeters (mm).

5. **Apply:** Click "Apply" to generate the offset paths.

## Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yokobond/inx-make-laser-path.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd inx-make-laser-path
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Install the extension by running the setup script:**
   ```bash
   poetry run poe setup
   ```

   - This script assumes your Inkscape extensions directory is set in the environment variable `INKSCAPE_EXTENSIONS_DIR`. If not, you can manually make a symbolic link of the `inx_make_laser_path` folder in the project directory to your Inkscape extensions directory.

5. **Build the extension:**

   ```bash
   poetry run poe build
   ```

   This command creates a ZIP file of the extension in the `build` directory. You can install this ZIP file as described in the "Installation" section. 

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


