
  window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
      title:{
        text: "Technical skills"
      },
      data: [
      {
       type: "doughnut",
       dataPoints: [
       {  y: 53.37, indexLabel: "Python" },
       {  y: 35.0, indexLabel: "SQL" },
       {  y: 7, indexLabel: "Power BI" },
       {  y: 2, indexLabel: "Rstudio" },
       {  y: 5, indexLabel: "Others" }
       ]
     }
     ]
   });

    chart.render();
  }

  