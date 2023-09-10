import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';
import Home from './Home';

function App() {
  const [goOn, setGoOn] = useState(false);
  console.log(goOn);
  const handleClick = (e) => {
    console.log(goOn);
    setGoOn(!goOn);
  }

  if (!goOn) {
    return (<div className='start' style={{backgroundImage: "url('images/bg4.jpg')",  backgroundSize: 'cover', height: '100%', width: '100%'}}>

      <img src="./newLogo.png" alt="logo" />
      <button id='startButton' onClick={handleClick} style={{
        width: '200px', height: '50px', fontSize: '50px', textAlign: 'center'
        }}>התחל</button>
    </div>);
  } else {
    return <div><Home /></div>;
  }


    

  {/* <textarea id='srcText' placeholder='הכנס את הטקסט' onChange={handleChange}></textarea>
  <textarea id='destText' value={result}>{result}</textarea>
  <button onClick={handleClick}>הפשט</button> */}
 
}

export default App;
