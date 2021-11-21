import pandas as p
import os
import pytest


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
names = p.read_excel(os.path.join(project_dir, "groups.xlsx"))
lst = []
n = 0
for o in names.itertuples():
    v = str(o)
    v = v.replace(f"Pandas(Index={n}, Names='", "")
    v = v.replace("')", "")
    lst.append(v)
    n += 1

@pytest.mark.parametrize("group", lst, ids=[repr(x) for x in lst])
def test_add_group(app, group):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    old_list = str(old_list)
    new_list = str(new_list)
    assert sorted(old_list.translate({ord(i): None for i in '\')'})) == sorted(new_list.translate({ord(i): None for i in '\')'}))


