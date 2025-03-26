import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, useRoutes } from 'react-router-dom'
import './App.css'
import routes from './routes'

// Component to render routes using useRoutes hook
const AppRoutes: React.FC = () => {
  return useRoutes(routes);
};

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
          <AppRoutes />
        </main>
        <footer>
          <p>© {new Date().getFullYear()} Tento. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  )
}

export default App
