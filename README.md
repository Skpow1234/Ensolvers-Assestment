
# **Full-Stack Notes Application README**

## **Project Overview**

This project is a full-stack application for managing notes, built with a **FastAPI backend** and a **React.js frontend**. It includes features such as creating, editing, deleting, archiving/unarchiving notes, tagging notes, and filtering notes by tags. The backend uses **PostgreSQL** as its database and **SQLAlchemy** for ORM, while the frontend is styled and built with React components.

A single **bash/zsh script** (`run_app.sh`) is provided to set up and run the application seamlessly.

---

## **Key Tools and Versions**

### **Languages**

- **Python 3.10+**: Backend development.
- **JavaScript (ES6)**: Frontend development.

### **Frameworks and Libraries**

#### Backend

- **FastAPI 0.95.2**: Web framework for creating APIs.
- **SQLAlchemy 1.4.41**: ORM for interacting with the PostgreSQL database.
- **Pydantic 1.10.4**: Data validation and serialization.
- **Alembic 1.10.1**: Database migration tool.

#### Frontend

- **React.js 18.2.0**: JavaScript library for building the user interface.
- **Axios 1.4.0**: For making HTTP requests to the backend API.

### **Database**

- **PostgreSQL 15.2**: Relational database for persisting data.

### **Development Tools**

- **Node.js 18.17.0**: JavaScript runtime for running the frontend locally.
- **npm 9.6.1**: Node package manager.
- **uvicorn 0.20.0**: ASGI server for running FastAPI.
- **psycopg2-binary 2.9.6**: PostgreSQL database adapter.

---

## **Features**

### Backend Features

- **Notes Management**:
  - Create, edit, delete notes.
  - Archive and unarchive notes.
- **Tag Management**:
  - Create and manage tags.
  - Assign tags to notes.
  - Filter notes by tags.

### Frontend Features

- Fully functional UI for managing notes.
- Create, edit, delete, and archive/unarchive notes.
- Tag management and filtering by tags.
- Clean and modular React components.

### Integration

- The frontend communicates with the backend using **Axios** for API calls.
- Data persistence is handled through **PostgreSQL**.

---

## **Setup and Installation**

### **Prerequisites**

- Python 3.10+ installed.
- Node.js 18.17.0 and npm 9.6.1 installed.
- PostgreSQL 15.2 installed and running.

### **Steps to Set Up the Project**

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Run the Setup Script**

   A single script automates the entire setup:

   ```bash
   ./run_app.sh
   ```

3. **Access the Application**
   - **Frontend**: Open `http://localhost:3000` in your browser.
   - **Backend**: API documentation is available at `http://127.0.0.1:8000/docs`.

---

## **Backend Overview**

The backend is built with **FastAPI** and follows a layered architecture:

### **Structure**

```bash
backend/
├── app/
│   ├── main.py              # Application entry point
│   ├── routes/              # API endpoints for notes and tags
│   ├── services/            # Business logic for notes and tags
│   ├── repositories/        # Database operations (CRUD)
│   ├── models/              # SQLAlchemy models for notes and tags
│   ├── database.py          # Database connection and session management
│   ├── config.py            # Configuration for environment variables
├── requirements.txt         # Python dependencies
├── alembic/                 # Migrations folder
└── README.md                # Backend documentation
```

### **Key Features**

- CRUD for notes and tags.
- Tagging system with note-tag relationships.
- Swagger-based API documentation (`/docs`).
- Uses Alembic for database migrations.

### **Database**

- **PostgreSQL** is used for data persistence.
- Schema:
  - `notes` table: Stores note details (title, content, archived status).
  - `tags` table: Stores tag names.
  - `note_tags` table: Many-to-many relationship between notes and tags.

### **Key Tools**

- **Uvicorn**: ASGI server for serving the FastAPI app.
- **SQLAlchemy**: ORM for database interactions.

---

## **Frontend Overview**

The frontend is built with **React.js** and styled using CSS modules.

### **Structure**

```bash
frontend/
├── src/
│   ├── components/           # Reusable React components
│   │   ├── NoteList.js       # Displays all notes
│   │   ├── NoteForm.js       # Form for creating/editing notes
│   │   ├── NoteFilter.js     # Filtering notes by tags
│   │   ├── TagManager.js     # Managing tags
│   ├── services/             # Axios setup for API calls
│   ├── App.js                # Main application component
│   ├── index.js              # Entry point for React
├── package.json              # Node.js dependencies and scripts
└── README.md                 # Frontend documentation
```

### **Key Features**

- Note CRUD operations (create, edit, delete, archive/unarchive).
- Tag management (add, remove, filter by tags).
- Dynamic API communication with the backend.

### **Key Tools**

- **React Context**: For global state management.
- **Axios**: For making HTTP requests to the backend.

---

## **Script Overview**

The `run_app.sh` script automates the entire process of setting up and running the application:

### **Script Functionality**

1. Sets up the backend:
   - Creates a virtual environment for Python dependencies.
   - Installs backend dependencies from `requirements.txt`.
   - Runs Alembic migrations to set up the database schema.
   - Starts the FastAPI server using Uvicorn.

2. Sets up the frontend:
   - Installs Node.js dependencies using `npm install`.
   - Starts the React development server.

3. Provides URLs for accessing the application.

### **Usage**
Run the script from the root directory:
```bash
./run_app.sh
```

---

## **Runtime Specifications**

- **Python**: `3.10+`
- **PostgreSQL**: `15.2`
- **React.js**: `18.2.0`
- **Node.js**: `18.17.0`
- **npm**: `9.6.1`
- **uvicorn**: `0.20.0`

---
