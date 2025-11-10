# 🌐 To-Do Web Application

An interactive **To-Do Web App** built using **Python** and **Streamlit**.  
It lets users **add**, **view**, and **complete** their daily tasks easily — right from the browser.  
Data is stored locally in a simple text file (`todo.txt`) for persistent tracking.

🟢 **Live Demo:**  
👉 [Try it on Streamlit Cloud](https://todo-webapp-mfvrzf7vwsat8exzyhdffl.streamlit.app/)

---

## 🚀 Features

- ✅ Add new tasks directly in the browser  
- 🗑️ Mark tasks as complete (auto-remove on check)  
- 💾 Tasks are saved persistently in a local text file  
- 🕒 Real-time updates — no refresh required  
- 🧭 Clean and simple UI built with **Streamlit**  
- 📱 Fully responsive — works on desktop and mobile  
- ☁️ Deployable easily on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🗂️ Project Structure

```
ToDo_WebApp/
│
├── functions.py        # Helper functions to read and write todos
├── app.py              # Main Streamlit application
├── todo.txt            # Data file storing todos
├── requirements.txt    # Dependencies list
└── README.md           # Documentation (this file)
```

---

## 📦 Requirements

Ensure you have **Python 3.10+** and **Streamlit** installed.  
Install dependencies with:

```bash
pip install streamlit
```

or, if using a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
streamlit>=1.38.0
```

---

## ▶️ Run Locally

To start the app locally:

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

You’ll see your To-Do web app running live.

---

## ☁️ Deploying to Streamlit Cloud

1. Push your project to **GitHub**  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)  
3. Connect your GitHub repository  
4. Select the file `app.py` as the main entry point  
5. Click **Deploy** 🚀  

Your web app will be live instantly — just like this one:  
👉 [https://todo-webapp-mfvrzf7vwsat8exzyhdffl.streamlit.app/](https://todo-webapp-mfvrzf7vwsat8exzyhdffl.streamlit.app/)

---

## 🧠 How It Works

1. The app loads existing todos from `todo.txt`.  
2. You can add new todos using the text input.  
3. Each todo appears with a checkbox beside it.  
4. Checking a box removes the todo from the list and updates the file.  
5. Streamlit automatically refreshes the UI in real time.

---

## 🧩 Possible Enhancements

- 🌈 Add task categories (Work, Personal, etc.)  
- 🕓 Add due dates using Streamlit’s date picker  
- 💡 Include a progress bar for completed tasks  
- ☁️ Store todos in a database or cloud storage (e.g., Firebase, PostgreSQL)

---

## 🪪 License

This project is open-source and available under the [MIT License](LICENSE).  
© 2025 Ananthu Prakash, Ardit Sulce
