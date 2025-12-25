import './App.css'
import { C1Chat, ThemeProvider } from '@thesysai/genui-sdk'
import '@crayonai/react-ui/styles/index.css'
import { useState, useCallback, useRef, useEffect } from 'react'

// Recommendation data
const RECOMMENDATIONS = [
  {
    icon: '📊',
    text: "Analyze the Indian stock market with today's key signals"
  },
  {
    icon: '🧭',
    text: "Analyse Conditions of Large, Mid and Small Cap in Indian Market"
  },
  {
    icon: '📰',
    text: 'Track major stock market events shaping investor sentiment'
  },
  {
    icon: '🌍',
    text: 'How global news connects with Indian market movements'
  }
]

// Custom hook for sending messages programmatically
function useMessageSender() {
  const sendMessage = useCallback((text: string) => {
    // Set flag to prevent sidebar toggle
    document.body.setAttribute('data-programmatic-interaction', 'true')

    // Small delay to ensure C1Chat is ready
    setTimeout(() => {
      const inputElement = document.querySelector(
        'textarea, input[type="text"], [contenteditable="true"]'
      ) as HTMLTextAreaElement | HTMLInputElement | HTMLElement

      if (inputElement) {
        // Set the input value
        if ('value' in inputElement) {
          const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
            inputElement instanceof HTMLTextAreaElement
              ? window.HTMLTextAreaElement.prototype
              : window.HTMLInputElement.prototype,
            'value'
          )?.set

          if (nativeInputValueSetter) {
            nativeInputValueSetter.call(inputElement, text)
          }

          inputElement.dispatchEvent(new Event('input', { bubbles: true }))
          inputElement.dispatchEvent(new Event('change', { bubbles: true }))
        } else if (inputElement.isContentEditable) {
          inputElement.textContent = text
          inputElement.dispatchEvent(new Event('input', { bubbles: true }))
        }

        // Don't focus input to prevent keyboard popup on mobile
        // This prevents the white space issue at the bottom

        // Send the message
        setTimeout(() => {
          const sendButton = document.querySelector(
            'button[type="submit"], button[aria-label*="send" i]'
          ) as HTMLButtonElement

          if (sendButton) {
            sendButton.click()
          } else {
            const form = inputElement.closest('form')
            if (form) {
              form.requestSubmit()
            }
          }

          // Remove flag after action completes
          setTimeout(() => {
            document.body.removeAttribute('data-programmatic-interaction')
          }, 100)
        }, 300)
      } else {
        document.body.removeAttribute('data-programmatic-interaction')
      }
    }, 100)
  }, [])

  return sendMessage
}

