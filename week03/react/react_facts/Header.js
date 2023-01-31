
// Create a navigation bar for the top of a page.
function Header() {
    return (
        <header>
            <nav className="nav-bar">
                <div>
                    <img src="./react-logo.png" id="nav-logo" />
                    <a href="#">ReactFacts</a>
                </div>
                <ul className="nav-items">
                    <li>About</li>
                    <li>Courses</li>
                    <li>Contact</li>
                </ul>
            </nav>
        </header>
    )
}

// Export this function so the main script can use it.
export default Header