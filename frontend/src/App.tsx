import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <div className="app">
        <header className="app-header">
          <h1>Tento - Housing Platform</h1>
          <p>A comprehensive housing platform connecting tenants, landlords, and brokers</p>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<div>Home Page</div>} />
            <Route path="/dashboard" element={<div>Dashboard</div>} />
            <Route path="/properties" element={<div>Properties</div>} />
            <Route path="*" element={<div>Page Not Found</div>} />
          </Routes>
        </main>
        <footer>
          <p>© {new Date().getFullYear()} Tento. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  )
}

export default App