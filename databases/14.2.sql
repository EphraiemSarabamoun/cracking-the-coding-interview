SELECT b.building_name, COUNT(r.request_id) as open_requests
FROM Buildings b 
JOIN Apartments a ON b.building_id = a.building_id
JOIN Requests r ON a.apartment_id = r.apartment_id
WHERE r.status = "Open"
GROUP BY b.building_id