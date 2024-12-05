from jinja2 import Template, TemplateError
import os


def main():
    """Создание контракта."""
    try:
        # Проверяем, существует ли файл шаблона
        template_file = "contract_template.txt"
        if not os.path.exists(template_file):
            raise FileNotFoundError(f"Файл шаблона '{template_file}' не найден.")

        # Данные для подстановки
        data = {
            "contract_number": "12345",
            "city": "Москва",
            "date": "05 декабря 2024",
            "party1": "ООО Ромашка",
            "party2": "ИП Иванов Иван Иванович",
            "amount": "500000",
            "deadline": "31 декабря 2024",
            "obligation1": "предоставить услуги по разработке ПО",
            "obligation2": "осуществить оплату в полном объеме"
        }

        # Читаем шаблон из файла
        try:
            with open(template_file, "r", encoding="utf-8") as file:
                template_content = file.read()
        except Exception as e:
            raise IOError(f"Ошибка чтения файла шаблона: {e}")

        # Создаем объект шаблона Jinja2
        try:
            template = Template(template_content)
        except TemplateError as e:
            raise ValueError(f"Ошибка в шаблоне Jinja2: {e}")

        # Генерируем договор
        try:
            rendered_contract = template.render(data)
        except TemplateError as e:
            raise ValueError(f"Ошибка при генерации договора: {e}")

        # Сохраняем результат в новый файл
        output_file = "generated_contract.txt"
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(rendered_contract)
        except Exception as e:
            raise IOError(f"Ошибка записи в файл '{output_file}': {e}")

        print("Договор успешно сгенерирован!")

    except FileNotFoundError as fnf_error:
        print(f"Ошибка: {fnf_error}")
    except IOError as io_error:
        print(f"Ошибка ввода-вывода: {io_error}")
    except ValueError as value_error:
        print(f"Ошибка данных: {value_error}")
    except Exception as general_error:
        print(f"Непредвиденная ошибка: {general_error}")


if __name__ == "__main__":
    main()
