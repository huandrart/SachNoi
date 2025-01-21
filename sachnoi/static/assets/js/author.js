document.addEventListener("DOMContentLoaded", function () {
    const containers = document.querySelectorAll(".audiobook-list");

    containers.forEach(container => {
        const items = Array.from(container.querySelectorAll(".audiobook-item"));
        let sortState = 'default'; 
        const sortButton = container.previousElementSibling.querySelector("h2");
        if (sortButton) {
            sortButton.addEventListener("click", (e) => {
                e.preventDefault(); 
                if (sortState === 'default') {
                    items.sort((a, b) => {
                        const authorA = a.querySelector(".author").textContent.trim().toLowerCase();
                        const authorB = b.querySelector(".author").textContent.trim().toLowerCase();
                        return authorA.localeCompare(authorB);
                    });
                    sortState = 'asc'; 
                } else if (sortState === 'asc') {
                    items.sort((a, b) => {
                        const authorA = a.querySelector(".author").textContent.trim().toLowerCase();
                        const authorB = b.querySelector(".author").textContent.trim().toLowerCase();
                        return authorB.localeCompare(authorA);
                    });
                    sortState = 'desc'; 
                } else {
                    items.sort(() => 0); 
                    sortState = 'default'; 
                }

                container.innerHTML = "";

                
                items.forEach(item => container.appendChild(item));
            });
        }
    });
});


