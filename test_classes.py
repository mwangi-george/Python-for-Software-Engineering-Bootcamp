from classes import NtdModelingWorkshop

nairobi_workshop = NtdModelingWorkshop(
    countries=["Kenya", "Ethiopia", "Zimbabwe", "Nigeria", "Rwanda"],
    partners=["inSupply Health", "CHAI", "SightSavers", "CEMA"],
    donors=["BMGF"]
)

print(nairobi_workshop.workshop_participants())

print(nairobi_workshop.countries)

# Accessing attributes directly without instanciating the class
print(NtdModelingWorkshop.next_host())
