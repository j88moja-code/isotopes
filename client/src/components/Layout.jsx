import React, {useEffect, useState} from 'react';
import axios from "axios";
import {useNavigate} from 'react-router-dom';
import Navbar from "./Navbar";

const Layout = (props) => {
    const [redirect, setRedirect] = useState(false);

    let navigator = useNavigate();
    useEffect(() => {
        (
            async () => {
                try {
                    const {data} = await axios.get('user');

                } catch (e) {
                    setRedirect(true);
                }
            }
        )();
    }, [])

    if (redirect) {
        navigator('/login');
    }

    return (
        <div>
            <Navbar />
            {props.children}
        </div>
    );
};

export default Layout;