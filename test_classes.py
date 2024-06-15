from classes import Library, PostMordernLibrary, Books, NtdModelingWorkshop

nairobi_workshop = NtdModelingWorkshop(
    countries=["Kenya", "Ethiopia", "Zimbabwe", "Nigeria", "Rwanda"],
    partners=["inSupply Health", "CHAI", "SightSavers", "CEMA"],
    donors=["BMGF"]
)

print(nairobi_workshop.workshop_participants())

print(nairobi_workshop.countries)

# Accessing attributes directly without instanciating the class
print(NtdModelingWorkshop.next_host())

pml = PostMordernLibrary("Kenya")
print(f"pml has {pml.print_floors()} floors")
print(pml.librarian_name())

print(pml)
