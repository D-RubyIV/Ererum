import os

ROOT_PATH = os.getcwd()


class StyleSheet:

    Q_MENU_CSS = """
        QMenu
        {   
            color: #f0f2f5;
            font: 10.5px;
            background-color: #303031;
            border-radius: 3px;
        }

        QMenu::item
        {
            color: #cfd1d5;
            background-color: #303031;
        }

        QMenu::item:selected
        {
            color: #0e0e0e;
            background-color: rgb(170,170,255);
        }

        QMenu::item:hover
        {
            color: #0e0e0e;
            background-color: rgb(170,170,255);
        }

        QMenu::separator
        {
            height: 1px;
            background-color: #565656;
            margin-left: 5px;
            margin-right: 5px;
        }

        QMenu::indicator:checked
        {
            background-color: rgb(85, 170, 255);
        }

        QMenu::indicator:unchecked
        {
            background-color: #303031;
        }

        QMenu::submenu
        {
            background-color: #303031;
            border-radius: 3px;
        }

        QMenu::submenu:pressed
        {
            background-color: rgb(170,170,255);
        }

        QMenu::submenu:hover
        {
            background-color: rgb(170,170,255);
        }

        QMenu::submenu:selected
        {
            background-color: rgb(170,170,255);
        }
        """
