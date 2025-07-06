
class HtmlMaker:
    def __init__(self):
        pass

    def make(self, content) -> str:
        return f"""
        <html>
        <head>
          <style>
            body {{ font-family: 'Helvetica', sans-serif; margin: 2em; }}
            h1 {{ color: #2c3e50; font-size: 2.5em; }}
            h2, h3 {{ color: #2c3e50; margin-top: 2em; }}
            img {{ 
                max-width: 40%; 
                height: auto; 
                vertical-align: middle;
                display: block;
                margin-left:  auto;  
                margin-right: auto;
                margin-top: 1em;
            }}
            h1 + * img {{
                max-width: 60%;
            }}
            p {{ line-height: 1.6; }}
            li {{ margin-bottom: 1em; }}
            .custom-line {{
              border: none;
              height: 4px;
              background: #4cb7ac;
              margin-bottom: 2em;
              margin-top: 0;
              width: 100%;
            }}
          </style>
        </head>
        <body>
        <hr class="custom-line">
        {content}
        <hr class="custom-line">
        </body>
        </html>
        """