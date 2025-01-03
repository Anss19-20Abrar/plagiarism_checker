# Plagiarism Checker GUI

This Python application provides a user-friendly graphical interface to check for similarities between two pieces of text. It uses the `Tkinter` library for the GUI, and the `sklearn` library to calculate text similarity using TF-IDF and cosine similarity.

---

## Features

1. **Text Input:** Users can input two pieces of text to compare.
2. **File Upload:** Users can upload text files to populate the input fields.
3. **Text Highlighting:** Matching portions of text between the two inputs are highlighted in color.
4. **Similarity Score:** The application calculates and displays the percentage similarity between the two texts.
5. **Clear Button:** A button to clear both text fields.
6. **Background Image:** The interface includes a customizable background image for better aesthetics.
7. **Footer:** Displays an “Authorized by Ans” footer for branding.

---

## Requirements

- Python 3.6+
- Libraries:
  - `Tkinter`
  - `sklearn`
  - `numpy`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   ```
2. Navigate to the project directory:
   ```bash
   cd plagiarism-checker-gui
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the script:
   ```bash
   python plagiarism_checker.py
   ```
2. Enter text in the two input fields or upload files.
3. Click the **Check Similarity** button to calculate similarity.
4. Matching text will be highlighted, and the similarity percentage will be displayed.
5. Use the **Clear** button to reset the input fields.

---

## Customization

### Background Image
To change the background image, update the following line in the script:
```python
root.image = tk.PhotoImage(file="https://your-image-url.png")
```
Replace `https://your-image-url.png` with the desired image link.

### Footer Text
Modify the footer text in the script:
```python
author_label = tk.Label(root, text="Authorized by Ans", font=("Arial", 10), bg="lightgray")
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Developed by Ans. For inquiries, please contact [anssabrar11@gmail.com ].

