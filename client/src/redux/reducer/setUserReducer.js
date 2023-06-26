import Types from '../actions/types';

const initialState = {
    user: []
};

export const setUserReducer = (state = initialState, action) => {
    switch (action.type) {
        case Types.GET_USER:
            return {
                ...state,
                user: action.user,
            }
        default: return state;
    }
}