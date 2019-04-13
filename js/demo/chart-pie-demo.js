// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("sex");
var sex = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Male", "Female"],
    datasets: [{
      data: [75, 125],
      backgroundColor: ["#ADFF2F", "#00FA9A"],
      hoverBackgroundColor: ['#98FB98', '#98FB98'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 0,
  },
});


// Pie Chart Example
var ageChart = document.getElementById("age");
var age = new Chart(ageChart, {
  type: 'doughnut',
  data: {
    labels: ["Toddler", "Child", "Adolescent", "Adult", "Elderly"],
    datasets: [{
      data: [20, 40, 10, 100, 30],
      backgroundColor: ["#D8BFD8", "#DA70D6", "#BA55D3", "#9932CC", "#4B0082"],
      hoverBackgroundColor: ["#E6E6FA", "#E6E6FA", "#E6E6FA", "#E6E6FA", "#E6E6FA"],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 0,
  },
});

// Pie Chart Example
var ethnicityChart = document.getElementById("ethnicity");
var ethnicity = new Chart(ethnicityChart, {
  type: 'doughnut',
  data: {
    labels: ["African/African-American", "Caucasian", "East Asian", "Latino/Hispanic", "Native American/Pacific Islander", "South Asian"],
    datasets: [{
      data: [10, 10, 80, 10, 80, 10],
      backgroundColor: ["#AFEEEE", "#40E0D0", "#48D1CC", "#00CED1", "#20B2AA", "#008B8B"],
      hoverBackgroundColor: ["#E0FFFF", "#E0FFFF", "#E0FFFF", "#E0FFFF", "#E0FFFF", "#E0FFFF"],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 0,
  },
});

