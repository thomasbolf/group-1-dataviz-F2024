document.addEventListener('DOMContentLoaded', () => {
    // Input handlers
    let viz_goal = "analyze";
    let target_audience = "experts";
    let visual_style = "professional";

    document.getElementById('viz-goal-choice').addEventListener('change', (event) => {
        viz_goal = event.target.value;
        console.log("Visualization Goal:", viz_goal);
    });
    document.getElementById('target-audience-choice').addEventListener('change', (event) => {
        target_audience = event.target.value;
        console.log("Target Audience:", target_audience);
    });
    document.getElementById('visual-style-choice').addEventListener('change', (event) => {
        visual_style = event.target.value;
        console.log("Visual Style:", visual_style);
    });

    const submitButton = document.getElementById("submit-button");

    // Function to fetch and update the image every 10 seconds
function refreshImage() {
    setInterval(() => {
        console.log("Refreshing image...");

        fetch("http://127.0.0.1:5000/get-image", { method: "GET" })
            .then(response => {
                if (!response.ok) {
                    console.log("GET request for image failed with status:", response.status);
                    throw new Error(`Failed to retrieve image. Status: ${response.status}`);
                }
                console.log("GET request for image successful:", response);
                return response.blob();
            })
            .then(imageBlob => {
                const newImageUrl = URL.createObjectURL(imageBlob);
                const imageElement = document.getElementById("visualization-image");
                imageElement.src = newImageUrl;
                console.log("Image URL refreshed to:", newImageUrl);
            })
            .catch(error => {
                console.error("Error refreshing image:", error);
            });
    }, 10000); // Refresh every 10 seconds
}

// Start the image refresh on page load
window.onload = refreshImage;

// Submit button event listener for the "POST" request
submitButton.addEventListener("click", (event) => {
    event.preventDefault();
    console.log("Submit button clicked");

    const vizGoal = document.getElementById("viz-goal-choice").value;
    const targetAudience = document.getElementById("target-audience-choice").value;
    const visualStyle = document.getElementById("visual-style-choice").value;
    const fileInput = document.getElementById("uploaded-file");

    if (!vizGoal || !targetAudience || !visualStyle || !fileInput.files.length) {
        alert("Please complete all fields before submitting.");
        return;
    }

    const formData = new FormData();
    formData.append("visualization_goal", vizGoal);
    formData.append("target_audience", targetAudience);
    formData.append("visual_style", visualStyle);
    formData.append("file", fileInput.files[0]);

    console.log("FormData created:", Array.from(formData.entries()));

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            console.log("POST request failed with status:", response.status);
            throw new Error(`Failed to upload file. Status: ${response.status}`);
        }
        console.log("POST request successful:", response);
        return response.json();
    })
    .then(data => {
        console.log("POST response data:", data);
        // Optionally, trigger some visual feedback after successful POST
    })
    .catch(error => {
        console.error("Error during POST request:", error);
        alert(`An error occurred: ${error.message}`);
    });
});

});
