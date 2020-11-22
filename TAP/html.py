def getPrint(data):

    file = open("..\\output\\main.html", "w")
    file.write(getHeader())
    file.write(getBodyBegin())

    testNum = '1'

    flag = 0
    for x in range(0, len(data.test)):

        if data.test.__getitem__(x)[0] != 'ok':
            flag = 1

    if flag == 0:
        file.write(allTestCorrect(testNum))
    else:
        file.write(notAllTestCorrect(testNum))

    count = 0
    for x in range(0, len(data.test)):

        if data.test.__getitem__(x)[0] == 'ok':
            file.write(
                testCorrect(data.test.__getitem__(x)[0], data.test.__getitem__(x)[1], data.test.__getitem__(x)[2], 0))
        else:
            file.write(
                testIncorrect(data.test.__getitem__(x)[0], data.test.__getitem__(x)[1], data.test.__getitem__(x)[2], 0))


        #       f"  subtests : {data.test.__getitem__(x)[3]}")
        # if data.test.__getitem__(x)[-1] > 0:
        #     for y in range(0, data.test.__getitem__(x)[-1]):
        #         print((data.subtests.__getitem__(count)[-1] * "\t") +
        #               f"subtest {data.subtests.__getitem__(count)[0]} : "
        #               f"{data.subtests.__getitem__(count)[1]} "
        #               f"{data.subtests.__getitem__(count)[2]}"),
        #         count += 1


    file.write(testEnd())
    file.write(getBodyEnd())
    file.close()


def getHeader():
    return ('''<!DOCTYPE html>
        <html lang='en'>
        <head>
          <title>PL - Trabalho</title>
          <meta charset='utf-8'>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
          <style>
            /* Set height of the grid so .sidenav can be 100% (adjust if needed) */
            .row.content {height: 1500px}
        
            /* Set gray background color and 100% height */
            .sidenav {
              background-color: #f1f1f1;
              height: 100%;
            }
        
            /* Set black background color, white text and some padding */
            footer {
              background-color: #555;
              color: white;
              padding: 15px;
            }
        
            /* On small screens, set height to 'auto' for sidenav and grid */
            @media screen and (max-width: 767px) {
              .sidenav {
                height: auto;
                padding: 15px;
              }
              .row.content {height: auto;}
            }
          </style>
        </head>''')


def getBodyBegin():
    return ('''<body>
        <div class="container-fluid">
          <div class="row content">
            <div class="col-sm-2 col-md-2 sidenav">
              <h4>Processamento de Linguagens</h4>
            </div>
        
        
            <div class="col-sm-10 col-md-10">
              <h1>Testes</h1>
              <hr>''')


def getBodyEnd():
    return ('''</div>
                  </div>
                </div>
                
                <footer class="container-fluid">
                  <p>Footer Text</p>
                </footer>
                
                </body>
        </html>''')


def allTestCorrect(data):
    return('''<p><h2><a data-toggle="collapse" href="#collapseTeste''' + data + '''" class="text-success">
      Teste ''' + data + '''
      </a></h2></p>
      <div class="collapse" id="collapseTeste''' + data + '''">
      ''')


def notAllTestCorrect(data):
    return('''<p><h2><a data-toggle="collapse" href="#collapseTeste''' + data + '''" class="text-danger">
          Teste ''' + data + '''
      </a></h2></p>
      <div class="collapse" id="collapseTeste''' + data + '''">
      ''')

def testEnd():
    return('''</div>''')


def tab():
    return ("&emsp;")


def testCorrect(status, offset, text, level):
    return('''<h4><a class="text-success">''' + tab()*level + status + ''' ''' + offset + ''' ''' + text + '''</a></h4>'''
       )


def testIncorrect(status, offset, text, level):
    return('''<h4><a class="text-danger"> ''' + tab()*level + status + ''' ''' + offset + ''' ''' + text + '''</a></h4>'''
        )