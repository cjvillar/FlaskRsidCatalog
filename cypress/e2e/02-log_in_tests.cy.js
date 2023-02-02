describe("Sign in with valid user", {}, () => {
  it("should log in for test user", () => {
    cy.visit("/");
    cy.get("input[name=username]").type(Cypress.env("USERNAME"));
    cy.get("input[name=password]").type(Cypress.env("PASSWORD"));
    cy.contains("Sign In").click();
    cy.get("h1").should("contain", Cypress.env("USERNAME"));
    cy.contains("Log Out").click();
  });
});

describe("Attempt log in withinvalid user name and password", {}, () => {
  it("should error for invalid user", () => {
    cy.visit("/");
    cy.get("input[name=username]").type(Cypress.env("INVALIDUSERNAME"), {
      log: false,
    });
    cy.get("input[name=password]").type(Cypress.env("INVALIDPASSWORD"), {
      log: false,
    });
    cy.contains("Sign In").click();
    cy.get("ul").should("contain", "Invalid username or password");
  });
});
