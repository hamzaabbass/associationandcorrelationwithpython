import numpy as np
import scipy.stats


# Prepare data
x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
z = np.array([5, 3, 2, 1, 0, -2, -8, -11, -15, -16])

# Rank data
rank_x = scipy.stats.rankdata(x)
rank_y = scipy.stats.rankdata(y)
rank_z = scipy.stats.rankdata(z)

# Calculate correlation
correlation_xy = np.corrcoef(x, y)[0, 1]
correlation_xz = np.corrcoef(x, z)[0, 1]
correlation_yz = np.corrcoef(y, z)[0, 1]

# Prepare HTML content
html_content = """
<html>
<head>
    <title>Data Mining Results</title>
</head>
<body>
    <h1>Rank of Data</h1>
    <p>Rank of x: {}</p>
    <p>Rank of y: {}</p>
    <p>Rank of z: {}</p>

    <h1>Correlation</h1>
    <p>Correlation between x and y: {}</p>
    <p>Correlation between x and z: {}</p>
    <p>Correlation between y and z: {}</p>
</body>
</html>
""".format(rank_x, rank_y, rank_z, correlation_xy, correlation_xz, correlation_yz)

# Save the HTML content to a file
with open('index.html', 'w') as f:
    f.write(html_content)

print("Results saved to index.html")
