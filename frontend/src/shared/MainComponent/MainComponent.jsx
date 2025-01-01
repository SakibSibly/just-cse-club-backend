import Navbar from "../../components/NavBar/Navbar"

const MainComponent = ({ children }) => {
    return (
        <>
            <Navbar />
            { children }
        </>
    );
}

export default MainComponent;