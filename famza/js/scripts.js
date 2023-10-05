document.addEventListener('DOMContentLoaded', () => {
    // Sample project data (replace with your own data)
    const projects = [
        {
            title: 'Project 1',
            description: 'Description of Project 1',
            url: '#',
        },
        {
            title: 'Project 2',
            description: 'Description of Project 2',
            url: '#',
        },
        // Add more projects as needed
    ];

    const projectSection = document.getElementById('projects');

    // Function to create project elements
    function createProjectElement(project) {
        const projectDiv = document.createElement('div');
        projectDiv.classList.add('project');

        const title = document.createElement('h3');
        title.textContent = project.title;

        const description = document.createElement('p');
        description.textContent = project.description;

        const link = document.createElement('a');
        link.textContent = 'View Project';
        link.href = project.url;

        projectDiv.appendChild(title);
        projectDiv.appendChild(description);
        projectDiv.appendChild(link);

        return projectDiv;
    }

    // Populate the project section
    projects.forEach(project => {
        const projectElement = createProjectElement(project);
        projectSection.appendChild(projectElement);
    });
});

function toggleDetails(targetId) {
    var target = document.getElementById(targetId);
    if (target.style.display === "none") {
        target.style.display = "block";
    } else {
        target.style.display = "none";
    }
}


document.addEventListener("DOMContentLoaded", function () {
    // Check if user's preference is dark mode
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

    // Function to toggle between light and dark mode
    function toggleTheme() {
        const body = document.body;
        body.classList.toggle("dark-mode");

        // Save user's preference in local storage
        const isDarkMode = body.classList.contains("dark-mode");
        localStorage.setItem("darkMode", isDarkMode);
    }

    // Initialize theme based on user's preference or default to light mode
    if (localStorage.getItem("darkMode") === "true" || prefersDark) {
        document.body.classList.add("dark-mode");
    }

    // Attach click event listener to the theme toggle button
    const themeToggle = document.getElementById("theme-toggle");
    if (themeToggle) {
        themeToggle.addEventListener("click", toggleTheme);
    }
});
