import React from 'react'
import { BrowserRouter,Routes, Route} from 'react-router-dom';
import EncryptionApp from './Components/EncryptionApp'

export const App = () => {
  return (
    <div>
      <BrowserRouter>
          <EncryptionApp />
      </BrowserRouter>
    </div>
  )
}

