import pandas as p
import os
import pytest
from model.group import Group


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
names = p.read_excel(os.path.join(project_dir, "groups.xlsx"))
lst = []
n = 0
for o,p in names.itertuples():
    lst.append(Group(name=p))

@pytest.mark.parametrize("group", lst, ids=[repr(x) for x in lst])
def test_add_group(app, group):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(str(group))
    assert sorted(old_list) == sorted(new_list)


