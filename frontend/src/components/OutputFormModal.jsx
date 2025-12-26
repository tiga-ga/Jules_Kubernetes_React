import React, { useState, useEffect } from 'react';

const OutputFormModal = ({ isOpen, onClose, onSubmit, initialData }) => {
    const [formData, setFormData] = useState({
        title: '',
        url: '',
        content_type: 'Blog',
        published_at: '',
        comment: ''
    });

    useEffect(() => {
        if (initialData) {
            setFormData({
                title: initialData.title,
                url: initialData.url,
                content_type: initialData.content_type,
                published_at: initialData.published_at,
                comment: initialData.comment || ''
            });
        } else {
            setFormData({
                title: '',
                url: '',
                content_type: 'Blog',
                published_at: new Date().toISOString().split('T')[0],
                comment: ''
            });
        }
    }, [initialData, isOpen]);

    if (!isOpen) return null;

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <div className="modal-overlay" style={{
            position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
            backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center',
            zIndex: 1000
        }}>
            <div className="modal-content" style={{
                backgroundColor: 'white', padding: '20px', borderRadius: '8px', width: '400px',
                boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
            }}>
                <h2 style={{ marginTop: 0 }}>{initialData ? 'Edit Output' : 'New Output'}</h2>
                <form onSubmit={handleSubmit}>
                    <div style={{ marginBottom: '10px' }}>
                        <label htmlFor="title" style={{ display: 'block', marginBottom: '5px' }}>Title:</label>
                        <input
                            id="title"
                            type="text" name="title" value={formData.title} onChange={handleChange} required
                            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
                        />
                    </div>
                    <div style={{ marginBottom: '10px' }}>
                        <label htmlFor="url" style={{ display: 'block', marginBottom: '5px' }}>URL:</label>
                        <input
                            id="url"
                            type="url" name="url" value={formData.url} onChange={handleChange} required
                            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
                        />
                    </div>
                    <div style={{ marginBottom: '10px' }}>
                        <label htmlFor="content_type" style={{ display: 'block', marginBottom: '5px' }}>Type:</label>
                        <select
                            id="content_type"
                            name="content_type" value={formData.content_type} onChange={handleChange}
                            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
                        >
                            <option value="Blog">Blog</option>
                            <option value="Video">Video</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div style={{ marginBottom: '10px' }}>
                        <label htmlFor="published_at" style={{ display: 'block', marginBottom: '5px' }}>Date:</label>
                        <input
                            id="published_at"
                            type="date" name="published_at" value={formData.published_at} onChange={handleChange} required
                            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
                        />
                    </div>
                    <div style={{ marginBottom: '10px' }}>
                        <label htmlFor="comment" style={{ display: 'block', marginBottom: '5px' }}>Comment:</label>
                        <textarea
                            id="comment"
                            name="comment" value={formData.comment} onChange={handleChange}
                            style={{ width: '100%', padding: '8px', boxSizing: 'border-box', minHeight: '80px' }}
                        />
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '20px' }}>
                        <button type="button" onClick={onClose} style={{ padding: '8px 16px', cursor: 'pointer' }}>Cancel</button>
                        <button type="submit" style={{ padding: '8px 16px', cursor: 'pointer', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px' }}>Save</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default OutputFormModal;
