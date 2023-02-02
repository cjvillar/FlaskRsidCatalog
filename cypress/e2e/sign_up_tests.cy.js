describe("Sign up ne user", {}, () => {
  it("should log in for new user", () => {
    cy.visit("/");
    cy.contains("Sign Up").click();
    cy.get("input[id=new_username]").type(Cypress.env("NEWUSERNAME"));
    cy.get("input[id=new_password]").type(Cypress.env("NEWPASSWORD"));
    cy.contains("Sign Up").click();
    cy.get("h1").should("contain", Cypress.env("NEWUSERNAME"));
    cy.contains("Log Out").click();
  });
});
