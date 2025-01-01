import { useState } from "react";
import "./Login.css";
import api from "../../api";
import { ACCESS_TOKEN } from "../../constants";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {

            
            const response = await api.post("api/token/", {
                email,
                password
            });
            
            // console.log(response.data);
            
            if (response.data.access) {
                console.log("SUCCESS");
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                window.location.href = "/";
            } else {
                setErrorMessage("Invalid credentials. Please try again.");
            }
        } catch (error) {
            console.error(error);
            setErrorMessage("Invalid credentials. Please try again.");
        }
    };

    return (
        <div className="login-container">
            <form className="login-form" onSubmit={handleSubmit}>
                <h2>Login</h2>
                {errorMessage && <p className="error-message">{errorMessage}</p>}
                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        id="email"
                        placeholder="Enter your email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        placeholder="Enter your password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" className="login-button">
                    Login
                </button>
            </form>
        </div>
    );
};

export default Login;
