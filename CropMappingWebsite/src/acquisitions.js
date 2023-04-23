import Chart from 'chart.js/auto'
const totalTypeNumber = [
  { type: "Field X", count: 10 },
  { type: "Field P", count: 20 },
  { type: "Field G", count: 15 },
  { type: "Field T", count: 25 },
  { type: "Field C", count: 22 },
  { type: "Field D", count: 30 },
  { type: "Field V", count: 28 },
  { type: "Field YP", count: 28 },
];

const srandValues = [
  { type: "Field X", count: 10 },
  { type: "Field P", count: 20 },
  { type: "Field G", count: 15 },
  { type: "Field T", count: 25 },
  { type: "Field C", count: 22 },
  { type: "Field D", count: 30 },
  { type: "Field V", count: 28 },
  { type: "Field YP", count: 28 },
];

(async function() {
  const etValues = [
    { type: "Field X", count: 10 },
    { type: "Field P", count: 20 },
    { type: "Field G", count: 15 },
    { type: "Field T", count: 25 },
    { type: "Field C", count: 22 },
    { type: "Field D", count: 30 },
    { type: "Field V", count: 28 },
    { type: "Field YP", count: 28 },
  ];


  new Chart(
    document.getElementById('acquisitions'),
    {
      type: 'pie',
      data: {
        labels: totalTypeNumber.map(row => row.type),
        datasets: [
          {
            label: 'Total #of Crops per Field Type',
            data: totalTypeNumber.map(row => row.count),
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
        labels: etValues.map(row => row.type),
        datasets: [
          {
            label: 'ET Value Averages Per type',
            data: etValues.map(row => row.count)
          }
        ]
      }
    }
  );

  new Chart(
    document.getElementById('moreData'),
    {
      type: 'bar',
      data: {
        labels: srandValues.map(row => row.type),
        datasets: [
          {
            label: 'sRand Averages Per Field Type',
            data: srandValues.map(row => row.count)
          }
        ]
      }
    }
  );

})();
