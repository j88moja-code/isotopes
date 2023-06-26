import axios from "axios";
const ROOT_URL = 'http://127.0.0.1:8000/api'

export const getRoles = async (nextPageURL) => {
    let roles = null;
    let url = `${ROOT_URL}/roles`;

    let response = await axios.get(url);

    roles = await response.data;
    return roles;
}
