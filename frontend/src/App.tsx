import './App.css'
import { C1Chat, ThemeProvider } from '@thesysai/genui-sdk'
import '@crayonai/react-ui/styles/index.css'
import { useState, useEffect, useCallback } from 'react'

function App() {
  const [showRecommendations, setShowRecommendations] = useState(true)
  const recommendations = [
    {
      icon: '📊',
      text: "Analyze the Indian stock market with today's key signals"
    },
    {
      icon: '🧭',
      text: "What are today's biggest gainers and losers in Indian Market?"
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
  const handleRecommendationClick = useCallback((text: string, event?: React.MouseEvent | Event) => {
    // Prevent event from bubbling up (which might close sidebar)
    if (event) {
      event.stopPropagation()
    }

    // Find the input/textarea element in C1Chat
    setTimeout(() => {
      // Try multiple selectors to find the input
      const inputElement = document.querySelector(
        'textarea, input[type="text"], [contenteditable="true"]'
      ) as HTMLTextAreaElement | HTMLInputElement | HTMLElement

      if (inputElement) {
        // Set the value based on element type
        if ('value' in inputElement) {
          // For textarea and input elements
          const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
            inputElement instanceof HTMLTextAreaElement
              ? window.HTMLTextAreaElement.prototype
              : window.HTMLInputElement.prototype,
            'value'
          )?.set

          if (nativeInputValueSetter) {
            nativeInputValueSetter.call(inputElement, text)
          }

          // Dispatch input event to trigger React's onChange
          const inputEvent = new Event('input', { bubbles: true })
          inputElement.dispatchEvent(inputEvent)
        } else if (inputElement.isContentEditable) {
          // For contenteditable elements
          inputElement.textContent = text

          // Dispatch input event
          const inputEvent = new Event('input', { bubbles: true })
          inputElement.dispatchEvent(inputEvent)
        }

        // Focus the input
        inputElement.focus()

        // Try to find and click the send button after a short delay
        setTimeout(() => {
          const sendButton = document.querySelector(
            'button[type="submit"], button[aria-label*="send" i], button[aria-label*="submit" i], button:has(svg)'
          ) as HTMLButtonElement

          if (sendButton) {
            sendButton.click()
          }
        }, 150)
      }
    }, 100)

    // Hide recommendations after clicking
    setShowRecommendations(false)
  }, [])

  // Watch for chat resets (new chat button clicks) and first message
  useEffect(() => {
    // Create a MutationObserver to watch for DOM changes
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        // Check if messages were removed (indicating a new chat)
        if (mutation.type === 'childList' && mutation.removedNodes.length > 0) {
          // Look for message container being cleared
          const messageContainer = document.querySelector('[class*="message"], [class*="chat"]')
          if (messageContainer && messageContainer.children.length === 0) {
            setShowRecommendations(true)
          }
        }

        // Check if messages were added (user sent a message)
        if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
          // Look for new messages being added
          const hasMessages = document.querySelector('[class*="message"], [class*="Message"]')
          if (hasMessages && showRecommendations) {
            // Hide recommendations after first message
            setShowRecommendations(false)
          }
        }
      })
    })

    // Start observing after a delay to ensure C1Chat is mounted
    const timeoutId = setTimeout(() => {
      const chatContainer = document.querySelector('[class*="chat"], [class*="container"]')
      if (chatContainer) {
        observer.observe(chatContainer, {
          childList: true,
          subtree: true
        })
      }
    }, 1000)

    // Listen for clicks on elements that might trigger new chat
    document.addEventListener('click', (e) => {
      const target = e.target as HTMLElement
      if (target.textContent?.toLowerCase().includes('new chat') ||
        target.getAttribute('aria-label')?.toLowerCase().includes('new chat')) {
        setTimeout(() => setShowRecommendations(true), 100)
      }
    })

    return () => {
      observer.disconnect()
      clearTimeout(timeoutId)
    }
  }, [showRecommendations])

  // Inject recommendations directly into the chat DOM
  useEffect(() => {
    if (!showRecommendations) {
      // Remove injected recommendations if they exist
      const injected = document.querySelector('.recommendations-wrapper-injected')
      if (injected) {
        injected.remove()
      }
      return
    }

    const injectRecommendations = () => {
      // Check if already injected
      if (document.querySelector('.recommendations-wrapper-injected')) {
        return
      }

      // Find the input element
      const inputElement = document.querySelector('textarea, input[type="text"]') as HTMLElement

      if (!inputElement) {
        return
      }

      // Find the parent container to inject before
      const targetContainer = inputElement.closest('[class*="container"], [class*="wrapper"], form, div') as HTMLElement

      if (targetContainer) {
        // Create recommendations HTML
        const recommendationsHTML = `
          <div class="recommendations-wrapper-injected" style="
            margin-bottom: 1rem;
            width: 100%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
          ">
            <div class="recommendations-container">
              ${recommendations.map((rec, index) => `
                <div class="recommendation-box" data-rec-index="${index}">
                  <span class="recommendation-icon">${rec.icon}</span>
                  <p class="recommendation-text">${rec.text}</p>
                </div>
              `).join('')}
            </div>
          </div>
        `

        // Insert before the input container
        targetContainer.insertAdjacentHTML('beforebegin', recommendationsHTML)

        // Add click handlers
        document.querySelectorAll('.recommendation-box').forEach((box, index) => {
          box.addEventListener('click', (e) => {
            handleRecommendationClick(recommendations[index].text, e as any)
          })
        })
      }
    }

    // Try to inject with delays - store timeout IDs to clear them
    const timeout1 = setTimeout(injectRecommendations, 500)
    const timeout2 = setTimeout(injectRecommendations, 1000)
    const timeout3 = setTimeout(injectRecommendations, 2000)

    // Cleanup function - clear timeouts and remove injected elements
    return () => {
      clearTimeout(timeout1)
      clearTimeout(timeout2)
      clearTimeout(timeout3)
      const injected = document.querySelector('.recommendations-wrapper-injected')
      if (injected) {
        injected.remove()
      }
    }
  }, [showRecommendations, recommendations])

  return (
    <div className='app-container'>
      <ThemeProvider mode="dark">
        {/* Recommendations are now injected directly into chat DOM */}

        <div className='app-container'>
          <ThemeProvider mode="dark">
            <C1Chat
              apiUrl='https://marketinsight-skgl.onrender.com/api/chat'
              agentName='Market Insight'
              logoUrl='/icon.png'
              formFactor='full-page'
            />
          </ThemeProvider>
        </div>

      </ThemeProvider>
    </div>

  )
}

export default App