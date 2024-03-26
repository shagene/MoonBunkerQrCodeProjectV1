# User Guide for Custom QR Code Generator

This comprehensive guide is designed to help you navigate and utilize the Custom QR Code Generator, a powerful tool that creates personalized QR codes for your business or event. Each QR code includes a unique identifier (UUID) and displays the company name for easy identification. Here’s how to use the tool, with all the details explained simply.

## What Is This Tool For?

This tool is ideal for businesses, event organizers, or anyone needing to create QR codes that:

- Link to a unique identifier for each entity (such as a company or product).
- Need to display a company name or other text alongside the QR code.
- Require a specific color scheme to align with branding.
- Must be positioned precisely for design purposes.

## Preparations Before You Start

To ensure a smooth experience, please have the following ready:

- **An active internet connection**: The tool is hosted on Replit and runs in the cloud.
- **A CSV file named `data.csv`**: It should have two columns: `Company Name` and `UUID`. Ensure there are no extra spaces or special characters that might interfere with the QR code generation.

Example CSV content:
```
Company Name,UUID
Coffee Shop,123e4567-e89b-12d3-a456-426614174000
Ice Cream Parlor,987e6543-e21c-34d2-a457-526314175000
```

## Accessing and Using the Tool

1. **Go to Replit**: Open your web browser and navigate to the Replit project page where the QR code generator is deployed.

2. **Prepare Your Data File**: Ensure your CSV file is named `data.csv` and contains the necessary data in the format mentioned above.

3. **Upload the CSV File**: Within the Replit interface, there will be an option to upload files. Select your `data.csv` and upload it, replacing any existing file with the same name.

4. **Initiate QR Code Generation**: The project will have a button or a command that you can execute to start the QR code generation process. This will create QR code images for each line in your CSV file.

5. **Retrieving Your QR Codes**: Once generated, the QR codes will be saved in the `qr_codes` folder on Replit. From there, you can download them for your use.

## Customizing Your QR Codes

You can personalize the QR codes to match your brand's color scheme and to ensure the accompanying text is positioned correctly.

### Adjusting Colors

- To modify the **background color** of the QR code, look for the line in the `create_qr_code_image` function with `back_color="#1D120B"` and replace the hex code with your desired color.
- To change the **color of the QR code** itself, replace the hex code in the `fill_color="white"` parameter.

### Positioning the Company Name

- To move the company name, adjust the `text_x_position` and `text_y_position` values in the `create_qr_code_image` function. These determine the horizontal and vertical positioning of the text on the QR code image.

### Positioning QR Codes on the Background

In the `main` function, you’ll find variables for adjustments:
- `x1_adjustment` and `x2_adjustment` determine the horizontal positioning of the two QR codes when they are displayed side by side.
- `y_position` controls how high or low the QR codes sit on the vertical axis.

## For Non-Technical Users: Simple Tips

- **Hex Codes for Colors**: Use an online color picker tool to select colors and obtain their hex codes (looks like `#FFFFFF` for white).
- **Testing**: After making adjustments, generate a QR code and see how it looks. Tweak as necessary and regenerate until satisfied.
- **Backup**: Save a copy of the original script and data before making changes, so you can always revert to the starting point if needed.

## Need Help?

- If you encounter any issues, Replit’s help resources and community forums are a great place to seek assistance.

By following this guide, you can confidently generate custom QR codes that are both functional and visually aligned with your branding. Enjoy creating QR codes that make an impression!
