import { useState, useEffect } from 'react';
import axios from 'axios';

const useOutputs = () => {
    const [outputs, setOutputs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchOutputs = async () => {
        setLoading(true);
        try {
            const response = await axios.get('/api/outputs');
            setOutputs(response.data);
            setError(null);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const createOutput = async (newOutput) => {
        try {
            await axios.post('/api/outputs', newOutput);
            await fetchOutputs(); // Refresh list
        } catch (err) {
            setError(err.message);
            throw err;
        }
    };

    const updateOutput = async (id, updatedData) => {
        try {
            await axios.put(`/api/outputs/${id}`, updatedData);
            await fetchOutputs();
        } catch (err) {
            setError(err.message);
            throw err;
        }
    };

    const deleteOutput = async (id) => {
        try {
            await axios.delete(`/api/outputs/${id}`);
            await fetchOutputs();
        } catch (err) {
            setError(err.message);
            throw err;
        }
    };

    useEffect(() => {
        fetchOutputs();
    }, []);

    return {
        outputs,
        loading,
        error,
        createOutput,
        updateOutput,
        deleteOutput,
        refreshOutputs: fetchOutputs
    };
};

export default useOutputs;
