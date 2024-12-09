import React, { useEffect, useState } from 'react';
import { fetchNotes, deleteNote, archiveNote, unarchiveNote } from '../services/api';

const NoteList = ({ archived }) => {
    const [notes, setNotes] = useState([]);

    useEffect(() => {
        fetchNotes(archived).then((response) => {
            setNotes(response.data);
        });
    }, [archived]);

    const handleDelete = (id) => {
        deleteNote(id).then(() => {
            setNotes(notes.filter((note) => note.id !== id));
        });
    };

    const handleArchiveToggle = (id, isArchived) => {
        const action = isArchived ? unarchiveNote : archiveNote;
        action(id).then(() => {
            setNotes(notes.filter((note) => note.id !== id));
        });
    };

    return (
        <div>
            <h2>{archived ? 'Archived Notes' : 'Active Notes'}</h2>
            {notes.map((note) => (
                <div key={note.id} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
                    <h3>{note.title}</h3>
                    <p>{note.content}</p>
                    <button onClick={() => handleArchiveToggle(note.id, archived)}>
                        {archived ? 'Unarchive' : 'Archive'}
                    </button>
                    <button onClick={() => handleDelete(note.id)}>Delete</button>
                </div>
            ))}
        </div>
    );
};

export default NoteList;
