document.addEventListener('DOMContentLoaded', () => {
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

    submitButton.addEventListener("click", () => {
        // Collect input values
        const vizGoal = document.getElementById("viz-goal-choice").value;
        const targetAudience = document.getElementById("target-audience-choice").value;
        const visualStyle = document.getElementById("visual-style-choice").value;
        const fileInput = document.getElementById("uploaded-file");

        if (!vizGoal || !targetAudience || !visualStyle || !fileInput.files.length) {
            alert("Please complete all fields before submitting.");
            return;
        }

        // Prepare data for API call
        const formData = new FormData();
        formData.append("visualization_goal", vizGoal);
        formData.append("target_audience", targetAudience);
        formData.append("visual_style", visualStyle);
        formData.append("file", fileInput.files[0]);

        // API call
        fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log("API Response:", data);
            return new Promise(resolve => setTimeout(resolve, 2000)).then(() => {
                return fetch("http://127.0.0.1:5000/get-image", {
                    method: "GET",
                });
            });
        })
        .then(response => response.blob()) 
        .then(imageBlob => {
            // Create a URL for the image and set it as the src of the <img> element
            const newImageUrl = URL.createObjectURL(imageBlob);
            const imageElement = document.getElementById("visualization-image");
            imageElement.src = newImageUrl;
        })
        .catch(error => {
            console.error("Error calling API:", error);
        });
    });
    




});