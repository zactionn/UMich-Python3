nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 
'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 
'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
#US_count = [nested_d['Beijing']['USA'], nested_d['London']['USA'], nested_d['Rio']['USA']]

US_count = [nested_d[olympics]['USA'] for olympics in nested_d]

