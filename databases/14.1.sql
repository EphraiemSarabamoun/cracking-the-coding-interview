SELECT t.tenant_name
FROM Tenants t
JOIN TenantApartments ta ON t.tenant_id = ta.tenant_id
GROUP BY t.tenant_id
HAVING COUNT(ta.apartment_id) > 1