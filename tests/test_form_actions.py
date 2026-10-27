from playwright.sync_api import Page, expect


def test_checkbox_selection(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator('input[type="checkbox"]').nth(0)

    checkbox.check()

    expect(checkbox).to_be_checked()


def test_checkbox_unselection(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator('input[type="checkbox"]').nth(1)

    # Second checkbox is checked by default
    expect(checkbox).to_be_checked()

    checkbox.uncheck()

    expect(checkbox).not_to_be_checked()


def test_checkbox_not_selected_by_default(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator('input[type="checkbox"]').nth(0)

    # Without any action, first checkbox must stay unchecked
    expect(checkbox).not_to_be_checked()