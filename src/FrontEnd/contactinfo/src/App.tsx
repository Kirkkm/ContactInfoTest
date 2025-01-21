import React from 'react';
import './App.css';
import { useState } from 'react';
import { ContactInfo } from './types/ContactInfo';
import { postContactInfo } from './services/OutboundContactInfoService'

function App() {

  const [inputs, setInputs] = useState<ContactInfo>({
    Name: '',
    DateOfBirth: undefined,
    PhoneNumber: '',
    Email: '',
    Comments: undefined
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
    postContactInfo({...inputs, Comments: textarea})
    alert('Thank you for submitting your contact info!')
  }

  return (
    <div className="App">
      <header className="App-header">
        <h2>Contact Info</h2>
        <form onSubmit={handleSubmit}>
          <label>Name:
            <input type='text' name='Name' onChange={handleTextChange}/>
          </label>
          <br/>
          <label>Date of Birth:
            <input type='date' name='DateOfBirth' onChange={handleTextChange}/>
          </label>
          <br/>
          <label>Phone Number:
            <input type='text' name='PhoneNumber' onChange={handleTextChange}/>
          </label>
          <br/>
          <label>Email:
            <input type='text' name='Email' onChange={handleTextChange}/>
          </label>
          <br/>
          <label> Comments: 
            <textarea name='Comments' value = {textarea} onChange={handleTextAreaChange} />
          </label>
          
          <input type='submit' value="Submit"/>
          
        </form>
      </header>
    </div>
  );
}

export default App;
