VERSAO = "SELECT @@VERSION AS versao"

TAMANHO_BANCOS = """
SELECT DB_NAME(database_id) AS banco,
       SUM(size) * 8 / 1024 AS tamanho_mb
FROM sys.master_files
GROUP BY database_id
ORDER BY tamanho_mb DESC
"""

SESSOES_ATIVAS = """
SELECT s.session_id, s.login_name, s.host_name, s.status,
       r.command, r.wait_type, r.total_elapsed_time/1000 AS segundos
FROM sys.dm_exec_sessions s
LEFT JOIN sys.dm_exec_requests r ON s.session_id = r.session_id
WHERE s.is_user_process = 1
"""

TOP_ESPERAS = """
SELECT TOP 10 wait_type, wait_time_ms/1000 AS segundos, waiting_tasks_count
FROM sys.dm_os_wait_stats
WHERE wait_type NOT LIKE '%SLEEP%' AND wait_type NOT LIKE '%QUEUE%'
ORDER BY wait_time_ms DESC
"""
