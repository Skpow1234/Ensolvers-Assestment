import React, { useState } from 'react';
import { createNote, updateNote } from '../services/api';

const NoteForm = ({ note = {}, onSave }) => {
    const [title, setTitle] = useState(note.title || '');
    const [content, setContent] = useState(note.content || '');

    const handleSubmit = (e) => {
        e.preventDefault();
        const action = note.id ? updateNote : createNote;
        action(note.id, { title, content }).then((response) => {
            onSave(response.data);
            setTitle('');
            setContent('');
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
            />
            <textarea
                placeholder="Content"
                value={content}
                onChange={(e) => setContent(e.target.value)}
            />
            <button type="submit">{note.id ? 'Update Note' : 'Create Note'}</button>
        </form>
    );
};

export default NoteForm;
