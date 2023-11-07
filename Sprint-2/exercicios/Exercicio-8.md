# E8
## Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

```sql
SELECT v.cdvdd, v.nmvdd
FROM tbvendedor v
JOIN (
    SELECT cdvdd, COUNT(*) AS num_vendas
    FROM tbvendas
    WHERE status = 'Concluído'
    GROUP BY cdvdd
    ORDER BY num_vendas DESC
    LIMIT 1
) t ON v.cdvdd = t.cdvdd;

```