
// Creates a navigation bar for the top of a page.
function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="#">Navbar</a>

            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                <li className="nav-item active">
                    <a className="nav-link" href="#">Home</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Link</a>
                </li>
                <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                    </a>
                    <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a className="dropdown-item" href="#">Action</a>
                    <a className="dropdown-item" href="#">Another action</a>
                    <div className="dropdown-divider"></div>
                    <a className="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
                </ul>
            </div>
        </nav>
    )
}

// Creates the main content of the page.
function MainContent() {
    return (
        <div className="main_content">
            <h1>Hello, world!</h1>
            <p>My name is Heather, and I am learning React.</p>
            Fruits:<br />
            <ul><li>apples</li><li>bananas</li><li>cherries</li></ul>
        </div>
    )
}


let root_div = document.getElementById("root")

// Add the nav bar and main content to the page.
ReactDOM.render(
    <div>
        <Navbar />
        <MainContent />
    </div>, 
    root_div
)
