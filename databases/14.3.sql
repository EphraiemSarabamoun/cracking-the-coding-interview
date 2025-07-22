UPDATE r  
SET r.status = 'Closed'
FROM Requests r
JOIN Apartments a ON r.apartment_id = a.apartment_id
JOIN Buildings b ON a.building_id = b.building_id
WHERE r.status = 'Open' 
AND b.building_id = 11;
