const setUser = (state = {user: []}) => {
    return {
        type: 'SET_USER',
        user: user
    }
}

export default setUser