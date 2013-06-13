## Script (Python) "isIE6Or7"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Detect IE 6 or 7

user_agent = container.REQUEST['HTTP_USER_AGENT'].lower()

return (user_agent.find('msie 7.0')!=-1) or (user_agent.find('msie 6.0')!=-1)
