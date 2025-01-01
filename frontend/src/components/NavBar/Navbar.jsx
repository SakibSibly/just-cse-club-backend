import "./Navbar.css";
import { Link } from "react-router-dom";


const Navbar = () => {
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
        </nav>
    );
};

export default Navbar;