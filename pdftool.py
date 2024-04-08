# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:45:54 2021

@author: CT
"""

import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

def mergePdf(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合并的文档的 list
    :param outFile:    合并后的输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter()
    for inFile in inFileList:
        # 依次循环打开要合并文件
        pdfReader = PdfFileReader(open(inFile, 'rb'))
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)

        # 最后,统一写入到输出文件中
        pdfFileWriter.write(open(outFile, 'wb'))
        

readFile1 = r'D:\desktop\北交所打新资格申请材料\3. 产品合同\财通证券资管智汇87号单一资产管理计划资产管理合同.pdf'
readFile2 = r'D:\desktop\北交所打新资格申请材料\3. 产品合同\补充协议\财通证券资管智汇87号单一资产管理计划补充协议.pdf'



outFile = r'D:\desktop\北交所打新资格申请材料\3. 产品合同\合并版\智汇87号合同更新.pdf'

mergePdf([readFile1,readFile2],outFile)



























