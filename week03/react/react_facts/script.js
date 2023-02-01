
// Create a navigation bar for the top of a page.
function Header() {
    return (
        <header>
            <nav className="nav-bar">
                <img className="nav-logo" src="./react-logo.png" />
                <h3 className="nav-site">ReactFacts</h3>
                <h4 className="nav-title">React Course - Project 1</h4>
            </nav>
        </header>
    )
}

// Creates the main content of the page.
function MainContent() {
    return (
        <main className="main-content">
            <h1 className="main-title">Fun facts about React</h1>
            <ul className="list-facts">
                <li>First released in 2013</li>
                <li>Originally created by Jordan Walke</li>
                <li>Has well over 100K stars on GitHub</li>
                <li>Currently is maintained by Meta</li>
                <li>Powers thousands of enterprise websites and mobile apps, including:</li>
                <ul className="list-companies">
                    <li>Netflix</li>
                    <li>Meta/Facebook</li>
                    <li>The New York Times</li>
                    <li>Dropbox</li>
                    <li>Airbnb</li>
                    <li>Uber</li>
                </ul>
            </ul>
        </main>
    )
}


// Put all of the page content into one div.
function App() {
    return (
        <div>
            <Header />
            <MainContent />
        </div>
    )
}

// Get the root div element in the HTML body.
const root = ReactDOM.createRoot(document.getElementById("root"))

// Add the content to the page.
root.render(
    <App />
)