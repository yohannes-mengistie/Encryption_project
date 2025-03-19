import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import {App} from './App.tsx'
import {EncryptionProvider} from './Context/EncryptionContext'

createRoot(document.getElementById('root')!).render(
  <EncryptionProvider>
    <App />
  </EncryptionProvider>,
)
