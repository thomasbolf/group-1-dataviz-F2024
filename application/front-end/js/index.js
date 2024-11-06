document.addEventListener("DOMContentLoaded", () => {
    const submitButton = document.getElementById("submit-button");

    submitButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Gather selected options and user input
        const vizGoal = document.getElementById("viz-goal-choice").value;
        const targetAudience = document.getElementById("target-audience-choice").value;
        const visualStyle = document.getElementById("visual-style-choice").value;
        const targetVariable = document.querySelector(".target-variable input").value;
        const fileInput = document.getElementById("uploaded-file");

        // Validate that all necessary fields are filled
        if (!vizGoal || !targetAudience || !visualStyle || !targetVariable || !fileInput.files.length) {
            alert("Please complete all fields before submitting.");
            return;
        }

        // Prepare form data for the API request
        const formData = new FormData();
        formData.append("visualization_goal", vizGoal);
        formData.append("target_audience", targetAudience);
        formData.append("visual_style", visualStyle);
        formData.append("targetVariable", targetVariable);
        formData.append("file", fileInput.files[0]);
        
        try {
            // Show a loading graphic while waiting for API response
            const visualizationImage = document.getElementById("visualization-image");
            visualizationImage.src = "loading-spinner.gif"; // Placeholder for loading image
            //wait 5 seconds
            await fetch("http://127.0.0.1:5000/upload", {
                method: "POST",
                body: formData,
            });
            //await new Promise(resolve => setTimeout(resolve, 5000));
            
            const visualizationResponse = await fetch(`http://127.0.0.1:5000/get-image`);
            
            if (!visualizationResponse.ok) {
                throw new Error("Failed to retrieve generated visualization");
            }

            // Convert the image response to a Blob and create an Object URL for it
            const blob = await visualizationResponse.blob();
            const imageUrl = URL.createObjectURL(blob);

            // Update the image src to display the generated visualization
            visualizationImage.src = imageUrl;
            alert("Visualization generated successfully!");

        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred while generating the visualization. Please try again.");
        }
    });
});
