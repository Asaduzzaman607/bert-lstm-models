import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ProjectGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Deliverables: IMDb Sentiment Analysis")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        nav_frame = ttk.Frame(self, padding=10)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        sections = ["Abstract", "Proposed Methods", "Experiments", "Results", "Charts"]
        for section in sections:
            btn = ttk.Button(nav_frame, text=section, command=lambda s=section: self.show_section(s))
            btn.pack(fill=tk.X, pady=5)

        self.content_frame = ttk.Frame(self, padding=10)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.content_label = ttk.Label(self.content_frame, text="Select a section to view.", wraplength=600, justify="left")
        self.content_label.pack(anchor="w", padx=10, pady=10)

    def show_section(self, section):
        if section == "Abstract":
            text = (
                "Language Modeling is a prevalent task in NLP. This project fine-tunes BERT for sentiment "
                "classification on IMDb movie reviews. Performance is compared against LSTM, Logistic Regression, "
                "and other baseline models. We demonstrate BERT's superior accuracy in handling complex text."
            )
        elif section == "Proposed Methods":
            text = (
                "1. BERT: Fine-tuned for binary sentiment classification.\n"
                "2. LSTM: Trained on sequences of word embeddings.\n"
                "3. Logistic Regression: Applied to TF-IDF features.\n"
                "4. XGBoost: Ensemble learning method for robust performance.\n"
                "5. Linear SVM: Optimized for linearly separable data.\n"
                "6. Naïve Bayes: Effective probabilistic model for text classification."
            )
        elif section == "Experiments":
            text = (
                "Experiments were conducted on the IMDb dataset to evaluate different models. "
                "Each model's accuracy and resource usage were recorded, highlighting the trade-offs in performance."
            )
        elif section == "Results":
            text = "Results indicate BERT achieves the highest accuracy (94.2%), followed by XGBoost and LSTM."
        elif section == "Charts":
            self.show_charts()
            return
        else:
            text = "Select a valid section."

        self.content_label.config(text=text)

    def show_charts(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        chart_paths = [
            "scalability_chart_path.png",  # Replace with actual image paths
            "efficiency_chart_path.png",
            "performance_vs_training_time_chart_path.png"
        ]

        for path in chart_paths:
            img = Image.open(path)
            img = img.resize((400, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            lbl = ttk.Label(self.content_frame, image=photo)
            lbl.image = photo
            lbl.pack(padx=10, pady=10)

        back_btn = ttk.Button(self.content_frame, text="Back to Sections", command=self.reset_content)
        back_btn.pack(pady=5)

    def reset_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.content_label = ttk.Label(self.content_frame, text="Select a section to view.", wraplength=600, justify="left")
        self.content_label.pack(anchor="w", padx=10, pady=10)

app = ProjectGUI()
app.mainloop()
