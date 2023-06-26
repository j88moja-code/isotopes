import {createContext, useReducer} from "react";

const userState = {
    data: JSON.parse(localStorage.getItem('jwt')) || null
}

export const userReduce = createContext(userState);

function reducer(state,action) {
    switch(action.type) {
        case "login_success":
            localStorage.setItem('jwt',JSON.stringify(action.payload))
            return {...state,data:JSON.parse(localStorage.getItem("jwt"))}
        case "logout":
            localStorage.removeItem("jwt")
            return {...state,data:null}
        default:
            return state;
    }
}

export const UserProvider = ({children}) => {
    const [state,dispatch] = useReducer(reducer,userState)

    function login_success(data) {
        dispatch({
            type:"login_success",
            payload:{...data}
        })
    }

    function logout() {
        dispatch({type:"logout"})
    }

    return (<userReduce.Provider value={{
        user:state,login_success,logout
    }}>
        {children}
    </userReduce.Provider>)
}