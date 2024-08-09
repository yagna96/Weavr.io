select AVG(END_TIMESTAMP- CREATION_TIMESTAMP) as duration , transaction_id , MONTH(CREATION_TIMESTAMP) as month
from transaction_time 
where YEAR(CREATION_TIMESTAMP) == 2024
group by MONTH(CREATION_TIMESTAMP)

