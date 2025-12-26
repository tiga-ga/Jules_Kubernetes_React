import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)
  const [formData, setFormData] = useState({
    title: '',
    url: '',
    type: 'zenn',
    published_date: ''
  })

  const fetchOutputs = () => {
    setLoading(true)
    fetch('/api/outputs')
      .then(response => response.json())
      .then(data => {
        setItems(data)
        setLoading(false)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
        setLoading(false)
      })
  }

  useEffect(() => {
    fetchOutputs()
  }, [])

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    fetch('/api/outputs', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => {
      if (response.ok) {
        setFormData({ title: '', url: '', type: 'zenn', published_date: '' })
        fetchOutputs()
      } else {
        alert('Error adding output')
      }
    })
  }

  const handleDelete = (id) => {
    if (confirm('Are you sure you want to delete this item?')) {
      fetch(`/api/outputs/${id}`, {
        method: 'DELETE'
      })
      .then(response => {
        if (response.ok) {
          fetchOutputs()
        }
      })
    }
  }

  if (loading && items.length === 0) {
    return <div className="loading">Loading...</div>
  }

  return (
    <div className="container">
      <header>
        <h1>My Outputs</h1>
        <p>Record your Zenn blogs and YouTube videos.</p>
      </header>

      <section className="add-form">
        <h2>Add New Output</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>URL</label>
            <input
              type="url"
              name="url"
              value={formData.url}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Type</label>
            <select name="type" value={formData.type} onChange={handleInputChange}>
              <option value="zenn">Zenn</option>
              <option value="youtube">YouTube</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div className="form-group">
            <label>Published Date</label>
            <input
              type="date"
              name="published_date"
              value={formData.published_date}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Add Output</button>
        </form>
      </section>

      <main>
        <h2>Recent Outputs</h2>
        <div className="grid">
          {items.map((item) => (
            <div key={item.id} className={`card ${item.type}`}>
              <div className="card-header">
                <span className={`badge ${item.type}`}>{item.type.toUpperCase()}</span>
                <span className="date">{item.published_date}</span>
                <button className="delete-btn" onClick={() => handleDelete(item.id)}>×</button>
              </div>
              <div className="card-content">
                <h3><a href={item.url} target="_blank" rel="noopener noreferrer">{item.title}</a></h3>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}

export default App
