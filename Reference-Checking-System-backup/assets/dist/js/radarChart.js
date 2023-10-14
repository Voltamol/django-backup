// Get the canvas element
var ctx = document.getElementById('radarChart').getContext('2d');

// Define the data for the chart
var data = {
labels: ['TeamWork', 'Problem solving', 'Time Management', 'Quality of Work', 'Integrity','Reliable'],
datasets: [
    {
    label: 'BakerTilly',
    data: [10, 20, 30, 40, 50,50],
    backgroundColor: 'rgba(250, 10, 58, 0.886)', // Set the background color for the chart area
    borderColor: 'rgba(250, 10, 58, 0.886)', // Set the border color for the data points
    borderWidth: 1 // Set the border width for the data points
    },
    {
        label: 'KPMG',
        data: [48, 45, 40, 30, 25,50],
        backgroundColor: 'rgba(10, 250, 150, 0.9)', // Set the background color for the chart area
        borderColor: 'rgba(10, 250, 150, 0.9)', // Set the border color for the data points
        borderWidth: 1 // Set the border width for the data points
        },
    {
        label: 'EY',
        data: [20, 50, 35, 48, 40,45],
        backgroundColor: 'rgba(10, 150, 250, 0.886)', // Set the background color for the chart area
        borderColor: 'rgba(10, 150, 250, 0.886)', // Set the border color for the data points
        borderWidth: 1 // Set the border width for the data points
        }
]
};

// Create the radar chart
var radarChart = new Chart(ctx, {
type: 'radar',
data: data,
options: {
    // Additional options for customization
}
});
