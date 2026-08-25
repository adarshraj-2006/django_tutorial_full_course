# Django Forms & Settings Revision Notes

This document contains a summary of the issues identified in the project, the solutions applied, and key points to remember for future Django development.

---

## 🔍 Identified Errors & Solutions

### 1. Swapped Database & Static Directory Configuration
* **The Error**:
  In `formscore/settings.py`, the database path and the static root directories were swapped:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'static',  # ❌ Swapped with static directory
      }
  }
  # ...
  STATIC_ROOT = BASE_DIR / 'db.sqlite3',  # ❌ Swapped with DB file + trailing comma
  ```
  This caused Django to point to a `static` file instead of the actual `db.sqlite3` database file where all migrations had been applied. It also created a database file named `static` and made `STATIC_ROOT` a tuple due to the trailing comma.
* **The Solution**:
  Reverted the settings to point the database back to `db.sqlite3` and the static root to `static` without the trailing comma:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',  #   Correct database file
      }
  }
  # ...
  STATIC_ROOT = BASE_DIR / 'static'  #   Correct static directory (no trailing comma)
  ```

### 2. Missing Form Inputs in `order.html`
* **The Error**:
  Inside the form loop in `pizza/templates/pizza/order.html`, the fields were iterated over, but the actual HTML input element (`{{ field }}`) was never rendered:
  ```html
  {% for field in pizzaform %}
      <div class="form-group">
          {{ field.errors }}
          {{ field.label_tag }}
          <!-- ❌ The field input itself was missing! -->
      </div>
  {% endfor %}
  ```
  This resulted in only labels and errors showing up on the page without any text fields or dropdowns for user input.
* **The Solution**:
  Used `widget_tweaks` to render the correct Bootstrap input/select classes:
  ```html
  {% for field in pizzaform %}
      <div class="form-group mb-3">
          <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
          {{ field.errors }}
          
          {% if field.name == 'size' %}
              {{ field|add_class:"form-select" }}
          {% else %}
              {{ field|add_class:"form-control" }}
          {% endif %}
      </div>
  {% endfor %}
  ```

---

## 📌 Points to Remember & Best Practices

### Django Settings
1. **Avoid Trailing Commas on String Settings**:
   Adding a trailing comma (e.g., `STATIC_ROOT = BASE_DIR / 'db.sqlite3',`) turns the variable into a **Tuple** instead of a path or string, causing configuration errors down the line.
2. **Database Verification**:
   If Django behaves as though your database tables do not exist even after running `python manage.py migrate`, double-check the `'NAME'` path in `DATABASES`.

### Django Templates & Forms
1. **Always Output the Field**:
   When looping over form fields manually in templates, you must render `{{ field }}` or apply filters like `{{ field|add_class:"..." }}` to ensure the input fields display.
2. **Rendering Fields Individually**:
   If using custom styles, check field names or field types to selectively apply classes (e.g., `.form-select` for select dropdowns and `.form-control` for text inputs).
3. **Load `widget_tweaks`**:
   To add classes dynamically to form widgets inside templates, ensure `{% load widget_tweaks %}` is placed at the top of the template block.

### CSS Page Backgrounds
1. **Full Page Backgrounds**:
   To make a background cover the entire viewport on all pages, apply the styling to the `body` tag in the base template:
   ```css
   body {
       background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("{% static 'image.jpg' %}");
       background-size: cover;
       background-position: center;
       background-repeat: no-repeat;
       background-attachment: fixed;
       min-height: 100vh;
   }
   ```
2. **Readability Overlay**:
   Using a semi-transparent dark linear gradient overlay (`linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7))`) on top of a background image ensures that foreground text remains highly legible.
