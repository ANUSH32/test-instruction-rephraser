# Test Instruction Rephraser - Full Stack Application

This is a full-stack web application that allows users to enter natural language test instructions, rephrase them using the Cohere API, and confirm or edit the rephrased instructions.

---

## Features

- Backend API built with Python Flask
- Frontend built with React and Next.js (app router)
- Uses Cohere's `command-r-plus` model to rephrase instructions
- Modern, responsive UI with loading indicators and confirmation
- Proxy setup to forward API requests from frontend to backend
- Automated startup script to run backend and frontend together

---

## Prerequisites

Make sure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (v16 or higher recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
cd ..
```

### 3. Install Frontend Dependencies

```bash
npm install
```

---

## Running the Application

### Option 1: Run Backend and Frontend Separately

- Start the backend Flask server:

```bash
python3 backend/app.py
```

- In a separate terminal, start the frontend Next.js development server:

```bash
npm run dev
```

- Open your browser and navigate to [http://localhost:8000](http://localhost:8000)

---

### Option 2: Run Both Servers Together (Linux/macOS)

- Use the provided shell script to start both backend and frontend:

```bash
bash run.sh
```

- This will start the backend on port 5000 and frontend on port 8000.

- Open your browser and navigate to [http://localhost:8000](http://localhost:8000)

---

## Environment Variables

- The Cohere API key is currently hardcoded in `backend/app.py`. For production use, consider storing it securely in environment variables.

---

## Project Structure

```
backend/
  ├── app.py            # Flask backend API
  └── requirements.txt  # Python dependencies

src/app/
  ├── layout.tsx        # Next.js root layout
  ├── page.tsx          # React frontend page
  └── globals.css       # Global styles

next.config.js          # Next.js config with API proxy
run.sh                  # Script to run backend and frontend together
README.md               # This file
```

---

## Notes

- The frontend proxies API requests to the backend via Next.js rewrites configured in `next.config.js`.
- The UI uses Tailwind CSS for styling and Google Fonts for typography.
- The backend uses Flask-CORS to allow cross-origin requests.
- The app is designed for development and demonstration purposes. For production, consider additional security, error handling, and deployment setup.

---

## Troubleshooting

- If ports 5000 or 8000 are in use, stop the conflicting processes or change the ports in the code.
- Ensure Python and Node.js versions are compatible.
- If you encounter CORS or network errors, verify the proxy settings in `next.config.js`.

---

## License

This project is open source and free to use.

---

## Contact

For questions or support, please contact the maintainer.
