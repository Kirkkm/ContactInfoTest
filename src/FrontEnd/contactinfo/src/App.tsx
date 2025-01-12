import React from 'react';
import './App.css';
import { useState } from 'react';
import { ContactInfo } from './types/ContactInfo';
import { postContactInfo } from './services/OutboundContactInfoService'

function App() {

  const [inputs, setInputs] = useState<ContactInfo>({
    name: '',
    dateOfBirth: undefined,
    phoneNumber: '',
    email: '',
    comments: undefined
  });
  const handleTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }
  
  const [textarea, setTextArea] = useState('Please leave a comment');
  const handleTextAreaChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setTextArea(event.target.value)
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    postContactInfo({...inputs, comments: textarea})
    console.log(inputs, textarea)
  }

  return (
    <div className="App">
      <header className="App-header">
        <h2>Contact Info</h2>
        <form onSubmit={handleSubmit}>
          <label>Name:
            <input type='text' name='name' onChange={handleTextChange}/>
          </label>
          <br/>
          <label>Date of Birth:
            <input type='text' name='dateOfBirth' onChange={handleTextChange}/>
          </label>
          <label>Phone Number:
            <input type='text' name='phoneNumber' onChange={handleTextChange}/>
          </label>
          <label>Email:
            <input type='text' name='email' onChange={handleTextChange}/>
          </label>
          <textarea name='comments' value = {textarea} onChange={handleTextAreaChange} />

          <input type='submit'/>
          
        </form>
      </header>
    </div>
  );
}

export default App;
