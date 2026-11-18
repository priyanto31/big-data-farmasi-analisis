-- Kueri Analisis Pendapatan & Risiko Kedaluwarsa
SELECT branch, category, SUM(revenue) AS total_revenue
FROM pharmacy_supply_chain
GROUP BY branch, category
ORDER BY total_revenue DESC;