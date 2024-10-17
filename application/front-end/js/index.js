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
});