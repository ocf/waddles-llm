import './App.css';
import React, {useState} from 'react';

function App() {
  const makeApiCall = async (userInput) => {
    try {
      const response = await fetch(' http://localhost:8000/waddles', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: userInput }),
      });
  
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
  
      const data = await response.json();
      console.log("Response from server:", data);
      // Handle the response data (e.g., display it in the UI)
    } catch (error) {
      console.error('Failed to fetch:', error);
    }
  };
  const [inputValue, setInputValue] = useState('');
   // Update state based on input
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  // Handle submission
  const handleSubmit = () => {
    // Make the API call here
    makeApiCall(inputValue);
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={`${process.env.PUBLIC_URL}/images.png`} className="App-logo" alt="logo" />
        <p>
          <br></br>
          Welcome to Waddle! Ask your questions
        </p>
        {}
        <input type="text" 
        placeholder="Waddle is looking at you..." 
        value={inputValue} 
        onChange={handleInputChange}
        />
        <button onClick={handleSubmit}>Submit</button>
      </header>
    </div>
  );
}

export default App;
