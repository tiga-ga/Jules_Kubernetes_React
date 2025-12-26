import React from 'react';
import OutputItem from './OutputItem';

const OutputList = ({ outputs, onEdit, onDelete }) => {
    if (!outputs || outputs.length === 0) {
        return <p>No outputs found.</p>;
    }

    return (
        <div className="output-list">
            {outputs.map(output => (
                <OutputItem
                    key={output.id}
                    output={output}
                    onEdit={onEdit}
                    onDelete={onDelete}
                />
            ))}
        </div>
    );
};

export default OutputList;
