
# **Frontend README**

## **Project Overview**

This frontend application is built using **React.js** to provide a user interface for managing notes. It supports creating, editing, deleting, archiving/unarchiving notes, tagging notes, and filtering notes by tags. The application communicates with the **FastAPI backend** using **Axios** for API requests.

---

## **Project Structure**

The project is organized into the following structure:

```bash
frontend/
├── public/
│   ├── index.html                # HTML template for the app
├── src/
│   ├── components/               # Reusable React components
│   │   ├── NoteList.js           # Displays all notes (active/archived)
│   │   ├── NoteForm.js           # Form for creating/editing notes
│   │   ├── NoteFilter.js         # Filtering notes by tags
│   │   ├── TagManager.js         # Tag creation and assignment
│   │   ├── Login.js              # Basic login UI (optional placeholder)
│   ├── services/                 # Utility services
│   │   ├── api.js                # Axios setup for API calls
│   ├── App.js                    # Main application component
│   ├── index.js                  # Entry point for React
├── package.json                  # Node.js dependencies and scripts
├── README.md                     # This documentation
```

---

## **Key Tools and Versions**

### **Languages**

- **JavaScript (ES6)**: Core programming language.

### **Frameworks and Libraries**

- **React.js 18.2.0**: JavaScript library for building the user interface.
- **Axios 1.4.0**: For making HTTP requests to the backend API.
- **React Router 6.11.0** (optional): For navigation if needed.

### **Development Tools**

- **Node.js 18.17.0**: JavaScript runtime for running the app locally.
- **npm 9.6.1**: Node package manager.

---

## **Setup and Installation**

### **Prerequisites**

- Node.js 18.17.0 installed.
- npm 9.6.1 installed.

### **Steps to Set Up the Project**

1. **Install Dependencies**

   ```bash
   npm install
   ```

2. **Run the Application**

   Start the development server:

   ```bash
   npm start
   ```

3. **Access the Application**
   Open your browser and navigate to:

   ```bash
   http://localhost:3000
   ```

---

## **Features**

### **Notes Management**

- **Create Note**: Users can create new notes with a title and content.
- **Edit Note**: Users can modify existing notes.
- **Delete Note**: Users can delete notes permanently.
- **Archive/Unarchive Note**: Users can toggle between active and archived states.

### **Tag Management**

- **Add Tags to Notes**: Users can assign tags to notes.
- **Remove Tags from Notes**: Users can remove tags from notes.

### **Filtering**

- **Filter Notes by Tags**: Users can filter notes based on selected tags.

### **Integration with Backend**

- All operations are synced with the FastAPI backend via API requests.

---

## **Components Overview**

### **Main Components**

1. **`NoteList.js`**:
   - Displays a list of notes (either active or archived).
   - Provides actions to delete or toggle archive status.
2. **`NoteForm.js`**:
   - Handles creating or editing notes.
3. **`NoteFilter.js`**:
   - Allows users to filter notes by tags.
4. **`TagManager.js`**:
   - Placeholder for creating and managing tags.

### **Utility Services**

- **`api.js`**:
  - Axios setup for making API calls to the backend.

---

## **Runtime Specifications**

- **React.js**: `18.2.0`
- **Node.js**: `18.17.0`
- **npm**: `9.6.1`

---

## **Key Considerations**

- **Performance**: Ensure that API calls are efficient by using React's `useEffect` and caching results where necessary.
- **Scalability**: Components are reusable and modular to allow easy addition of features.
- **UI/UX**: Ensure the interface is user-friendly and intuitive.
