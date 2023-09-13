from django.urls import path
from userapp import views


urlpatterns=[
     path("",views.home_fn,name='home_fn'),
     path('login2_fn/',views.login2_fn,name='login2_fn'),
     path('saveregistration_fn/',views.saveregistration_fn,name='saveregistration_fn'),
     path('signup_fn/',views.signup_fn,name='signup_fn'),
     path('userlogout/',views.userlogout,name='userlogout'),
     path('main_fn/',views.main_fn,name='main_fn'),
     path('registration_fn/',views.registration_fn,name='registration_fn'),
     path('saveregister_fn/',views.saveregister_fn,name='saveregister_fn'),
     path('user_login/',views.user_login,name='user_login'),
     path('gallery_fn/',views.gallery_fn,name='gallery_fn'),
     path('malegallery_fn/',views.malegallery_fn,name='malegallery_fn'),
     path('viewprofile_fn/<int:dataid>/',views.viewprofile_fn,name='viewprofile_fn'),
     path('savemessage_fn/',views.savemessage_fn,name='savemessage_fn'),
     # path('receivemsg_fn/',views.receivemsg_fn,name='receivemsg_fn'),

     path('sendmessage_fn/',views.sendmessage_fn,name='sendmessage_fn'),
     path('deletemessage/<int:dataid>/',views.deletemessage,name='deletemessage'),
     path('deletereceive_msg/<int:dataid>/',views.deletereceive_msg,name='deletereceive_msg'),
     path('displayuser_details/',views.displayuser_details,name='displayuser_details'),
     path('updateuser_details/',views.updateuser_details,name='updateuser_details'),
     path('general_info/<int:dataid>/',views.general_info,name='general_info'),
     path('familydetail_fn/<int:dataid>/',views.familydetail_fn,name='familydetail_fn'),
     path('educationdetail_fn/<int:dataid>/',views.educationdetail_fn,name='educationdetail_fn'),
     path('text_msg_fn/<int:dataid>/',views.text_msg_fn,name='text_msg_fn'),
     path('requestedmsg_fn/',views.requestedmsg_fn,name='requestedmsg_fn'),
     path('text_feedback_fn/',views.text_feedback_fn,name='text_feedback_fn'),
     path('savefeedback_fn/',views.savefeedback_fn,name='savefeedback_fn'),
     path('contact_fn/',views.contact_fn,name='contact_fn'),
     path('contactsave/',views.contactsave,name='contactsave'),
     path('deleteuserpage_fn/',views.deleteuserpage_fn,name='deleteuserpage_fn'),
     path('text_successstory_fn/',views.text_successstory_fn,name='text_successstory_fn'),
     path('story_save/',views.story_save,name='story_save'),
     path('viewstory_fn/',views.viewstory_fn,name='viewstory_fn'),
     path('updatesuccessstory_fn/',views.updatesuccessstory_fn,name='updatesuccessstory_fn'),
     path('deletesuccess_story/',views.deletesuccess_story,name='deletesuccess_story'),
     path('viewallstories/',views.viewallstories,name='viewallstories'),
     path('viewallstories2/',views.viewallstories2,name='viewallstories2'),
     path('singleviewstory_fn/<int:dataid>/',views.singleviewstory_fn,name='singleviewstory_fn'),
     path('about_fn/',views.about_fn,name='about_fn'),
     path('viewuserprofile/',views.viewuserprofile,name='viewuserprofile'),

     path('search_results/', views.search_results, name='search_results'),

     # path('savefeedback_fn/',views.savefeedback_fn,name='savefeedback_fn'),
     # path('text_feedback/<int:dataid>/',views.text_feedback,name='text_feedback'),

     # path('messages_view/',views.messages_view,name='messages_view'),
     # path('editloginuser_fn/<int:dataid>/',views.editloginuser_fn,name='editloginuser_fn'),

     # path('displayallcustomer_fn/',views.displayallcustomer_fn,name='displayallcustomer_fn'),
     # path('deletecustomer_fn/<int:dataid>/',views.deletecustomer_fn,name='deletecustomer_fn'),

]