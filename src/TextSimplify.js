import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';

function TextSimplify() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');
  const handleClick = (e) => {
    //let text = e.target.value;
    //console.log(input);
    setResult(input);

  }

  const handleChange = ({target}) => {
    const { value } = target;
    //console.log(value);
    setInput(value);
  }
  return (
    
    <div className="home">

      <textarea id='srcText' placeholder='הכנס את הטקסט' onChange={handleChange}></textarea>
      <textarea id='destText' value={result}>{result}</textarea>
      <button onClick={handleClick}>הפשט</button>
    </div>
  );
}


export default TextSimplify;