// Main App Component
function App() {
  const [showRecommendations, setShowRecommendations] = useState(true)
  const [hasMessages, setHasMessages] = useState(false)
  const sendMessage = useMessageSender()
  const chatContainerRef = useRef<HTMLDivElement>(null)

  const handleRecommendationClick = useCallback((text: string) => {
    setShowRecommendations(false)
    setHasMessages(true)
    sendMessage(text)
  }, [sendMessage])

  // Watch for user input to hide recommendations
  useEffect(() => {
    const handleInput = () => {
      // Hide recommendations as soon as user starts typing
      if (showRecommendations) {
        setHasMessages(true)
        setShowRecommendations(false)
      }
    }

    const handleSubmit = () => {
      // Ensure recommendations stay hidden after message is sent
      setHasMessages(true)
      setShowRecommendations(false)
    }

    // Start monitoring after a delay to ensure C1Chat is mounted
    const timeout = setTimeout(() => {
      // Monitor input elements
      const inputElement = document.querySelector('textarea, input[type="text"]')
      if (inputElement) {
        inputElement.addEventListener('input', handleInput)
        inputElement.addEventListener('keydown', handleInput)
      }

      // Monitor form submissions
      const form = document.querySelector('form')
      if (form) {
        form.addEventListener('submit', handleSubmit)
      }

      // Also monitor for any button clicks that might send messages
      document.addEventListener('click', (e) => {
        const target = e.target as HTMLElement
        if (
          target.matches('button[type="submit"], button[aria-label*="send" i]') ||
          target.closest('button[type="submit"], button[aria-label*="send" i]')
        ) {
          handleSubmit()
        }
      })
    }, 500)

    return () => {
      clearTimeout(timeout)
      const inputElement = document.querySelector('textarea, input[type="text"]')
      if (inputElement) {
        inputElement.removeEventListener('input', handleInput)
        inputElement.removeEventListener('keydown', handleInput)
      }
      const form = document.querySelector('form')
      if (form) {
        form.removeEventListener('submit', handleSubmit)
      }
    }
  }, [showRecommendations])

  // Watch for new chat events to show recommendations again
  useEffect(() => {
    const handleClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement
      if (
        target.textContent?.toLowerCase().includes('new chat') ||
        target.getAttribute('aria-label')?.toLowerCase().includes('new chat')
      ) {
        // Reset states to show recommendations again
        setHasMessages(false)
        setTimeout(() => setShowRecommendations(true), 100)

        // Close menu/sidebar on mobile after clicking New Chat
        setTimeout(() => {
          // Try to find and click the menu close button or backdrop
          const menuButton = document.querySelector('[aria-label*="menu" i], [aria-label*="close" i]') as HTMLElement
          const backdrop = document.querySelector('[class*="backdrop" i], [class*="overlay" i]') as HTMLElement

          if (menuButton && window.innerWidth < 768) {
            menuButton.click()
          } else if (backdrop && window.innerWidth < 768) {
            backdrop.click()
          }
        }, 200)
      }
    }

    document.addEventListener('click', handleClick)
    return () => document.removeEventListener('click', handleClick)
  }, [])

  // Inject recommendations into C1Chat DOM
  useEffect(() => {
    if (!showRecommendations || hasMessages) {
      const injected = document.querySelector('.recommendations-overlay')
      if (injected) {
        injected.remove()
      }
      return
    }

    const injectRecommendations = () => {
      if (document.querySelector('.recommendations-overlay')) {
        return
      }

      const inputElement = document.querySelector('textarea, input[type="text"]')
      if (!inputElement) {
        return
      }

      const targetContainer = inputElement.closest('[class*="container"], [class*="wrapper"], form, div') as HTMLElement
      if (!targetContainer) {
        return
      }

      // Create overlay container
      const overlay = document.createElement('div')
      overlay.className = 'recommendations-overlay'

      const container = document.createElement('div')
      container.className = 'recommendations-container'

      RECOMMENDATIONS.forEach((rec) => {
        const box = document.createElement('div')
        box.className = 'recommendation-box'
        box.setAttribute('role', 'button')
        box.setAttribute('tabindex', '0')

        const icon = document.createElement('span')
        icon.className = 'recommendation-icon'
        icon.textContent = rec.icon

        const text = document.createElement('p')
        text.className = 'recommendation-text'
        text.textContent = rec.text

        box.appendChild(icon)
        box.appendChild(text)

        box.addEventListener('click', (e) => {
          e.preventDefault()
          e.stopPropagation()
          e.stopImmediatePropagation()
          handleRecommendationClick(rec.text)
        }, { capture: true })

        container.appendChild(box)
      })

      overlay.appendChild(container)
      targetContainer.insertAdjacentElement('beforebegin', overlay)
    }

    const timeout1 = setTimeout(injectRecommendations, 500)
    const timeout2 = setTimeout(injectRecommendations, 1000)

    return () => {
      clearTimeout(timeout1)
      clearTimeout(timeout2)
      const injected = document.querySelector('.recommendations-overlay')
      if (injected) {
        injected.remove()
      }
    }
  }, [showRecommendations, hasMessages, handleRecommendationClick])

  return (
    <div className="app-container" ref={chatContainerRef}>
      <ThemeProvider mode="dark">
        <C1Chat
          apiUrl="https://marketinsight-skgl.onrender.com/api/chat"
          agentName="Market Insight"
          logoUrl="/icon.png"
          formFactor="full-page"
        />
      </ThemeProvider>
    </div>
  )
}

export default App