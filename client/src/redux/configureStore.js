import { createStore } from 'redux';
import { setUserReducer } from './reducer/setUserReducer';

export const configureStore = () => createStore(setUserReducer);