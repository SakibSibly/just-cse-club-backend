import react from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Home from "./pages/Home/Home"
import Login from "./pages/Login/Login"
import Register from "./pages/Register/Register"
import Events from './pages/Events/Events'
import About from './pages/About/About'
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
        <Route path='/events' element={<Events />} />
        <Route path='/about' element={<About />} />
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
