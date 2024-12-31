import react from 'react'
import { BrowserRouter as Router, Route, Navigate } from 'react-router-dom'
import Home from "./pages/Home/Home"
import Login from "./pages/Login/Login"
import Register from "./pages/Register/Register"
import Treasury from './pages/Treasury/Treasury'
import NotFound from "./pages/NotFound/NotFound"
import ProtectedRoute from "./components/ProtectedRoute/ProtectedRoute"

const Logout = () => {
  localStorage.clear()
  return <Navigate to="/login" />
}

const RegisterAndLogout = () => {
  localStorage.clear()
  return <Register />
} 


function App() {
  return (
    <>
     <BrowserRouter>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/treasury" element={
          <ProtectedRoute>
            <Treasury />
          </ProtectedRoute>} />
        <Route path="*" element={<NotFound />} />
      </Routes>
     </BrowserRouter>
    </>
  )
}

export default App
