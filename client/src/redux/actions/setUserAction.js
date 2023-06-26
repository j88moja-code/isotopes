import axios from "axios";

import Types from './types';

const initialState = {
    user: []
};

export const setUser = (user) => ({
    type: Types.SET_USER,
    user: user
})

export const getUser = () => {
    return dispatch => {
        axios.get('user')
        .then(response => {
            dispatch({type: Types.GET_USER, payload: response.data})
        }
        )
        .catch(error => {
            console.log(error)
        }
        );
        }
    }


