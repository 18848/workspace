
class Test:
    def __init__(self, status, offset, text, comment, test, subtests):
        self.status = status
        self.offset = offset
        self.text = text
        self.comment = comment
        self.test = test #[("", "", "", -1), ]
        self.subtests = subtests #[("", "", "", -1), ]

    def getPrint(self):
        if self.ok == "ok":
            return "yes %s %s" % (self.status, self.offset)
        else:
            return "no %s %s" % (self.status, self.offset)

    def printTests(self):
        tabs=""
        for x in range(self.nivel-1):
            tabs += "\t"
        print("%s%s"% (tabs,self.getPrint()))
        if self.subtests:
            self.printSTests()

    def printHTML(self):
        html=""
        if self.nivel==1:
            if len(self.subtests)>0:
                if self.ok==True:
                    html = '''<div class="test_header_ok">
                                                <h2>''' + self.getPrint() + '''</h2>
                                                <button data-toggle=collapse data-target="#teste''' + str(self.id) + '''" type="button" class="btn btn-success"
                                                    style="transform:translateY(-20%); ">
                                                Ver subtestes
                                                </button>
                                            </div>'''

                    html += '''<div id="teste''' + str(self.id) + '''" class="collapse">'''
                    for sub in self.subtests:
                        html += sub.printHTML()

                    html += '''</div>'''
                else:
                    html = '''<div class="test_header_notok">
                                                <h2>''' + self.getPrint() + '''</h2>
                                                <button data-toggle=collapse data-target="#teste''' + str(self.id) + '''" type="button" class="btn btn-danger"
                                                    style="transform:translateY(-20%); ">
                                                Ver subtestes
                                                </button>
                                            </div>'''

                    html += '''<div id="teste''' + str(self.id) + '''" class="collapse">'''
                    for sub in self.subtests:
                        html += sub.printHTML()

                    html += '''</div>'''
            else:
                if self.ok==True:
                    html='''<div>
                                <div class="test_header_ok">
                                    <h2> '''+ self.getPrint() +'''</h2>
                                </div>
                            </div>'''
                else:
                    html = '''<div>
                                <div class="test_header_notok">
                                    <h2> ''' + self.getPrint() + '''</h2>
                                </div>
                            </div>'''
        else:
            if len(self.subtests) > 0:
                if self.ok== True:
                    margin= (self.nivel-1)*40
                    html+='''<div class="subtest" style="margin-left: '''+str(margin)+'''px">
                                <div class="card w-50">
                                    <div class="subtest_content_ok">
                                        '''+self.getPrint()+'''
                                    </div>
                                </div>
                            </div>'''
                    for sub in self.subtests:
                        html+=sub.printHTML()
                else:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_notok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
                    for sub in self.subtests:
                        html+=sub.printHTML()
            else:
                if self.ok== True:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_ok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
                else:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_notok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''

        return html

    def printSTests(self):
        for test_ in self.subtests:
            test_.printTests()
