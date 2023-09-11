import './Input.css'
import { useState } from 'react'
import axios from 'axios'

function Input() {
  const [input, setInput] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    const parameter = { input }

    axios
      .post('http://localhost:8080/analyze', parameter)
      .then((res) => {
        const data = res.data.data
        const output = `Result: ${data.result}`
        alert(output)
        reset()
      })
      .catch((error) => alert(`Error`))
  }

  const reset = () => {
    setInput('')
  }

  return (
    <div className="glass">
      <form onSubmit={(e) => handleSubmit(e)} className="glass__form">
        <h4>Sentiment Analysis</h4>
        <div className="glass__form__group">
          <input
            id="title"
            className="glass__form__input"
            placeholder="Input: "
            required
            autoFocus
            title="Input:"
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
        </div>

        <div className="glass__form__group">
          <button type="submit" className="glass__form__btn">
            Submit
          </button>
        </div>
      </form>
    </div>
  )
}

export default Input