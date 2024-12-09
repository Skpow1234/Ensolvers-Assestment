import React, { useEffect, useState } from 'react';
import { fetchTags } from '../services/api';

const NoteFilter = ({ onFilter }) => {
    const [tags, setTags] = useState([]);

    useEffect(() => {
        fetchTags().then((response) => {
            setTags(response.data);
        });
    }, []);

    return (
        <div>
            <h3>Filter Notes by Tag</h3>
            <select onChange={(e) => onFilter(e.target.value)}>
                <option value="">All Tags</option>
                {tags.map((tag) => (
                    <option key={tag.id} value={tag.id}>
                        {tag.name}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default NoteFilter;
