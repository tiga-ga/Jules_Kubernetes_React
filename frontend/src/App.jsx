import React, { useState } from 'react';
import './App.css';
import OutputList from './components/OutputList';
import OutputFormModal from './components/OutputFormModal';
import useOutputs from './hooks/useOutputs';

function App() {
    const { outputs, loading, error, createOutput, updateOutput, deleteOutput } = useOutputs();
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [editingOutput, setEditingOutput] = useState(null);

    const handleCreate = () => {
        setEditingOutput(null);
        setIsModalOpen(true);
    };

    const handleEdit = (output) => {
        setEditingOutput(output);
        setIsModalOpen(true);
    };

    const handleDelete = async (id) => {
        if (window.confirm('Are you sure you want to delete this output?')) {
            await deleteOutput(id);
        }
    };

    const handleSave = async (data) => {
        try {
            if (editingOutput) {
                await updateOutput(editingOutput.id, data);
            } else {
                await createOutput(data);
            }
            setIsModalOpen(false);
        } catch (err) {
            alert('Failed to save output: ' + err.message);
        }
    };

    return (
        <div className="App">
            <header className="App-header" style={{ marginBottom: '20px', padding: '10px', backgroundColor: '#282c34', color: 'white' }}>
                <h1>Output Manager</h1>
            </header>

            <main style={{ padding: '20px' }}>
                <div style={{ marginBottom: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h2>My Outputs</h2>
                    <button onClick={handleCreate} style={{ padding: '10px 20px', fontSize: '16px' }}>+ New Output</button>
                </div>

                {loading && <p>Loading...</p>}
                {error && <p style={{ color: 'red' }}>Error: {error}</p>}

                {!loading && !error && (
                    <OutputList
                        outputs={outputs}
                        onEdit={handleEdit}
                        onDelete={handleDelete}
                    />
                )}
            </main>

            <OutputFormModal
                isOpen={isModalOpen}
                onClose={() => setIsModalOpen(false)}
                onSubmit={handleSave}
                initialData={editingOutput}
            />
        </div>
    );
}

export default App;
