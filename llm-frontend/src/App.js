import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  useEffect(() => {
    // Set the title of the page
    document.title = "Waddles Chat";

    // Set the custom favicon
    const favicon = document.createElement("link");
    favicon.rel = "icon";
    favicon.href = `${process.env.PUBLIC_URL}/assets/favicon.ico`;
    document.head.appendChild(favicon);

    // Clean up function to remove the favicon when the component unmounts
    return () => {
      document.head.removeChild(favicon);
    };
  }, []); // Empty dependency array ensures this effect runs only once, similar to componentDidMount

  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false); // Add loading state

  const makeApiCall = async (userInput) => {
    try {
      setIsLoading(true); // Set loading to true before making the API call

      const response = await fetch("http://0.0.0.0:8000/waddles/invoke", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input: { input: userInput } }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data = await response.json();
      const data2 = data.output.output;

      // Remove the loading message and add the actual response
      setMessages((prevMessages) => [
        ...prevMessages.filter((message) => message.text !== "Loading..."),
        { type: "bot", text: data2 },
      ]);
    } catch (error) {
      console.error("Failed to fetch:", error);
      // Handle error
    } finally {
      setIsLoading(false); // Set loading to false after the API call completes
    }
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = () => {
    if (inputValue.trim() !== "") {
      setMessages((prevMessages) => [
        ...prevMessages,
        { type: "user", text: inputValue },
      ]);
      makeApiCall(inputValue);
      setInputValue("");
    }
  };

  return (
    <div className="App">
      <title>My Blog</title>
      <header className="App-header">
        <img
          src={`${process.env.PUBLIC_URL}/assets/waddles.png`}
          className="App-logo"
          alt="logo"
        />
        <h1>Waddle Chat</h1>
      </header>
      <div className="chat-container">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message-container ${message.type}-message`}
          >
            <img
              src={
                message.type === "user"
                  ? `${process.env.PUBLIC_URL}/assets/oski.jpg`
                  : `${process.env.PUBLIC_URL}/assets/waddles.png`
              }
              alt={message.type}
            />
            <div className="message">
              <p className="message-text">{message.text}</p>
            </div>
          </div>
        ))}
        {isLoading && ( // Render loading message if isLoading is true
          <div className="message-container bot-message">
            <img
              src={`${process.env.PUBLIC_URL}/assets/waddles.png`}
              alt="bot"
            />
            <div className="message">
              <p className="message-text">
                <span className="loading-dots">
                  Loading<span>.</span>
                  <span>.</span>
                  <span>.</span>
                </span>
              </p>
            </div>
          </div>
        )}
      </div>
      <div className="input-container">
        <input
          type="text"
          placeholder="Waddle is looking at you..."
          value={inputValue}
          onChange={handleInputChange}
          onKeyDown={(event) => {
            if (event.key === "Enter") {
              handleSubmit();
            }
          }}
        />
        <button onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  );
}

export default App;
