import "./Navbar.css";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { ACCESS_TOKEN } from "../../constants";


const Navbar = () => {
    const [loggedIn, setLoggedIn] = useState(false);

    useEffect(() => {
        // console.log(localStorage.getItem(ACCESS_TOKEN));
        if (localStorage.getItem(ACCESS_TOKEN)) {
            setLoggedIn(true);
        }
    }
    , []);

    const HandleUserStatus = () => {
        if (loggedIn) {
            return (
                <div>
                    <Link to="/logout">Logout</Link>
                </div>
            )
        } else {
            return (
                <div>
                    <Link to="/login">Login</Link>
                </div>
            )
        }
    }

    return (
        <nav className="navbar">
                <ul className="navbar-menu">
                    <li>
                        <Link to="/home" >Home</Link>
                    </li>
                    <li>
                        <Link to="/about">About</Link>
                    </li>
                    <li>
                        <Link to="/events">Events</Link>
                    </li>
                    <li>
                        <Link to="/notices">Notices</Link>
                    </li>
                    <li>
                        <Link to="/treasury">Treasury</Link>
                    </li>
                </ul>
                <div>
                    <ul className="navbar-menu">
                        <li>
                            <HandleUserStatus />
                        </li>
                    </ul>
                </div>
        </nav>
    );
};

export default Navbar;