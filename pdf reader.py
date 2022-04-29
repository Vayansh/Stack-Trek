import tabula
pdf="tables_sample.pdf"
dsf=tabula.read_pdf(pdf,pages="1")
for i in range(len(dsf)):
    dsf[i].to_csv(f"table_output{i}.csv")
    
    
