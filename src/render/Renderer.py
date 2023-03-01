class Renderer:
    # on fait des methodes pour chaque page et le header et le footer
    @staticmethod
    def get_header(title="Quizz"):
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
                <title>{}</title>
                <link rel="stylesheet" type="text/css" href="css/main.css"/>
                <link rel="icon" type="image/png" href="img/icon.png"/>
                <script type="text/javascript" src="fonctions.js"></script>
            </head>
            <body>
                <header>
                    <nav>
                        <ul>
                            <li><a href="head.html">Accueil</a></li>
                        </ul>
                    </nav>
                </header>
        '''.format(title)

    @staticmethod
    def get_footer():
        return '''
            </body>
        </html>
        '''



