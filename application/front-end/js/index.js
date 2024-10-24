document.addEventListener('DOMContentLoaded', () => {
    let viz_goal = "analyze";
    let target_audience = "experts";
    let visual_style = "professional";
    let target_variable = "any";
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
    document.querySelector('.target-variable input').addEventListener('input', (event) => {
        let target_variable = event.target.value;
        console.log(target_variable);
    });
    
    
});