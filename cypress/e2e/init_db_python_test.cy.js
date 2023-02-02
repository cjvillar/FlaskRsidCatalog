it("seed db with python scrtip", () =>{
    cy.exec("python init_db.py").then((data)=>{
        cy.log(data.stdout);
    })
})