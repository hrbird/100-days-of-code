
// Creates a navigation bar for the top of a page.
function Navbar() {
    return (
        <nav className="nav_bar">
            <a href="#">Website Name</a> |&nbsp;
            <a href="#">About</a> |&nbsp;
            <a href="https://reactjs.org">React</a> |&nbsp;
            <a href="#">Contact</a>
        </nav>
    )
}

// Creates the main content of the page.
function MainContent() {
    return (
        <div className="main_content">
            <h1>Hello, world!</h1>
            <p>My name is Heather, and I am learning React.</p>
        </div>
    )
}

// Creates an unordered list of companies that use React.
function ReactCompaniesList() {
    return (
        <div className="companies_list">
            <strong>Companies that use React:</strong>
            <br />
            <ul>
                <li>Netflix</li>
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