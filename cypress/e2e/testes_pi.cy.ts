describe('Cenários de testes', () => {
  const urlHome = 'https://pi-2022-g5.vercel.app/';
  const urlProfissional = 'https://pi-2022-g5.vercel.app/#profissional';
  const urlFuncionamento = 'https://pi-2022-g5.vercel.app/#funcionamento';
  const urlBeneficios = 'https://pi-2022-g5.vercel.app/#beneficios';
  const profissionalButton = '#id-profissionalButton';
  const funcionamentoButton = '#id-funcionamentoButton';
  const beneficiosButton = '#id-beneficiosButton';
  const contatoButton = '#id-contatoButton';
  const nomeInput = '#id-nomeInput';
  const telefoneInput = '#id-telefoneInput';
  const emailInput = '#id-emailInput';
  const msgInput = '#id-msgInput';
  const enviarMsgButton = '#id-enviarMsgButton'
  const contatoCard = '#contato'
  const msgAVisoErro = '#id-msgAvisoErro'

  beforeEach(() => {
    cy.visit(urlHome);
  });

  it('Deve acessar a urlHome e validar se a página está abrindo corretamente', () => {
    cy.url().should('eq', urlHome);
  });

  it('Deve acessar a urlHome, clicar em profissionalButton e validar se a url muda para urlProfissional', () => {
    cy.get(profissionalButton).click();
    cy.url().should('eq', urlProfissional);
  });

  it('Deve acessar a urlHome, clicar em funcionamentoButton e validar se a url muda para urlFuncionamento', () => {
    cy.get(funcionamentoButton).click();
    cy.url().should('eq', urlFuncionamento);
  });

  it('Deve acessar a urlHome, clicar em beneficiosButton e validar se a url muda para urlBeneficios', () => {
    cy.get(beneficiosButton).click();
    cy.url().should('eq', urlBeneficios);
  });

  it('Deve acessar a urlHome, clicar em contatoButton e validar se contatoCard é visível', () => {
    cy.get(contatoButton).click();
    cy.get(contatoCard).should('be.visible');
  });

  it('Deve preencher o formulário de contato e validar se a mensagem de sucesso é visível', () => {
    cy.get(nomeInput).type('Teste Teste Teste');
    cy.get(telefoneInput).type('1234567890');
    cy.get(emailInput).type('teste@teste.com');
    cy.get(msgInput).type('Teste Teste Teste');
    cy.get(enviarMsgButton).click();
    cy.get(msgAVisoErro).should('not.be.visible');
  });






})