import React from 'react';
import ReactDOM from 'react-dom/client';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import App from './App';
import reportWebVitals from './reportWebVitals';
import axios from 'axios';
import {configureStore} from "./redux/configureStore";
import {Provider} from "react-redux";

const defaultTheme = createTheme();

// Alert Options
const alertOptions = {
    timeout: 3000,
    position: 'top center'
}

axios.defaults.baseURL = 'http://localhost:8000/api/';
axios.defaults.withCredentials = true;
axios.defaults.headers.Authorization = `Bearer ${localStorage.getItem('token')}`;

const store = configureStore();

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <Provider store={store}>
      <ThemeProvider theme={defaultTheme}/>
      <CssBaseline />
      <App />
      </Provider>
  </React.StrictMode>
);

reportWebVitals();
