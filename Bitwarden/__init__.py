# -*- coding: utf-8 -*-

"""Evaluate simple python expressions. Use it with care every keystroke triggers an evaluation."""

from albertv0 import *
import json
import subprocess
import os

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Bitwarden"
__version__ = "1.0"
__trigger__ = "bw "
__author__ = "Daniel van der Ende"
__dependencies__ = []


iconPath = os.path.dirname(__file__)+"/python.svg"


def handleQuery(query):
    if query.isTriggered:
        item = Item(id=__prettyname__, completion=query.rawString)
        stripped = query.string.strip().split()
        item.text = "hello item1 {0}".format(stripped)
        if stripped[0] == 'search':
            return search_login(stripped[1])

        item2 = Item(id=__prettyname__, completion=query.rawString)
        item2.text = "Hello item2"

        return [item, item2]

        # if stripped == '':
        #     item.text = "Enter a python expression"
        #     item.subtext = "Math is in the namespace and, if installed, also Numpy as 'np'"
        #     return item
        # else:
        #     try:
        #         result = eval(stripped)
        #     except Exception as ex:
        #         result = ex
        #     item.text = str(result)
        #     item.subtext = type(result).__name__
        #     item.addAction(ClipAction("Copy result to clipboard", str(result)))
        #     item.addAction(FuncAction("Execute", lambda: exec(str(result))))
        # return item


def search_login(needle):
    p = subprocess.Popen(["bw", "list", "items", "--search", needle, "--session", "YOUR_SESSION_KEY_HERE"], stdout=subprocess.PIPE)
    res = p.communicate()
    logins = json.loads(res[0].decode())

    items_found = []
    for el in logins:
        item = Item(id=__prettyname__, text=el['name'])
        item.addAction(ClipAction("Copy result to clipboard", el['login']['password']))
        items_found.append(item)
    return items_found
