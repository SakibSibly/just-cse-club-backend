import React, { useState } from "react";
import "./Register.css"; // Optional: Add styles if needed
import api from "../../api";

const Register = () => {
  const [stage, setStage] = useState(1); // Stage 1: Email, Stage 2: OTP, Stage 3: Other details
  const [email, setEmail] = useState("");
  const [otp, setOtp] = useState("");
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    username: "",
    city: "",
    password1: "",
    password2: "",
  });
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const handleEmailSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("/api/verify/email/", {
          email: email
      });

      if (response.status === 200) {
        setSuccessMessage("OTP sent to your email.");
        setErrorMessage("");
        setStage(2); // Move to OTP stage
      } else {
        const errorData = await response.data;
        setErrorMessage(errorData.message || "Failed to send OTP.");
      }
    } catch (error) {
      setErrorMessage("An error occurred. Please try again later.");
      console.error(error);
    }
  };

  const handleOtpSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("api/verify/otp/", {
        email: email,
        otp: otp
      });

      if (response.status === 200) {
        setSuccessMessage("OTP verified. Please complete your registration.");
        setErrorMessage("");
        setStage(3); // Move to other details stage
      } else {
        const errorData = await response.data;
        setErrorMessage(errorData.message || "Invalid OTP.");
      }
    } catch (error) {
      setErrorMessage("An error occurred. Please try again later.");
      console.error(error);
    }
  };

  const handleFinalSubmit = async (e) => {
    e.preventDefault();

    if (formData.password1 !== formData.password2) {
      setErrorMessage("Passwords do not match.");
      return;
    }

    try {
      const response = await api.post("/api/register/", {
          email: email,
          first_name: formData.first_name,
          last_name: formData.last_name,
          username: formData.username,
          city: formData.city,
          password: formData.password1
      });

      if (response.status === 201) {
        setSuccessMessage("Account created successfully.");
        setErrorMessage("");
        setFormData({
          first_name: "",
          last_name: "",
          username: "",
          city: "",
          password1: "",
          password2: "",
        });
        setStage(1); // Reset to the first stage
        window.location.href = "/login";

      } else {
        const errorData = await response.data;
        setErrorMessage(errorData.message || "Registration failed.");
      }
    } catch (error) {
      setErrorMessage(error.response.data.error)
      console.error(error);
    }
  };

  return (
    <div className="register-container">
      {stage === 1 && (
        <form className="register-form" onSubmit={handleEmailSubmit}>
          <h2>Register</h2>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          {successMessage && <p className="success-message">{successMessage}</p>}
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="register-button">Send OTP</button>
        </form>
      )}

      {stage === 2 && (
        <form className="register-form" onSubmit={handleOtpSubmit}>
          <h2>Verify Email</h2>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          {successMessage && <p className="success-message">{successMessage}</p>}
          <div className="form-group">
            <label htmlFor="otp">OTP</label>
            <input
              type="text"
              id="otp"
              name="otp"
              value={otp}
              onChange={(e) => setOtp(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="register-button">Verify OTP</button>
        </form>
      )}

      {stage === 3 && (
        <form className="register-form" onSubmit={handleFinalSubmit}>
          <h2>Complete Registration</h2>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          {successMessage && <p className="success-message">{successMessage}</p>}
          <div className="form-group">
            <label htmlFor="first_name">First Name</label>
            <input
              type="text"
              id="first_name"
              name="first_name"
              value={formData.first_name}
              onChange={(e) => setFormData({ ...formData, first_name: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="last_name">Last Name</label>
            <input
              type="text"
              id="last_name"
              name="last_name"
              value={formData.last_name}
              onChange={(e) => setFormData({ ...formData, last_name: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={(e) => setFormData({ ...formData, username: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="city">City</label>
            <input
              type="text"
              id="city"
              name="city"
              value={formData.city}
              onChange={(e) => setFormData({ ...formData, city: e.target.value })}
            />
          </div>
          <div className="form-group">
            <label htmlFor="password1">Password</label>
            <input
              type="password"
              id="password1"
              name="password1"
              value={formData.password1}
              onChange={(e) => setFormData({ ...formData, password1: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password2">Confirm Password</label>
            <input
              type="password"
              id="password2"
              name="password2"
              value={formData.password2}
              onChange={(e) => setFormData({ ...formData, password2: e.target.value })}
              required
            />
          </div>
          <button type="submit" className="register-button">Register</button>
        </form>
      )}
    </div>
  );
};

export default Register;
