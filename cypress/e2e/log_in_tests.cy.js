describe('Attempt log in withinvalid user name and password', {
},() => {
  it('should error for invalid user', () => {
    cy.visit('/')
    cy.get(':nth-child(1) > .form-signin > :nth-child(3) > #username').type(Cypress.env('INVALIDUSERNAME'))
    cy.get(':nth-child(1) > .form-signin > :nth-child(4) > #password').type(Cypress.env('INVALIDPASSWORD'))
    cy.get(':nth-child(1) > .form-signin > .btn').click()
    cy.get('h1').and("have.text", "Invalid username or password")
  })
})

