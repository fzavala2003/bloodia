"""Cinco pruebas funcionales de regresión para Bloodia."""

import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = os.getenv("BLOODIA_BASE_URL", "http://localhost:8000/")


@pytest.fixture
def bloodia(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 15).until(
        lambda browser: browser.execute_script("return document.readyState")
        == "complete"
    )
    return driver


def test_mobile_menu_opens(bloodia):
    """El botón móvil abre el menú."""
    bloodia.set_window_size(390, 844)
    bloodia.refresh()

    menu = bloodia.find_element(By.ID, "nav-list")
    bloodia.find_element(By.ID, "btn-burger").click()

    assert "open" in menu.get_attribute("class").split()


def test_logo_returns_to_home(bloodia):
    """El logotipo permite regresar a Inicio."""
    bloodia.find_element(By.LINK_TEXT, "Galería").click()
    WebDriverWait(bloodia, 10).until(
        lambda browser: browser.current_url.endswith("imagenes.html")
    )

    bloodia.find_element(By.CSS_SELECTOR, "a.brand").click()
    WebDriverWait(bloodia, 10).until(
        lambda browser: browser.current_url.endswith("index.html")
    )

    assert bloodia.find_element(By.TAG_NAME, "body").is_displayed()


def test_navigation_menu_loads_each_page(bloodia):
    """Cada página del menú carga su HTML."""
    pages = {
        "Inicio": "index.html",
        "Galería": "imagenes.html",
        "Vocabulario": "vocabulario.html",
        "Bibliografía": "bibliografia.html",
    }

    for option, expected_page in pages.items():
        bloodia.get(BASE_URL)
        bloodia.find_element(By.LINK_TEXT, option).click()

        WebDriverWait(bloodia, 10).until(
            lambda browser: (
                browser.current_url.endswith(expected_page)
                and browser.execute_script("return document.readyState")
                == "complete"
            )
        )

        body = bloodia.find_element(By.TAG_NAME, "body")
        assert body.is_displayed()
        assert body.text.strip()


def test_visible_images_still_load(bloodia):
    """Todas las imágenes cargan correctamente."""
    images = bloodia.find_elements(By.TAG_NAME, "img")
    assert images, "No se encontraron imágenes"
    assert all(
        bloodia.execute_script(
            "return arguments[0].complete && arguments[0].naturalWidth > 0",
            image,
        )
        for image in images
    )


def test_internal_links_have_valid_destination(bloodia):
    """Todos los enlaces tienen un destino."""
    links = bloodia.find_elements(By.CSS_SELECTOR, "a[href]")
    assert links, "No se encontraron enlaces"
    assert all(link.get_attribute("href") for link in links)
