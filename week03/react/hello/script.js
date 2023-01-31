
// Creates a navigation bar for the top of a page.
function Navbar() {
    return (
        <nav>
            <h1>Website Name</h1>
            <ul>
                <li>Pricing</li>
                <li>About</li>
                <li>Contact</li>
            </ul>
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

// Creates an unordered list of fruit.
function FruitList() {
    return (
        <div className="fruits_list">
            Fruits:<br />
            <ul><li>apples</li><li>bananas</li><li>cherries</li></ul>
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
        <FruitList />
    </div>
)