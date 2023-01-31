
// Creates a navigation bar for the top of a page.
function Navbar() {
    return (
        <nav className="nav_bar">
            <img src="./react-logo.png" width="40px" />
            <a href="#">ReactFacts</a>
            <a href="#">React Course - Project 1</a>
        </nav>
    )
}

// Creates the main content of the page.
function MainContent() {
    return (
        <div className="main_content">
            <h1>Fun facts about React</h1>
            <ul>
                <li>First released in 2013</li>
                <li>Originally created by Jordan Walke</li>
                <li>Has well over 100K stars on GitHub</li>
                <li>Currently is maintained by Meta</li>
                <li>Powers thousands of enterprise websites and mobile apps</li>
            </ul>
        </div>
    )
}

// Creates an unordered list of companies that use React.
function ReactCompaniesList() {
    return (
        <div className="companies_list">
            <h1>Companies that use React:</h1>
            <ul>
                <li>Netlix</li>
                <li>Meta/Facebook</li>
                <li>The New York Times</li>
                <li>Dropbox</li>
                <li>Airbnb</li>
                <li>Uber</li>
            </ul>
        </div>
    )
}

// Get the root div element in the HTML body.
const root = ReactDOM.createRoot(document.getElementById("root"))

// Add the content to the page.
root.render(
    <div>
        <Navbar />
        <MainContent />
        <ReactCompaniesList />
    </div>
)