import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [items, setItems] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/feeds')
      .then(response => response.json())
      .then(data => {
        setItems(data)
        setLoading(false)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
        setLoading(false)
      })
  }, [])

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  return (
    <div className="container">
      <header>
        <h1>Content Aggregator</h1>
      </header>
      <main>
        <div className="grid">
          {items.map((item, index) => (
            <div key={index} className={`card ${item.type}`}>
              <div className="card-type">{item.type === 'youtube' ? 'YouTube' : 'Blog'}</div>
              <img src={item.thumbnail} alt={item.title} className="thumbnail" />
              <div className="card-content">
                <h3><a href={item.url} target="_blank" rel="noopener noreferrer">{item.title}</a></h3>
                <p>{item.description}</p>
                <span className="date">{item.date}</span>
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}

export default App
