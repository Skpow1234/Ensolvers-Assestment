import React, { useState } from 'react';
import NoteList from './components/NoteList';
import NoteForm from './components/NoteForm';
import NoteFilter from './components/NoteFilter';

const App = () => {
    const [filterTag, setFilterTag] = useState(null);

    const handleFilter = (tagId) => {
        setFilterTag(tagId);
    };

    return (
        <div>
            <h1>Notes Application</h1>
            <NoteFilter onFilter={handleFilter} />
            <NoteForm />
            <NoteList archived={false} />
            <NoteList archived={true} />
        </div>
    );
};

export default App;
