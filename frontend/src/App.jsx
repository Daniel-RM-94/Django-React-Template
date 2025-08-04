import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <h1>Core Project</h1>
        <div className="card">
          <button onClick={() => setCount((count) => count + 1)}>
            Contador: {count}
          </button>
          <p>
            Edita <code>src/App.jsx</code> y guarda para probar HMR
          </p>
        </div>
        <p className="read-the-docs">
          Haz clic en los enlaces de Vite y React para aprender más
        </p>
      </div>
    </>
  )
}

export default App 