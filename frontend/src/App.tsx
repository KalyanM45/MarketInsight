import './App.css'
import { C1Chat, ThemeProvider } from '@thesysai/genui-sdk'
import '@crayonai/react-ui/styles/index.css'

function App() {

  return (
    <div className='app-container'>
      <ThemeProvider mode="dark">
        <C1Chat apiUrl='/api/chat' />
      </ThemeProvider>
    </div>

  )
}

export default App