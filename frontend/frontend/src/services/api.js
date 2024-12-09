import axios from 'axios';

const API = axios.create({
    baseURL: 'http://127.0.0.1:8000/api', // Base URL for backend
});

export const fetchNotes = (archived = false) => API.get(`/notes?archived=${archived}`);
export const createNote = (data) => API.post('/notes', data);
export const updateNote = (id, data) => API.put(`/notes/${id}`, data);
export const deleteNote = (id) => API.delete(`/notes/${id}`);
export const archiveNote = (id) => API.post(`/notes/${id}/archive`);
export const unarchiveNote = (id) => API.post(`/notes/${id}/unarchive`);
export const fetchTags = () => API.get('/tags');
export const createTag = (name) => API.post('/tags', { name });
export const addTagToNote = (noteId, tagId) => API.post(`/notes/${noteId}/tags/${tagId}`);
export const removeTagFromNote = (noteId, tagId) => API.delete(`/notes/${noteId}/tags/${tagId}`);
