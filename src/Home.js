import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';
import Navbar from './Navbar';

function Home() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');
  const [clicked, setClicked] = useState(false);
  const [vowels, setVowels] = useState(false);
  const [showed, setShowed] = useState(true);
  const [digitsToWords, setDigitsToWords] = useState(true);

  const [textStyleSrc, setTextStyleSrc] = useState({ fontSize: '25px', width: '500px' });
  const [textStyleDst, setTextStyleDst] = useState({ fontSize: '25px', width: '500px' });

  const translateText = async () => {
    try {
      const response = await fetch('/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          // Include any required data for the Selenium script here
        })
      });
  
      if (response.ok) {
        const result = await response.json();
        // Use the result data as needed
        console.log(result);
        setResult(result);
      } else {
        // Handle error response
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      // Handle network or other errors
      console.error('Error:', error.message);
    }
  };
  
  


  const handleClick = async ({ target }) => {
    if (input != '') {
      setClicked(true);
      let { id } = target;
      // const response = await axios.get(`http://localhost:5000/addFeature/ שכתב לי בבקשה את הטקסט הבא להיות יותר קצר, במשלב לשוני נמוך יותר: ${input}`);
      // console.log(response.data);
      let level=id.replace("level","");
  
      const response = await axios.get(`http://localhost:5000/translate/${input}/${level}`);
      //const response = await axios.get(`http://localhost:5000/getText/${input}`);
  
  
      // Call the translateText function when needed, e.g., on a button click
      //translateText();
      setResult(response.data);
    }
  }

  const handleChange = ({target}) => {
    const { value } = target;
    console.log(value);
    setInput(value);
    if (value == '') {
      setResult('');
    } 
  }

 

  const handleClickLevel = async({ target }) => {
    let id = target.id;
    console.log(id);
    if (id == 'addVowels') {
      setVowels(!vowels);
    }
    if (id == 'increase') {
      let fontS = textStyleDst.fontSize.slice(0, -2);
      let newSize = fontS -0 + 2 + 'px';
      setTextStyleDst({ ...textStyleDst, fontSize: newSize });
    }
    if (id == 'decrease') {
      let fontS = textStyleDst.fontSize.slice(0, -2);
      let newSize = fontS - 2 + 'px';
      console.log(newSize);
      setTextStyleDst({ ...textStyleDst, fontSize: newSize });
    }
    if (id == 'switchNumbers') {
      if (result != '') {
        setDigitsToWords(digitsToWords);
        let level;
        if (digitsToWords) {
          level = 4;
        } else {
          level = 5;
        }
        const response = await axios.get(`http://localhost:5000/translate/${result}/${level}`);
        setResult(response.data);
        }
      
    }
  }

  const handleClearButton = ({ target }) => {
    setInput('');
    setResult('');
    setClicked(false);
    setVowels(false);
    setShowed(true);
    setDigitsToWords(true);
  }

  const handleShowButton = () => {
    if (!showed) {
      setTextStyleDst({ ...textStyleDst, width: '500px' });
    } else {
      setTextStyleDst({ ...textStyleDst, width: '900px' });
    }
    setShowed(!showed);

  }

  return (
    <div>
      <div className="header">
        {/* Your header content goes here */}
        {/* <img src="images/myLogo.jpg"/> */}
        {/* <h1>SIMPLIFY</h1> */}
        <img src="./newLogo.png" alt="logo" style={{width: '300px', height: '150px', marginTop: '30px'}}/>
      </div>
      {/* <Navbar/> */}
      <div className="navbar">
      <a id='level1' onClick={handleClick} disabled={result==''}>הפשט לרמה נמוכה</a>
      <a id='level2' onClick={handleClick} disabled={result==''}>הפשט לרמה בינונית</a>
      <a id='level3' onClick={handleClick} disabled={result==''}>הפשט לרמה גבוהה</a>
      <a id='increase' onClick={handleClickLevel}disabled={result==''}>הגדל את הטקסט</a>
      <a id='decrease' onClick={handleClickLevel} disabled={result==''}>הקטן את הטקסט</a>
      <a id='addVowels' onClick={handleClickLevel} disabled={result==''}>{vowels? 'הסר ניקוד': 'הוסף ניקוד'}</a>
      <a id='switchNumbers' onClick={handleClickLevel} disabled={result==''}>{digitsToWords? 'המר ספרות למילים': 'המר מילים לספרות'}</a>
    </div>
      <div className='container'>
        {/* <div className='sideButtons'> */}
          {clicked && <button className='sideButton' onClick={handleShowButton}>{showed ? 'הסתר טקסט מקור' : 'הצג טקסט מקור'}</button>}
          {clicked && <button className='sideButton' onClick={handleClearButton}>נקה טקסט</button>}
        {/* </div> */}
        {/* <div className='texts'> */}
          {showed && <textarea style={textStyleSrc} className='text' placeholder='הכנס טקסט' value={input} onChange={handleChange}></textarea>}
          
          {clicked  &&
            <section id='dstText' className='text' style={textStyleDst}>{clicked && result == '' ? 'טוען...' : result}</section>}
        {/* </div> */}
        
      
      {/* <button onClick={handleClick} disabled={input==''}>תרגם</button> */}

      </div>
      </div>

  );
}


export default Home;

// function TranslateComponent() {
//   const [text, setText] = useState('');
//   const [translatedText, setTranslatedText] = useState('');
  
//   const translateText = () => {
//     axios
//       .post(
//         'https://translation.googleapis.com/language/translate/v2',
//         {},
//         {
//           params: {
//             q: text,
//             target: 'en', // Target language (e.g., 'en' for English)
//             key: 'YOUR_API_KEY', // Replace with your actual API key
//           },
//         }
//       )
//       .then((response) => {
//         const translation = response.data.data.translations[0].translatedText;
//         setTranslatedText(translation);
//       })
//       .catch((error) => {
//         console.error('Translation error:', error);
//       });
//   };
  
//   // Rest of the component code
// }

// function TranslateComponent() {
//   const [text, setText] = useState('');
//   const [translatedText, setTranslatedText] = useState('');
  
//   const translateText = () => {
//     // Translation request code
//     axios
//       .post(
//         'https://translation.googleapis.com/language/translate/v2',
//         {},
//         {
//           params: {
//             q: text,
//             target: 'en', // Target language (e.g., 'en' for English)
//             key: 'YOUR_API_KEY', // Replace with your actual API key
//           },
//         }
//       )
//       .then((response) => {
//         const translation = response.data.data.translations[0].translatedText;
//         setTranslatedText(translation);
//       })
//       .catch((error) => {
//         console.error('Translation error:', error);
//   };
  
//   return (
//     <div>
//       <input
//         type="text"
//         value={text}
//         onChange={(e) => setText(e.target.value)}
//       />
//       <button onClick={translateText}>Translate</button>
//       <p>{translatedText}</p>
//     </div>
//   );
// }



