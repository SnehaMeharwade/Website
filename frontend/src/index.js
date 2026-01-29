import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const app = express();

app.use(cors({
  origin: [
    "https://697bb70d4e69b88edd8ca36c--hrmslite4.netlify.app","https://hrmslite6.netlify.app/","https://hrmslite4.netlify.app/"
  ]
}));

app.use(express.json());
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
