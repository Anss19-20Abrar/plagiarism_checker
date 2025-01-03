

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox, filedialog

# Define the global TfidfVectorizer instance
tfidf_vectorizer = TfidfVectorizer()


def vectorize_texts(text1, text2):
    return tfidf_vectorizer.fit_transform([text1, text2]).toarray()


def compute_similarity(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0] * 100


def highlight_matches(text_widget, text, matches):
    """
    Highlight the matching words in the text widget.
    """
    text_widget.tag_remove("highlight", "1.0", tk.END)  # Remove existing highlights
    for match in matches:
        start_idx = "1.0"
        while True:
            start_idx = text_widget.search(match, start_idx, tk.END)
            if not start_idx:
                break
            end_idx = f"{start_idx}+{len(match)}c"
            text_widget.tag_add("highlight", start_idx, end_idx)
            start_idx = end_idx
    text_widget.tag_config("highlight", background="yellow", foreground="black")


def check_similarity():
    base_text = text_input1.get("1.0", tk.END).strip()
    input_text = text_input2.get("1.0", tk.END).strip()

    if not base_text or not input_text:
        messagebox.showwarning("Input Error", "Both input fields must have text.")
        return

    # Vectorize the input texts together
    vectors = vectorize_texts(base_text, input_text)
    base_vector, input_vector = vectors[0], vectors[1]

    # Compute similarity percentage
    similarity_percentage = compute_similarity(base_vector, input_vector)

    # Find matching words
    base_words = set(base_text.split())
    input_words = set(input_text.split())
    matches = base_words.intersection(input_words)

    # Highlight matches in both text widgets
    highlight_matches(text_input1, base_text, matches)
    highlight_matches(text_input2, input_text, matches)

    # Display the similarity percentage
    result_label.config(text=f"Similarity: {similarity_percentage:.2f}%")


def clear_texts():
    text_input1.delete("1.0", tk.END)
    text_input2.delete("1.0", tk.END)
    result_label.config(text="Similarity: N/A")


def upload_file(input_text_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            input_text_widget.delete("1.0", tk.END)
            input_text_widget.insert("1.0", content)


# GUI setup
root = tk.Tk()
root.title("Text Similarity Checker")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

# Title label
title_label = tk.Label(root, text="Text Similarity Checker", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Input fields and buttons
frame1 = tk.Frame(root, bg="#f5f5f5")
frame1.pack(pady=10)

text_input1 = tk.Text(frame1, height=10, width=40, wrap="word", font=("Arial", 12))
text_input1.grid(row=0, column=0, padx=5, pady=5)
upload_button1 = tk.Button(frame1, text="Upload File 1", command=lambda: upload_file(text_input1), bg="#4caf50",
                           fg="white", font=("Arial", 10))
upload_button1.grid(row=1, column=0, pady=5)

text_input2 = tk.Text(frame1, height=10, width=40, wrap="word", font=("Arial", 12))
text_input2.grid(row=0, column=1, padx=5, pady=5)
upload_button2 = tk.Button(frame1, text="Upload File 2", command=lambda: upload_file(text_input2), bg="#4caf50",
                           fg="white", font=("Arial", 10))
upload_button2.grid(row=1, column=1, pady=5)

# Action buttons
action_frame = tk.Frame(root, bg="#f5f5f5")
action_frame.pack(pady=10)


check_button = tk.Button(action_frame, text="Check Similarity", command=check_similarity, bg="#2196f3", fg="white",
                         font=("Arial", 12))
check_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(action_frame, text="Clear Text", command=clear_texts, bg="#f44336", fg="white",
                         font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(root, text="Similarity: N/A", font=("Arial", 14), bg="#f5f5f5", fg="#333")
result_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Authorized by Ans", font=("Arial", 10, "italic"), bg="#f5f5f5", fg="#777")
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
