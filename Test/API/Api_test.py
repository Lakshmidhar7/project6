from Keywords.key_fun import Keyword

c_functions = Keyword()

c_functions.get_function('https://reqres.in/api/users?page=2')
c_functions.get_function('https://reqres.in/api/users/2')
c_functions.get_function('https://reqres.in/api/users/23')
c_functions.get_function('https://reqres.in/api/unknown')
c_functions.get_function('https://reqres.in/api/unknown/2')
c_functions.post('https://reqres.in/api/users')
c_functions.put('https://reqres.in/api/users/2')
c_functions.patch('https://reqres.in/api/users/2')
c_functions.delete('https://reqres.in/api/users/2')
c_functions.post_res('https://reqres.in/api/register')
c_functions.post_register('https://reqres.in/api/register')
c_functions.post_login('https://reqres.in/api/login')
c_functions.post_log('https://reqres.in/api/login')
