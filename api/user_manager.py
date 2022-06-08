# 主要实现用户增删改查
from api.base import Base
from loguru import logger


class UserManager(Base):


    #初始化接口路径
    def __init__(self):
        self.add_user_url = self.get_url('/admin/admin/create')
        self.edit_user_url = self.get_url('/admin/admin/update')
        self.search_user_url = self.get_url('/admin/admin/list?page=1&limit=20&sort=add_time&order=desc')
        self.delete_user_url = self.get_url('/admin/admin/delete')



    # 新增管理员
    def add_user(self,username,password,**kwargs):
        user_data = {'username':username,'password':password}
        if kwargs:
            logger.info("添加管理员可选参数:{}",**kwargs)
            user_data.update(**kwargs)
        return self.post(self.add_user_url,user_data)

    # 查询管理员
    def search_user(self):
        pass

    # 修改管理员
    def edit_user(self,id,username,password,**kwargs):
        user_data = {'username': username, 'id':id,'password':password}
        if kwargs:
            user_data.update(**kwargs)
        return self.post(self.edit_user_url, user_data)

    # 删除管理员
    def delete_user(self,id,username,**kwargs):
        ### 请求的事删除接口
        user_data = {'username': username, 'id': id}
        if kwargs:
            user_data.update(**kwargs)
        return self.post(self.delete_user_url, user_data)
























