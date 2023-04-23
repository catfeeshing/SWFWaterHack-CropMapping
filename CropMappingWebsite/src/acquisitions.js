import Chart from 'chart.js/auto'

(async function() {
  const data = [
    { year: "Field X", count: 10 },
    { year: "Field P", count: 20 },
    { year: "Field G", count: 15 },
    { year: "Field T", count: 25 },
    { year: "Field C", count: 22 },
    { year: "Field D", count: 30 },
    { year: "Field V", count: 28 },
  ];

  new Chart(
    document.getElementById('acquisitions'),
    {
      type: 'pie',
      data: {
        labels: data.map(row => row.year),
        datasets: [
          {
            label: 'Acquisitions by year',
            data: data.map(row => row.count)
          }
        ]
      }
    }
  );


  new Chart(
    document.getElementById('extraData'),
    {
      type: 'bar',
      data: {
        labels: data.map(row => row.year),
        datasets: [
          {
            label: 'Acquisitions by year',
            data: data.map(row => row.count)
          }
        ]
      }
    }
  );

  new Chart(
    document.getElementById('moreData'),
    {
      type: 'scatter',
      data: {
        labels: data.map(row => row.year),
        datasets: [
          {
            label: 'Acquisitions by year',
            data: data.map(row => row.count), 
          }
        ]
      }
    }
  );

})();
