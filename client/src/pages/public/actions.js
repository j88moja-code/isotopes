import axios from "axios";
const ROOT_URL = 'http://127.0.0.1:8000/api'

export const loginUser = async (loginPayload) => {
    try {
        let response = await fetch(`${ROOT_URL}/login`,{
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginPayload)
        });

        if(response.status===200) {
            let data = await response.json()
            return data;
        }
        return null;
    }
    catch (err) {
        console.log(err)
    }
}

export const getRoles = async (nextPageURL) => {
    let roles = null;
    let url = `${ROOT_URL}/roles`;

    let response = await fetch(url,{
        method:"GET",
        headers:{
            'Accept':'application/json',
        }
    });

    roles = await response.json();
    return roles;
}

export const registerUser = async (payload) => {
    try {
        let response = await fetch(`${ROOT_URL}register`,{
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if(response.status===201) {
            let data = await response.json()
            return data;
        }
        return null;
    }
    catch (err) {
        console.log(err)
    }
}