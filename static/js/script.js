// Sample Chart.js Implementation
const revenueCtx = document.getElementById('revenueChart').getContext('2d');
const expensesCtx = document.getElementById('expensesChart').getContext('2d');
const salesCtx = document.getElementById('salesChart').getContext('2d');

const createChart = (ctx, label, data) => {
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
      datasets: [{
        label: label,
        data: data,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      }
    }
  });
};

createChart(revenueCtx, 'Revenue', [800, 700, 900, 1000, 850, 950, 1050]);
createChart(expensesCtx, 'Expenses', [400, 500, 450, 600, 550, 500, 480]);
createChart(salesCtx, 'Sales', [150, 200, 250, 300, 350, 400, 450]);
