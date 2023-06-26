import React, {useState, useEffect} from 'react';
import {Link,useNavigate} from 'react-router-dom';

import Logo from "../assests/logo.png";
import {connect} from 'react-redux';

import { getUser } from '../redux/actions/setUserAction';

const Navbar = (props) => {

    const [user, setUser] = useState([]);

    useEffect(() => {
        (
           getUser 
        )();
    },[])

    return (
        <nav className="navbar navbar-expand-lg navbar-light sticky-top" style={{background:"#fff"}}>>
            <div className="container">
                <Link className="navbar-brand text-primary" to="/">
                    <img src={Logo} alt="logo" style={{height:"2em",width:"2em"}} />
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarNavDropdown">
                    <div className="ms-auto">
                        <form  className="d-flex" id="search__box">
                            <input className="form-control me-2" name="query" type="search" placeholder="search posts" aria-label="Search" style={{border:"none",background:"#f0f5fa"}}
                                    />
                            <button className="btn btn-sm btn-outline-primary" type="submit" style={{border:"none"}}> <i className="fas fa-search"/> </button>
                        </form>
                    </div>

                    <ul className="ms-auto navbar-nav">
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <i className="fas fa-user-circle" />
                            </a>
                            {user.data?
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><Link className="dropdown-item" to="/profile">Profile</Link></li>
                                    <li><Link className="dropdown-item" to="/logout">Logout</Link></li>
                                </ul> :
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                    <li><Link className="dropdown-item" to="/login">Login</Link></li>
                                    <li><Link className="dropdown-item" to="/register">Signup</Link></li>
                                </ul>
                            }
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;