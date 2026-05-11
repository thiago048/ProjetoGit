def test_002_fazer_pix(common_page,login_page, home_page,pix_page) -> None:
    login_page.login("user1", "pass1")
    login_page.assert_login_sucessful()
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("999.999.999.99","10")
    pix_page.assert_pix_Realizado()
    pix_page.voltar_home()
    common_page.assert_text("4.990,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("11/05/2026 - Pix para 999.999")


