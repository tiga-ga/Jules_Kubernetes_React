import React from 'react';

const OutputItem = ({ output, onEdit, onDelete }) => {
    return (
        <div className="output-item" style={{ border: '1px solid #ddd', padding: '10px', marginBottom: '10px', borderRadius: '4px' }}>
            <h3>{output.title}</h3>
            <p><strong>Type:</strong> {output.content_type}</p>
            <p><strong>URL:</strong> <a href={output.url} target="_blank" rel="noopener noreferrer">{output.url}</a></p>
            <p><strong>Date:</strong> {output.published_at}</p>
            {output.comment && <p><strong>Comment:</strong> {output.comment}</p>}
            <div style={{ marginTop: '10px' }}>
                <button onClick={() => onEdit(output)} style={{ marginRight: '5px' }}>Edit</button>
                <button onClick={() => onDelete(output.id)}>Delete</button>
            </div>
        </div>
    );
};

export default OutputItem;
