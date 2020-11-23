def get_print(data):
    file = open("..\\output\\main.html", "w")
    file.write(getHeader())
    file.write(getBodyBegin())

    for file_count in range(0, len(data)):
        test_num = file_count + 1

        flag = 0
        for x in range(0, len(data[file_count].test)):

            if data[file_count].test.__getitem__(x)[0] != 'ok':
                flag = 1
                break

        if flag == 0:
            file.write(allTestCorrect(test_num))
        else:
            file.write(notAllTestCorrect(test_num))

        count = 0
        n_incorrect = 0

        for x in range(0, len(data[file_count].test)):
            if data[file_count].test.__getitem__(x)[0] == "ok":
                file.write(
                    testCorrect(data[file_count].test.__getitem__(x)[0], data[file_count].test.__getitem__(x)[1],
                                data[file_count].test.__getitem__(x)[2],
                                0))
            else:
                file.write(
                    testIncorrect(data[file_count].test.__getitem__(x)[0], data[file_count].test.__getitem__(x)[1],
                                  data[file_count].test.__getitem__(x)[2],
                                  0))
                n_incorrect = n_incorrect + 1
            if data[file_count].test.__getitem__(x)[-1] > 0:
                for y in range(0, len(data[file_count].subtest)):
                    if data[file_count].subtest.__getitem__(count)[0] == "ok":
                        file.write(
                            testCorrect(data[file_count].subtest.__getitem__(count)[0],
                                        data[file_count].subtest.__getitem__(count)[1],
                                        data[file_count].subtest.__getitem__(count)[2],
                                        data[file_count].subtest.__getitem__(count)[-1]))
                    else:
                        file.write(
                            testIncorrect(data[file_count].subtest.__getitem__(count)[0],
                                          data[file_count].subtest.__getitem__(count)[1],
                                          data[file_count].subtest.__getitem__(count)[2],
                                          data[file_count].subtest.__getitem__(count)[-1]))
                        n_incorrect = n_incorrect + 1
                    count += 1

        file.write(testDefs(len(data[file_count].test), n_incorrect))
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
                  <p>Jose Cosgrove 18826 & Andre Cardoso 18848</p>
                </footer>
                
                </body>
        </html>''')


def allTestCorrect(data):
    return ('''<p><h2><a data-toggle="collapse" href="#collapseTeste''' + str(data) + '''" class="text-success">
      Teste ''' + str(data) + '''
      </a></h2></p>
      <div class="collapse" id="collapseTeste''' + str(data) + '''">
      ''')


def notAllTestCorrect(data):
    return ('''<p><h2><a data-toggle="collapse" href="#collapseTeste''' + str(data) + '''" class="text-danger">
          Teste ''' + str(data) + '''
      </a></h2></p>
      <div class="collapse" id="collapseTeste''' + str(data) + '''">
      ''')


def testEnd():
    return '''</div>'''


def tab():
    return "&emsp;"


def testCorrect(status, offset, text, level):
    return ('''<h4><a class="text-success">''' + (tab() * level) + status + ''' ''' + offset + ''' ''' + text +
            '''</a></h4>''')


def testIncorrect(status, offset, text, level):
    return ('''<h4><a class="text-danger"> ''' + (tab() * level) + status + ''' ''' + offset + ''' ''' + text +
            '''</a></h4>''')


def testDefs(total, incorrect):
    return '''<h5><br><p>Total de Testes: ''' + str(total) + '''</p><p>Percentagem de Falhas: ''' + str(
        (incorrect / total) * 100) + '''%</p></h5>'''
