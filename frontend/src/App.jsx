import "./assets/css/App.css"
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import MainComponent from './shared/MainComponent/MainComponent'
import Home from "./pages/Home/Home"
import Login from "./pages/Login/Login"
import Register from "./pages/Register/Register"
import Events from './pages/Events/Events'
import Notices from './pages/Notices/Notices'
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
        <Route path="/" element={<MainComponent children={<Home />} />} />
        <Route path="/home" element={<MainComponent children={<Home />} />} />
        <Route path="/login" element={<MainComponent children={<Login />} />} />
        <Route path="/register" element={<MainComponent children={<RegisterAndLogout />} />} />
        <Route path="/logout" element={<Logout />} />
        <Route path='/events' element={<MainComponent children={<Events />} />} />
        <Route path='/notices' element={<MainComponent children={<Notices />} />} />
        <Route path='/about' element={<MainComponent children={<About />} />} />
        <Route path="/treasury" element={
          <ProtectedRoute>
            <MainComponent children={<Treasury />} />
          </ProtectedRoute>} />
        <Route path="*" element={<NotFound />} />
      </Routes>
     </BrowserRouter>
    </>
  )
}

export default App
